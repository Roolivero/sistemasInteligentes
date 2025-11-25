import os
import shutil
import warnings
from pathlib import Path

import tensorflow as tf
from absl import logging as absl_logging
from mediapipe_model_maker import object_detector
from mediapipe_model_maker.python.vision.object_detector import model_spec as ms

SCRIPT_DIR = Path(__file__).resolve().parent
DATASET_DIR = SCRIPT_DIR / "Hard Hat Sample.v2-augmented-416x416.voc"
CACHE_DIR = DATASET_DIR / "cache"
MODEL_DIR = SCRIPT_DIR / "models"
MODEL_PATH = MODEL_DIR / "mobilenet_v2_float"
MODEL_QUAN_PATH = MODEL_DIR / "mobilenet_v2_qat.tflite"

# Reducir verbosidad de logs C++ de TensorFlow (0=all, 1=INFO, 2=WARNING, 3=ERROR)
os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "3")

#============================================================================
# HIPERPARÁMETROS DE ENTRENAMIENTO
# ============================================================================

# EPOCHS: Número de veces que el modelo verá todo el dataset completo
# - Valores típicos: 20-100 para object detection
# - Más épocas = mejor aprendizaje, pero riesgo de overfitting
# - 30 épocas es un buen balance para datasets medianos
EPOCHS = 15

# LEARNING_RATE: Tasa de aprendizaje - controla qué tan grandes son los ajustes de pesos
# - Valores típicos: 0.001 - 0.3 para object detection
# - Muy alto (>0.5): el modelo no converge, loss oscila
# - Muy bajo (<0.001): entrenamiento muy lento
# - 0.15 es agresivo pero efectivo para QAT (Quantization Aware Training)
LEARNING_RATE = 0.15

# BATCH_SIZE: Número de imágenes procesadas simultáneamente antes de actualizar pesos
# - Valores típicos: 4-32 dependiendo de memoria GPU/CPU
# - Más alto: entrenamiento más rápido pero requiere más memoria
# - Más bajo: más estable pero más lento
# - 8 es ideal para GPUs con memoria limitada (4-8GB) o CPUs
BATCH_SIZE = 4

# DECAY_STEPS: Cada cuántos pasos (batches) se reduce el learning rate
# - Se usa con DECAY_RATE para implementar "learning rate decay"
# - 8 pasos significa que cada 8 batches se aplicará la reducción
# - Ayuda a que el modelo haga ajustes más finos conforme avanza el entrenamiento
DECAY_STEPS = 8

# DECAY_RATE: Factor de multiplicación para reducir el learning rate
# - Nuevo LR = LR actual × DECAY_RATE
# - 0.96 significa reducción del 4% cada DECAY_STEPS
# - Valores típicos: 0.9-0.99
# - Permite convergencia más suave: ajustes grandes al inicio, finos al final
DECAY_RATE = 0.96


def ensure_dataset_dirs(dataset_dir: Path):
    """Valida que el dataset exista donde esperamos."""
    train_dir = dataset_dir / "train"
    val_dir = dataset_dir / "valid"
    if not train_dir.exists() or not val_dir.exists():
        raise FileNotFoundError(
            f"No se encontraron las carpetas 'train' y 'valid' en {dataset_dir}. "
            "Copia el dataset completo junto a este script: redes_neuronales_si/Hard Hat Sample.v2-augmented-416x416.voc"
        )
    return train_dir, val_dir


def normalize_voc_dirs(dataset_dir: Path):
    """Normaliza nombres de carpetas a lo que MediaPipe espera (images en minúsculas)."""
    for split in ("train", "valid", "test"):
        split_dir = dataset_dir / split
        if not split_dir.exists():
            continue
        images_upper = split_dir / "Images"
        images_lower = split_dir / "images"
        if images_upper.exists() and not images_lower.exists():
            images_upper.rename(images_lower)
        elif images_upper.exists() and images_lower.exists():
            raise FileExistsError(
                f"Se encontraron 'Images' y 'images' en {split_dir}. "
                "Unifica en una sola carpeta 'images'."
            )


def ensure_cache_structure(cache_dir: Path):
    """Crea la estructura de cache que MediaPipe necesita."""
    if cache_dir.exists():
        shutil.rmtree(cache_dir)

    (cache_dir / "train").mkdir(parents=True, exist_ok=True)
    (cache_dir / "valid").mkdir(parents=True, exist_ok=True)


def reduce_verbosity():
    """Silencia warnings/INFO de TF, absl y python para limpiar la salida."""
    warnings.filterwarnings("ignore", category=UserWarning)
    warnings.filterwarnings("ignore", category=FutureWarning)
    absl_logging.set_verbosity(absl_logging.ERROR)
    tf.get_logger().setLevel("ERROR")
    tf.autograph.set_verbosity(0)


def configure_tensorflow():
    """Muestra si hay GPU disponible y activa logs de colocación de dispositivos."""
    gpus = tf.config.list_physical_devices("GPU")
    print("GPUs disponibles:", gpus)
    if not gpus:
        print("No se detectó GPU; se usará CPU.")
        return

    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)

    # tf.debugging.set_log_device_placement(True)  # Descomenta para ver trazas detalladas CPU/GPU
    # print("Log de colocación de dispositivos activado (CPU/GPU).")


def main():
    reduce_verbosity()
    configure_tensorflow()
    normalize_voc_dirs(DATASET_DIR)
    train_dir, val_dir = ensure_dataset_dirs(DATASET_DIR)

    print("Creando estructura de cache...")
    ensure_cache_structure(CACHE_DIR)

    print("Cargando dataset...")
    train_data = object_detector.Dataset.from_pascal_voc_folder(
        data_dir=str(train_dir),
        cache_dir=str(CACHE_DIR / "train")
    )
    val_data = object_detector.Dataset.from_pascal_voc_folder(
        data_dir=str(val_dir),
        cache_dir=str(CACHE_DIR / "valid")
    )

    print(f"Train dataset cargado")
    print(f"Val dataset cargado")
    print(f"Clases: {train_data.label_names}")

    spec = ms.SupportedModels.MOBILENET_V2

    # Crear directorio para el modelo si no existe
    os.makedirs(MODEL_PATH, exist_ok=True)

    hparams = object_detector.HParams(
        export_dir=str(MODEL_PATH),
        epochs=EPOCHS
    )

    options = object_detector.ObjectDetectorOptions(
        supported_model=spec,
        hparams=hparams
    )
    options.model_options = object_detector.ModelOptions(l2_weight_decay=3e-05)

    print("\n=== PASO 1: Entrenando modelo FLOAT ===")
    model = object_detector.ObjectDetector.create(
        train_data=train_data,
        validation_data=val_data,
        options=options
    )

    print("\nEvaluando modelo float...")
    loss, metrics = model.evaluate(val_data)
    print("Float model - Loss: ", loss)
    print("Métricas:", metrics)

    # Si metrics es un diccionario o lista con estructura conocida
    if isinstance(metrics, dict):
        for key, value in metrics.items():
            print(f"  {key}: {value:.4f}" if isinstance(value, float) else f"  {key}: {value}")
    elif isinstance(metrics, list) and len(metrics) > 0:
        print(f"  mAP: {metrics[0]:.4f}" if isinstance(metrics[0], (int, float)) else f"  Métricas: {metrics}")

    # Exportar modelo float
    float_model_path = MODEL_PATH / "model_float.tflite"
    model.export_model(str(float_model_path))
    print(f"Modelo float exportado: {float_model_path}")

    print("\n=== PASO 2: Quantization Aware Training ===")
    qat_hparams = object_detector.QATHParams(
        learning_rate=LEARNING_RATE,
        batch_size=BATCH_SIZE,
        epochs=EPOCHS,
        decay_steps=DECAY_STEPS,
        decay_rate=DECAY_RATE
    )

    print("Restaurando checkpoint float...")
    model.restore_float_ckpt()

    print("Iniciando QAT...")
    model.quantization_aware_training(train_data, val_data, qat_hparams=qat_hparams)

    print("\nEvaluando modelo cuantizado...")
    loss, metrics = model.evaluate(val_data)
    print("QAT model - Loss: ", loss)
    print("Métricas:", metrics)

    print(f"\nExportando modelo cuantizado: {MODEL_QUAN_PATH}")
    model.export_model(str(MODEL_QUAN_PATH))
    print("¡Entrenamiento completo!")
    print(f"\nResumen:")
    print(f"- Modelo float: {float_model_path}")
    print(f"- Modelo cuantizado: {MODEL_QUAN_PATH}")


if __name__ == "__main__":
    main()
