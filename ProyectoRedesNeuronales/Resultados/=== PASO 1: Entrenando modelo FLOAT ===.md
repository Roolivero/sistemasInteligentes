=== PASO 1: Entrenando modelo FLOAT ===
/mnt/sda1/code/si/ProyectoRedesNeuronales/.venv/lib/python3.9/site-packages/keras/src/engine/functional.py:642: UserWarning: Input dict contained keys ['6'] which did not match any model input. They will be ignored by the model.
  inputs = self._flatten_to_reference_inputs(inputs)
WARNING:tensorflow:`tf.keras.layers.experimental.SyncBatchNormalization` endpoint is deprecated and will be removed in a future release. Please use `tf.keras.layers.BatchNormalization` with parameter `synchronized` set to True.
WARNING:tensorflow:`tf.keras.layers.experimental.SyncBatchNormalization` endpoint is deprecated and will be removed in a future release. Please use `tf.keras.layers.BatchNormalization` with parameter `synchronized` set to True.
Using existing files at /tmp/model_maker/object_detector/mobilenetv2_i256
Model: "retina_net_model"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 mobile_net (MobileNet)      {'2': (None, 64, 64, 24   2257984   
                             ),                                  
                              '3': (None, 32, 32, 32             
                             ),                                  
                              '4': (None, 16, 16, 96             
                             ),                                  
                              '5': (None, 8, 8, 320)             
                             , '6': (None, 8, 8, 128             
                             0)}                                 
                                                                 
 fpn (FPN)                   {'5': (None, 8, 8, 128)   149056    
                             , '4': (None, 16, 16, 1             
                             28),                                
                              '3': (None, 32, 32, 12             
                             8),                                 
                              '6': (None, 4, 4, 128)             
                             , '7': (None, 2, 2, 128             
                             )}                                  
                                                                 
 multilevel_detection_gener  multiple                  0 (unused)
 ator (MultilevelDetectionG                                      
 enerator)                                                       
                                                                 
 retina_net_head (RetinaNet  ({'3': (None, 32, 32, 3   173384    
 Head)                       6),                                 
                              '4': (None, 16, 16, 36             
                             ),                                  
                              '5': (None, 8, 8, 36),             
                              '6': (None, 4, 4, 36),             
                              '7': (None, 2, 2, 36)}             
                             , {'3': (None, 32, 32,              
                             36),                                
                              '4': (None, 16, 16, 36             
                             ),                                  
                              '5': (None, 8, 8, 36),             
                              '6': (None, 4, 4, 36),             
                              '7': (None, 2, 2, 36)}             
                             , {})                               
                                                                 
=================================================================
Total params: 2580424 (9.84 MB)
Trainable params: 2534792 (9.67 MB)
Non-trainable params: 45632 (178.25 KB)
_________________________________________________________________
Epoch 1/3
/mnt/sda1/code/si/ProyectoRedesNeuronales/.venv/lib/python3.9/site-packages/keras/src/backend.py:452: UserWarning: `tf.keras.backend.set_learning_phase` is deprecated and will be removed after 2020-10-11. To update it, simply pass a True/False value to the `training` argument of the `__call__` method of your layer or model.
  warnings.warn(
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
26/26 [==============================] - 53s 1s/step - total_loss: 2.3438 - cls_loss: 1.8572 - box_loss: 0.0086 - model_loss: 2.2888 - val_total_loss: 1.1466 - val_cls_loss: 0.8472 - val_box_loss: 0.0049 - val_model_loss: 1.0916
Epoch 2/3
26/26 [==============================] - 25s 968ms/step - total_loss: 1.0254 - cls_loss: 0.6954 - box_loss: 0.0055 - model_loss: 0.9704 - val_total_loss: 0.8970 - val_cls_loss: 0.6429 - val_box_loss: 0.0040 - val_model_loss: 0.8421
Epoch 3/3
26/26 [==============================] - 26s 1s/step - total_loss: 0.7804 - cls_loss: 0.5086 - box_loss: 0.0043 - model_loss: 0.7254 - val_total_loss: 0.7923 - val_cls_loss: 0.5312 - val_box_loss: 0.0041 - val_model_loss: 0.7373

Evaluando modelo float...
20/20 [==============================] - 1s 27ms/step - total_loss: 0.7936 - cls_loss: 0.5198 - box_loss: 0.0044 - model_loss: 0.7386
creating index...
index created!
creating index...
index created!
Running per image evaluation...
Evaluate annotation type *bbox*
DONE (t=0.09s).
Accumulating evaluation results...
DONE (t=0.02s).
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.157
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.322
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.140
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.133
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.158
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.761
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.133
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.314
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.335
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.200
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.336
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.800
Float model - Loss:  [0.7935795187950134, 0.5197941064834595, 0.004375881049782038, 0.7385881543159485]
Métricas: {'AP': 0.15667768, 'AP50': 0.32178828, 'AP75': 0.1399784, 'APs': 0.1332045, 'APm': 0.1575024, 'APl': 0.7610561, 'ARmax1': 0.13259259, 'ARmax10': 0.31444445, 'ARmax100': 0.3351852, 'ARs': 0.2, 'ARm': 0.33592594, 'ARl': 0.8}
  AP: 0.15667767822742462
  AP50: 0.3217882812023163
  AP75: 0.13997839391231537
  APs: 0.13320450484752655
  APm: 0.15750239789485931
  APl: 0.761056125164032
  ARmax1: 0.1325925886631012
  ARmax10: 0.3144444525241852
  ARmax100: 0.3351851999759674
  ARs: 0.20000000298023224
  ARm: 0.3359259366989136
  ARl: 0.800000011920929
Exporting a floating point model

Esto usamos:

EPOCHS = 2
LEARNING_RATE = 0.001
BATCH_SIZE = 4
DECAY_STEPS = 50
DECAY_RATE = 0.95

------------------------------------
------------------------------------


=== PASO 1: Entrenando modelo FLOAT ===
/mnt/sda1/code/si/ProyectoRedesNeuronales/.venv/lib/python3.9/site-packages/keras/src/engine/functional.py:642: UserWarning: Input dict contained keys ['6'] which did not match any model input. They will be ignored by the model.
  inputs = self._flatten_to_reference_inputs(inputs)
WARNING:tensorflow:`tf.keras.layers.experimental.SyncBatchNormalization` endpoint is deprecated and will be removed in a future release. Please use `tf.keras.layers.BatchNormalization` with parameter `synchronized` set to True.
WARNING:tensorflow:`tf.keras.layers.experimental.SyncBatchNormalization` endpoint is deprecated and will be removed in a future release. Please use `tf.keras.layers.BatchNormalization` with parameter `synchronized` set to True.
Using existing files at /tmp/model_maker/object_detector/mobilenetv2_i256
Model: "retina_net_model"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 mobile_net (MobileNet)      {'2': (None, 64, 64, 24   2257984   
                             ),                                  
                              '3': (None, 32, 32, 32             
                             ),                                  
                              '4': (None, 16, 16, 96             
                             ),                                  
                              '5': (None, 8, 8, 320)             
                             , '6': (None, 8, 8, 128             
                             0)}                                 
                                                                 
 fpn (FPN)                   {'5': (None, 8, 8, 128)   149056    
                             , '4': (None, 16, 16, 1             
                             28),                                
                              '3': (None, 32, 32, 12             
                             8),                                 
                              '6': (None, 4, 4, 128)             
                             , '7': (None, 2, 2, 128             
                             )}                                  
                                                                 
 multilevel_detection_gener  multiple                  0 (unused)
 ator (MultilevelDetectionG                                      
 enerator)                                                       
                                                                 
 retina_net_head (RetinaNet  ({'3': (None, 32, 32, 3   173384    
 Head)                       6),                                 
                              '4': (None, 16, 16, 36             
                             ),                                  
                              '5': (None, 8, 8, 36),             
                              '6': (None, 4, 4, 36),             
                              '7': (None, 2, 2, 36)}             
                             , {'3': (None, 32, 32,              
                             36),                                
                              '4': (None, 16, 16, 36             
                             ),                                  
                              '5': (None, 8, 8, 36),             
                              '6': (None, 4, 4, 36),             
                              '7': (None, 2, 2, 36)}             
                             , {})                               
                                                                 
=================================================================
Total params: 2580424 (9.84 MB)
Trainable params: 2534792 (9.67 MB)
Non-trainable params: 45632 (178.25 KB)
_________________________________________________________________
Epoch 1/3
/mnt/sda1/code/si/ProyectoRedesNeuronales/.venv/lib/python3.9/site-packages/keras/src/backend.py:452: UserWarning: `tf.keras.backend.set_learning_phase` is deprecated and will be removed after 2020-10-11. To update it, simply pass a True/False value to the `training` argument of the `__call__` method of your layer or model.
  warnings.warn(
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
26/26 [==============================] - 49s 1s/step - total_loss: 2.3830 - cls_loss: 1.8908 - box_loss: 0.0087 - model_loss: 2.3280 - val_total_loss: 1.2354 - val_cls_loss: 0.9148 - val_box_loss: 0.0053 - val_model_loss: 1.1805
Epoch 2/3
26/26 [==============================] - 23s 896ms/step - total_loss: 1.0860 - cls_loss: 0.7507 - box_loss: 0.0056 - model_loss: 1.0310 - val_total_loss: 0.9015 - val_cls_loss: 0.6389 - val_box_loss: 0.0042 - val_model_loss: 0.8465
Epoch 3/3
26/26 [==============================] - 30s 1s/step - total_loss: 0.8186 - cls_loss: 0.5358 - box_loss: 0.0046 - model_loss: 0.7636 - val_total_loss: 0.7745 - val_cls_loss: 0.5152 - val_box_loss: 0.0041 - val_model_loss: 0.7195

Evaluando modelo float...
20/20 [==============================] - 1s 25ms/step - total_loss: 0.8304 - cls_loss: 0.5586 - box_loss: 0.0043 - model_loss: 0.7754
creating index...
index created!
creating index...
index created!
Running per image evaluation...
Evaluate annotation type *bbox*
DONE (t=0.38s).
Accumulating evaluation results...
DONE (t=0.18s).
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.191
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.374
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.190
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.054
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.217
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.739
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.216
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.511
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.523
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.156
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.530
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.750
Float model - Loss:  [0.8303885459899902, 0.5585849285125732, 0.004336201585829258, 0.7753950357437134]
Métricas: {'AP': 0.19083539, 'AP50': 0.374429, 'AP75': 0.18965422, 'APs': 0.053826313, 'APm': 0.21741681, 'APl': 0.7392739, 'ARmax1': 0.21592593, 'ARmax10': 0.51148146, 'ARmax100': 0.5233333, 'ARs': 0.15555556, 'ARm': 0.52962965, 'ARl': 0.75}
  AP: 0.1908353865146637
  AP50: 0.37442898750305176
  AP75: 0.18965421617031097
  APs: 0.053826313465833664
  APm: 0.21741680800914764
  APl: 0.7392739057540894
  ARmax1: 0.215925931930542
  ARmax10: 0.5114814639091492
  ARmax100: 0.5233333110809326
  ARs: 0.15555556118488312
  ARm: 0.529629647731781
  ARl: 0.75
Exporting a floating point model



Evaluando modelo cuantizado...
20/20 [==============================] - 1s 40ms/step - total_loss: 1.9337 - cls_loss: 1.2257 - box_loss: 0.0142 - model_loss: 1.9337
creating index...
index created!
creating index...
index created!
Running per image evaluation...
Evaluate annotation type *bbox*
DONE (t=0.06s).
Accumulating evaluation results...
DONE (t=0.01s).
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.000
QAT model - Loss:  [1.933744192123413, 1.225687861442566, 0.014161127619445324, 1.933744192123413]
Métricas: {'AP': 0.0, 'AP50': 0.0, 'AP75': 0.0, 'APs': 0.0, 'APm': 0.0, 'APl': 0.0, 'ARmax1': 0.0, 'ARmax10': 0.0, 'ARmax100': 0.0, 'ARs': 0.0, 'ARm': 0.0, 'ARl': 0.0}



Esto usamos:

EPOCHS = 2
LEARNING_RATE = 0.15
BATCH_SIZE = 4
DECAY_STEPS = 50
DECAY_RATE = 0.95


----------------------------------------------------
----------------------------------------------------

Usamos:
EPOCHS = 3
LEARNING_RATE = 0.001
BATCH_SIZE = 4
DECAY_STEPS = 50
DECAY_RATE = 0.95


=== PASO 1: Entrenando modelo FLOAT ===
/mnt/sda1/code/si/ProyectoRedesNeuronales/.venv/lib/python3.9/site-packages/keras/src/engine/functional.py:642: UserWarning: Input dict contained keys ['6'] which did not match any model input. They will be ignored by the model.
  inputs = self._flatten_to_reference_inputs(inputs)
WARNING:tensorflow:`tf.keras.layers.experimental.SyncBatchNormalization` endpoint is deprecated and will be removed in a future release. Please use `tf.keras.layers.BatchNormalization` with parameter `synchronized` set to True.
WARNING:tensorflow:`tf.keras.layers.experimental.SyncBatchNormalization` endpoint is deprecated and will be removed in a future release. Please use `tf.keras.layers.BatchNormalization` with parameter `synchronized` set to True.
Using existing files at /tmp/model_maker/object_detector/mobilenetv2_i256
Model: "retina_net_model"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 mobile_net (MobileNet)      {'2': (None, 64, 64, 24   2257984   
                             ),                                  
                              '3': (None, 32, 32, 32             
                             ),                                  
                              '4': (None, 16, 16, 96             
                             ),                                  
                              '5': (None, 8, 8, 320)             
                             , '6': (None, 8, 8, 128             
                             0)}                                 
                                                                 
 fpn (FPN)                   {'5': (None, 8, 8, 128)   149056    
                             , '4': (None, 16, 16, 1             
                             28),                                
                              '3': (None, 32, 32, 12             
                             8),                                 
                              '6': (None, 4, 4, 128)             
                             , '7': (None, 2, 2, 128             
                             )}                                  
                                                                 
 multilevel_detection_gener  multiple                  0 (unused)
 ator (MultilevelDetectionG                                      
 enerator)                                                       
                                                                 
 retina_net_head (RetinaNet  ({'3': (None, 32, 32, 3   173384    
 Head)                       6),                                 
                              '4': (None, 16, 16, 36             
                             ),                                  
                              '5': (None, 8, 8, 36),             
                              '6': (None, 4, 4, 36),             
                              '7': (None, 2, 2, 36)}             
                             , {'3': (None, 32, 32,              
                             36),                                
                              '4': (None, 16, 16, 36             
                             ),                                  
                              '5': (None, 8, 8, 36),             
                              '6': (None, 4, 4, 36),             
                              '7': (None, 2, 2, 36)}             
                             , {})                               
                                                                 
=================================================================
Total params: 2580424 (9.84 MB)
Trainable params: 2534792 (9.67 MB)
Non-trainable params: 45632 (178.25 KB)
_________________________________________________________________
Epoch 1/3
/mnt/sda1/code/si/ProyectoRedesNeuronales/.venv/lib/python3.9/site-packages/keras/src/backend.py:452: UserWarning: `tf.keras.backend.set_learning_phase` is deprecated and will be removed after 2020-10-11. To update it, simply pass a True/False value to the `training` argument of the `__call__` method of your layer or model.
  warnings.warn(
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
26/26 [==============================] - 50s 1s/step - total_loss: 3.1281 - cls_loss: 2.6371 - box_loss: 0.0087 - model_loss: 3.0731 - val_total_loss: 1.2499 - val_cls_loss: 0.9498 - val_box_loss: 0.0049 - val_model_loss: 1.1949
Epoch 2/3
26/26 [==============================] - 25s 962ms/step - total_loss: 1.1403 - cls_loss: 0.7935 - box_loss: 0.0058 - model_loss: 1.0854 - val_total_loss: 0.9384 - val_cls_loss: 0.6807 - val_box_loss: 0.0041 - val_model_loss: 0.8834
Epoch 3/3
26/26 [==============================] - 27s 1s/step - total_loss: 0.8394 - cls_loss: 0.5583 - box_loss: 0.0045 - model_loss: 0.7844 - val_total_loss: 0.7919 - val_cls_loss: 0.5508 - val_box_loss: 0.0037 - val_model_loss: 0.7369

Evaluando modelo float...
20/20 [==============================] - 1s 28ms/step - total_loss: 0.8328 - cls_loss: 0.5845 - box_loss: 0.0039 - model_loss: 0.7778
creating index...
index created!
creating index...
index created!
Running per image evaluation...
Evaluate annotation type *bbox*
DONE (t=0.09s).
Accumulating evaluation results...
DONE (t=0.09s).
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.151
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.287
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.163
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.098
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.158
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.721
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.090
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.318
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.326
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.167
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.341
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.750
Float model - Loss:  [0.8328272700309753, 0.5844664573669434, 0.0038675335235893726, 0.777843177318573]
Métricas: {'AP': 0.1505339, 'AP50': 0.28690633, 'AP75': 0.16319183, 'APs': 0.09827531, 'APm': 0.15822339, 'APl': 0.72132015, 'ARmax1': 0.08962963, 'ARmax10': 0.31777778, 'ARmax100': 0.32555556, 'ARs': 0.16666667, 'ARm': 0.34111112, 'ARl': 0.75}
  AP: 0.15053389966487885
  AP50: 0.28690633177757263
  AP75: 0.16319182515144348
  APs: 0.0982753112912178
  APm: 0.15822339057922363
  APl: 0.7213201522827148
  ARmax1: 0.089629627764225
  ARmax10: 0.3177777826786041
  ARmax100: 0.32555556297302246
  ARs: 0.1666666716337204
  ARm: 0.34111112356185913
  ARl: 0.75
Exporting a floating point model


=== PASO 2: Quantization Aware Training ===
Restaurando checkpoint float...
/mnt/sda1/code/si/ProyectoRedesNeuronales/.venv/lib/python3.9/site-packages/keras/src/engine/functional.py:642: UserWarning: Input dict contained keys ['6'] which did not match any model input. They will be ignored by the model.
  inputs = self._flatten_to_reference_inputs(inputs)
Using existing files at /tmp/model_maker/object_detector/mobilenetv2_i256
Model: "retina_net_model_2"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 mobile_net_1 (MobileNet)    {'2': (None, 64, 64, 24   2257984   
                             ),                                  
                              '3': (None, 32, 32, 32             
                             ),                                  
                              '4': (None, 16, 16, 96             
                             ),                                  
                              '5': (None, 8, 8, 320)             
                             , '6': (None, 8, 8, 128             
                             0)}                                 
                                                                 
 fpn_1 (FPN)                 {'5': (None, 8, 8, 128)   149056    
                             , '4': (None, 16, 16, 1             
                             28),                                
                              '3': (None, 32, 32, 12             
                             8),                                 
                              '6': (None, 4, 4, 128)             
                             , '7': (None, 2, 2, 128             
                             )}                                  
                                                                 
 multilevel_detection_gener  multiple                  0 (unused)
 ator_2 (MultilevelDetectio                                      
 nGenerator)                                                     
                                                                 
 retina_net_head_1 (RetinaN  ({'3': (None, 32, 32, 3   173384    
 etHead)                     6),                                 
                              '4': (None, 16, 16, 36             
                             ),                                  
                              '5': (None, 8, 8, 36),             
                              '6': (None, 4, 4, 36),             
                              '7': (None, 2, 2, 36)}             
                             , {'3': (None, 32, 32,              
                             36),                                
                              '4': (None, 16, 16, 36             
                             ),                                  
                              '5': (None, 8, 8, 36),             
                              '6': (None, 4, 4, 36),             
                              '7': (None, 2, 2, 36)}             
                             , {})                               
                                                                 
=================================================================
Total params: 2580424 (9.84 MB)
Trainable params: 2534792 (9.67 MB)
Non-trainable params: 45632 (178.25 KB)
_________________________________________________________________
Iniciando QAT...
WARNING:tensorflow:`tf.keras.layers.experimental.SyncBatchNormalization` endpoint is deprecated and will be removed in a future release. Please use `tf.keras.layers.BatchNormalization` with parameter `synchronized` set to True.
WARNING:tensorflow:`tf.keras.layers.experimental.SyncBatchNormalization` endpoint is deprecated and will be removed in a future release. Please use `tf.keras.layers.BatchNormalization` with parameter `synchronized` set to True.
Epoch 1/3
/mnt/sda1/code/si/ProyectoRedesNeuronales/.venv/lib/python3.9/site-packages/keras/src/backend.py:452: UserWarning: `tf.keras.backend.set_learning_phase` is deprecated and will be removed after 2020-10-11. To update it, simply pass a True/False value to the `training` argument of the `__call__` method of your layer or model.
  warnings.warn(
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
52/52 [==============================] - 73s 742ms/step - total_loss: 2.6936 - cls_loss: 1.1217 - box_loss: 0.0314 - model_loss: 2.6936 - val_total_loss: 2.4658 - val_cls_loss: 1.5079 - val_box_loss: 0.0192 - val_model_loss: 2.4658
Epoch 2/3
52/52 [==============================] - 37s 719ms/step - total_loss: 2.0708 - cls_loss: 1.0292 - box_loss: 0.0208 - model_loss: 2.0708 - val_total_loss: 2.2237 - val_cls_loss: 1.4971 - val_box_loss: 0.0145 - val_model_loss: 2.2237
Epoch 3/3
52/52 [==============================] - 33s 626ms/step - total_loss: 1.8620 - cls_loss: 0.9678 - box_loss: 0.0179 - model_loss: 1.8620 - val_total_loss: 2.0554 - val_cls_loss: 1.3788 - val_box_loss: 0.0135 - val_model_loss: 2.0554

Evaluando modelo cuantizado...
20/20 [==============================] - 1s 45ms/step - total_loss: 1.9778 - cls_loss: 1.3061 - box_loss: 0.0134 - model_loss: 1.9778
creating index...
index created!
creating index...
index created!
Running per image evaluation...
Evaluate annotation type *bbox*
DONE (t=0.06s).
Accumulating evaluation results...
DONE (t=0.02s).
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.000
QAT model - Loss:  [1.9777898788452148, 1.306074619293213, 0.013434302993118763, 1.9777898788452148]
Métricas: {'AP': 0.0, 'AP50': 0.0, 'AP75': 0.0, 'APs': 0.0, 'APm': 0.0, 'APl': 0.0, 'ARmax1': 0.0, 'ARmax10': 0.0, 'ARmax100': 0.0, 'ARs': 0.0, 'ARm': 0.0, 'ARl': 0.0}


-----------------------------------------------------
-----------------------------------------------------



Usamos:
EPOCHS = 2
LEARNING_RATE = 0.15
BATCH_SIZE = 4
DECAY_STEPS = 8
DECAY_RATE = 0.96

== PASO 1: Entrenando modelo FLOAT ===
/mnt/sda1/code/si/ProyectoRedesNeuronales/.venv/lib/python3.9/site-packages/keras/src/engine/functional.py:642: UserWarning: Input dict contained keys ['6'] which did not match any model input. They will be ignored by the model.
  inputs = self._flatten_to_reference_inputs(inputs)
WARNING:tensorflow:`tf.keras.layers.experimental.SyncBatchNormalization` endpoint is deprecated and will be removed in a future release. Please use `tf.keras.layers.BatchNormalization` with parameter `synchronized` set to True.
WARNING:tensorflow:`tf.keras.layers.experimental.SyncBatchNormalization` endpoint is deprecated and will be removed in a future release. Please use `tf.keras.layers.BatchNormalization` with parameter `synchronized` set to True.
Using existing files at /tmp/model_maker/object_detector/mobilenetv2_i256
Model: "retina_net_model"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 mobile_net (MobileNet)      {'2': (None, 64, 64, 24   2257984   
                             ),                                  
                              '3': (None, 32, 32, 32             
                             ),                                  
                              '4': (None, 16, 16, 96             
                             ),                                  
                              '5': (None, 8, 8, 320)             
                             , '6': (None, 8, 8, 128             
                             0)}                                 
                                                                 
 fpn (FPN)                   {'5': (None, 8, 8, 128)   149056    
                             , '4': (None, 16, 16, 1             
                             28),                                
                              '3': (None, 32, 32, 12             
                             8),                                 
                              '6': (None, 4, 4, 128)             
                             , '7': (None, 2, 2, 128             
                             )}                                  
                                                                 
 multilevel_detection_gener  multiple                  0 (unused)
 ator (MultilevelDetectionG                                      
 enerator)                                                       
                                                                 
 retina_net_head (RetinaNet  ({'3': (None, 32, 32, 3   173384    
 Head)                       6),                                 
                              '4': (None, 16, 16, 36             
                             ),                                  
                              '5': (None, 8, 8, 36),             
                              '6': (None, 4, 4, 36),             
                              '7': (None, 2, 2, 36)}             
                             , {'3': (None, 32, 32,              
                             36),                                
                              '4': (None, 16, 16, 36             
                             ),                                  
                              '5': (None, 8, 8, 36),             
                              '6': (None, 4, 4, 36),             
                              '7': (None, 2, 2, 36)}             
                             , {})                               
                                                                 
=================================================================
Total params: 2580424 (9.84 MB)
Trainable params: 2534792 (9.67 MB)
Non-trainable params: 45632 (178.25 KB)
_________________________________________________________________
Epoch 1/2
/mnt/sda1/code/si/ProyectoRedesNeuronales/.venv/lib/python3.9/site-packages/keras/src/backend.py:452: UserWarning: `tf.keras.backend.set_learning_phase` is deprecated and will be removed after 2020-10-11. To update it, simply pass a True/False value to the `training` argument of the `__call__` method of your layer or model.
  warnings.warn(
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
26/26 [==============================] - 52s 1s/step - total_loss: 4.8857 - cls_loss: 4.3851 - box_loss: 0.0089 - model_loss: 4.8307 - val_total_loss: 1.2979 - val_cls_loss: 0.9936 - val_box_loss: 0.0050 - val_model_loss: 1.2429
Epoch 2/2
26/26 [==============================] - 26s 998ms/step - total_loss: 1.1356 - cls_loss: 0.7939 - box_loss: 0.0057 - model_loss: 1.0805 - val_total_loss: 0.9252 - val_cls_loss: 0.6507 - val_box_loss: 0.0044 - val_model_loss: 0.8701

Evaluando modelo float...
20/20 [==============================] - 1s 26ms/step - total_loss: 0.8921 - cls_loss: 0.6115 - box_loss: 0.0045 - model_loss: 0.8370
creating index...
index created!
creating index...
index created!
Running per image evaluation...
Evaluate annotation type *bbox*
DONE (t=0.12s).
Accumulating evaluation results...
DONE (t=0.02s).
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.114
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.241
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.082
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.164
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.117
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.564
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.067
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.251
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.266
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.233
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.272
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.750
Float model - Loss:  [0.8920913934707642, 0.6114992499351501, 0.004510826431214809, 0.8370406031608582]
Métricas: {'AP': 0.11418389, 'AP50': 0.24143371, 'AP75': 0.08207641, 'APs': 0.16393676, 'APm': 0.11713386, 'APl': 0.56436694, 'ARmax1': 0.06703704, 'ARmax10': 0.25111112, 'ARmax100': 0.2659259, 'ARs': 0.23333333, 'ARm': 0.27185184, 'ARl': 0.75}
  AP: 0.11418388783931732
  AP50: 0.24143370985984802
  AP75: 0.08207640796899796
  APs: 0.1639367640018463
  APm: 0.11713386327028275
  APl: 0.5643669366836548
  ARmax1: 0.06703703850507736
  ARmax10: 0.25111111998558044
  ARmax100: 0.26592591404914856
  ARs: 0.23333333432674408
  ARm: 0.2718518376350403
  ARl: 0.75
Exporting a floating point model



=== PASO 2: Quantization Aware Training ===
Restaurando checkpoint float...
/mnt/sda1/code/si/ProyectoRedesNeuronales/.venv/lib/python3.9/site-packages/keras/src/engine/functional.py:642: UserWarning: Input dict contained keys ['6'] which did not match any model input. They will be ignored by the model.
  inputs = self._flatten_to_reference_inputs(inputs)
Using existing files at /tmp/model_maker/object_detector/mobilenetv2_i256
Model: "retina_net_model_2"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 mobile_net_1 (MobileNet)    {'2': (None, 64, 64, 24   2257984   
                             ),                                  
                              '3': (None, 32, 32, 32             
                             ),                                  
                              '4': (None, 16, 16, 96             
                             ),                                  
                              '5': (None, 8, 8, 320)             
                             , '6': (None, 8, 8, 128             
                             0)}                                 
                                                                 
 fpn_1 (FPN)                 {'5': (None, 8, 8, 128)   149056    
                             , '4': (None, 16, 16, 1             
                             28),                                
                              '3': (None, 32, 32, 12             
                             8),                                 
                              '6': (None, 4, 4, 128)             
                             , '7': (None, 2, 2, 128             
                             )}                                  
                                                                 
 multilevel_detection_gener  multiple                  0 (unused)
 ator_2 (MultilevelDetectio                                      
 nGenerator)                                                     
                                                                 
 retina_net_head_1 (RetinaN  ({'3': (None, 32, 32, 3   173384    
 etHead)                     6),                                 
                              '4': (None, 16, 16, 36             
                             ),                                  
                              '5': (None, 8, 8, 36),             
                              '6': (None, 4, 4, 36),             
                              '7': (None, 2, 2, 36)}             
                             , {'3': (None, 32, 32,              
                             36),                                
                              '4': (None, 16, 16, 36             
                             ),                                  
                              '5': (None, 8, 8, 36),             
                              '6': (None, 4, 4, 36),             
                              '7': (None, 2, 2, 36)}             
                             , {})                               
                                                                 
=================================================================
Total params: 2580424 (9.84 MB)
Trainable params: 2534792 (9.67 MB)
Non-trainable params: 45632 (178.25 KB)
_________________________________________________________________
Iniciando QAT...
WARNING:tensorflow:`tf.keras.layers.experimental.SyncBatchNormalization` endpoint is deprecated and will be removed in a future release. Please use `tf.keras.layers.BatchNormalization` with parameter `synchronized` set to True.
WARNING:tensorflow:`tf.keras.layers.experimental.SyncBatchNormalization` endpoint is deprecated and will be removed in a future release. Please use `tf.keras.layers.BatchNormalization` with parameter `synchronized` set to True.
Epoch 1/2
/mnt/sda1/code/si/ProyectoRedesNeuronales/.venv/lib/python3.9/site-packages/keras/src/backend.py:452: UserWarning: `tf.keras.backend.set_learning_phase` is deprecated and will be removed after 2020-10-11. To update it, simply pass a True/False value to the `training` argument of the `__call__` method of your layer or model.
  warnings.warn(
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
52/52 [==============================] - 74s 751ms/step - total_loss: 1.7756 - cls_loss: 0.9713 - box_loss: 0.0161 - model_loss: 1.7756 - val_total_loss: 1.9424 - val_cls_loss: 1.2872 - val_box_loss: 0.0131 - val_model_loss: 1.9424
Epoch 2/2
52/52 [==============================] - 35s 654ms/step - total_loss: 1.1542 - cls_loss: 0.7243 - box_loss: 0.0086 - model_loss: 1.1542 - val_total_loss: 1.6920 - val_cls_loss: 1.1583 - val_box_loss: 0.0107 - val_model_loss: 1.6920

Evaluando modelo cuantizado...
20/20 [==============================] - 1s 39ms/step - total_loss: 1.6436 - cls_loss: 1.1032 - box_loss: 0.0108 - model_loss: 1.6436
creating index...
index created!
creating index...
index created!
Running per image evaluation...
Evaluate annotation type *bbox*
DONE (t=0.07s).
Accumulating evaluation results...
DONE (t=0.02s).
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.006
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.021
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.008
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.013
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.019
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.019
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.020
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.000
QAT model - Loss:  [1.643592119216919, 1.1032391786575317, 0.010807055979967117, 1.643592119216919]
Métricas: {'AP': 0.005997078, 'AP50': 0.02057684, 'AP75': 0.0, 'APs': 0.0, 'APm': 0.0080088, 'APl': 0.0, 'ARmax1': 0.0129629625, 'ARmax10': 0.018888889, 'ARmax100': 0.018888889, 'ARs': 0.0, 'ARm': 0.02, 'ARl': 0.0}

--------------------------------------------------
--------------------------------------------------

Usamos:
EPOCHS = 3
LEARNING_RATE = 0.15
BATCH_SIZE = 4
DECAY_STEPS = 8
DECAY_RATE = 0.96



2025-11-24 13:36:08.270236: E tensorflow/compiler/xla/stream_executor/cuda/cuda_dnn.cc:9342] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
2025-11-24 13:36:08.270580: E tensorflow/compiler/xla/stream_executor/cuda/cuda_fft.cc:609] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
2025-11-24 13:36:08.270635: E tensorflow/compiler/xla/stream_executor/cuda/cuda_blas.cc:1518] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
2025-11-24 13:36:08.292442: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
/mnt/sda1/code/si/ProyectoRedesNeuronales/.venv/lib/python3.9/site-packages/tensorflow_hub/__init__.py:61: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import parse_version
/mnt/sda1/code/si/ProyectoRedesNeuronales/.venv/lib/python3.9/site-packages/tensorflow_addons/utils/tfa_eol_msg.py:23: UserWarning: 

TensorFlow Addons (TFA) has ended development and introduction of new features.
TFA has entered a minimal maintenance and release mode until a planned end of life in May 2024.
Please modify downstream libraries to take dependencies from other repositories in our TensorFlow community (e.g. Keras, Keras-CV, and Keras-NLP). 

For more information see: https://github.com/tensorflow/addons/issues/2807 

  warnings.warn(
Creando estructura de cache...
Cargando dataset...
Train dataset cargado
Val dataset cargado
Clases: ['background', 'head', 'helmet', 'person']

=== PASO 1: Entrenando modelo FLOAT ===
/mnt/sda1/code/si/ProyectoRedesNeuronales/.venv/lib/python3.9/site-packages/keras/src/engine/functional.py:642: UserWarning: Input dict contained keys ['6'] which did not match any model input. They will be ignored by the model.
  inputs = self._flatten_to_reference_inputs(inputs)
WARNING:tensorflow:`tf.keras.layers.experimental.SyncBatchNormalization` endpoint is deprecated and will be removed in a future release. Please use `tf.keras.layers.BatchNormalization` with parameter `synchronized` set to True.
WARNING:tensorflow:`tf.keras.layers.experimental.SyncBatchNormalization` endpoint is deprecated and will be removed in a future release. Please use `tf.keras.layers.BatchNormalization` with parameter `synchronized` set to True.
Using existing files at /tmp/model_maker/object_detector/mobilenetv2_i256
Model: "retina_net_model"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 mobile_net (MobileNet)      {'2': (None, 64, 64, 24   2257984   
                             ),                                  
                              '3': (None, 32, 32, 32             
                             ),                                  
                              '4': (None, 16, 16, 96             
                             ),                                  
                              '5': (None, 8, 8, 320)             
                             , '6': (None, 8, 8, 128             
                             0)}                                 
                                                                 
 fpn (FPN)                   {'5': (None, 8, 8, 128)   149056    
                             , '4': (None, 16, 16, 1             
                             28),                                
                              '3': (None, 32, 32, 12             
                             8),                                 
                              '6': (None, 4, 4, 128)             
                             , '7': (None, 2, 2, 128             
                             )}                                  
                                                                 
 multilevel_detection_gener  multiple                  0 (unused)
 ator (MultilevelDetectionG                                      
 enerator)                                                       
                                                                 
 retina_net_head (RetinaNet  ({'3': (None, 32, 32, 3   173384    
 Head)                       6),                                 
                              '4': (None, 16, 16, 36             
                             ),                                  
                              '5': (None, 8, 8, 36),             
                              '6': (None, 4, 4, 36),             
                              '7': (None, 2, 2, 36)}             
                             , {'3': (None, 32, 32,              
                             36),                                
                              '4': (None, 16, 16, 36             
                             ),                                  
                              '5': (None, 8, 8, 36),             
                              '6': (None, 4, 4, 36),             
                              '7': (None, 2, 2, 36)}             
                             , {})                               
                                                                 
=================================================================
Total params: 2580424 (9.84 MB)
Trainable params: 2534792 (9.67 MB)
Non-trainable params: 45632 (178.25 KB)
_________________________________________________________________
Epoch 1/3
/mnt/sda1/code/si/ProyectoRedesNeuronales/.venv/lib/python3.9/site-packages/keras/src/backend.py:452: UserWarning: `tf.keras.backend.set_learning_phase` is deprecated and will be removed after 2020-10-11. To update it, simply pass a True/False value to the `training` argument of the `__call__` method of your layer or model.
  warnings.warn(
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
26/26 [==============================] - 49s 1s/step - total_loss: 3.1289 - cls_loss: 2.6382 - box_loss: 0.0087 - model_loss: 3.0740 - val_total_loss: 1.2647 - val_cls_loss: 0.9588 - val_box_loss: 0.0050 - val_model_loss: 1.2097
Epoch 2/3
26/26 [==============================] - 28s 1s/step - total_loss: 1.0792 - cls_loss: 0.7612 - box_loss: 0.0053 - model_loss: 1.0242 - val_total_loss: 0.8936 - val_cls_loss: 0.6370 - val_box_loss: 0.0040 - val_model_loss: 0.8386
Epoch 3/3
26/26 [==============================] - 28s 1s/step - total_loss: 0.8519 - cls_loss: 0.5633 - box_loss: 0.0047 - model_loss: 0.7969 - val_total_loss: 0.7611 - val_cls_loss: 0.5209 - val_box_loss: 0.0037 - val_model_loss: 0.7061

Evaluando modelo float...
20/20 [==============================] - 1s 25ms/step - total_loss: 0.8085 - cls_loss: 0.5511 - box_loss: 0.0040 - model_loss: 0.7535
creating index...
index created!
creating index...
index created!
Running per image evaluation...
Evaluate annotation type *bbox*
DONE (t=0.09s).
Accumulating evaluation results...
DONE (t=0.02s).
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.183
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.368
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.164
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.034
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.192
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.758
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.100
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.364
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.376
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.133
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.391
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.800
Float model - Loss:  [0.8084559440612793, 0.5510729551315308, 0.004047914408147335, 0.7534686923027039]
Métricas: {'AP': 0.18338753, 'AP50': 0.36763582, 'AP75': 0.16354862, 'APs': 0.03368323, 'APm': 0.19243035, 'APl': 0.7584253, 'ARmax1': 0.1, 'ARmax10': 0.36407408, 'ARmax100': 0.37592593, 'ARs': 0.13333334, 'ARm': 0.39074075, 'ARl': 0.8}
  AP: 0.18338753283023834
  AP50: 0.3676358163356781
  AP75: 0.16354861855506897
  APs: 0.033683229237794876
  APm: 0.19243034720420837
  APl: 0.7584252953529358
  ARmax1: 0.10000000149011612
  ARmax10: 0.36407408118247986
  ARmax100: 0.3759259283542633
  ARs: 0.13333334028720856
  ARm: 0.3907407522201538
  ARl: 0.800000011920929
Exporting a floating point model



=== PASO 2: Quantization Aware Training ===
Restaurando checkpoint float...
/mnt/sda1/code/si/ProyectoRedesNeuronales/.venv/lib/python3.9/site-packages/keras/src/engine/functional.py:642: UserWarning: Input dict contained keys ['6'] which did not match any model input. They will be ignored by the model.
  inputs = self._flatten_to_reference_inputs(inputs)
Using existing files at /tmp/model_maker/object_detector/mobilenetv2_i256
Model: "retina_net_model_2"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 mobile_net_1 (MobileNet)    {'2': (None, 64, 64, 24   2257984   
                             ),                                  
                              '3': (None, 32, 32, 32             
                             ),                                  
                              '4': (None, 16, 16, 96             
                             ),                                  
                              '5': (None, 8, 8, 320)             
                             , '6': (None, 8, 8, 128             
                             0)}                                 
                                                                 
 fpn_1 (FPN)                 {'5': (None, 8, 8, 128)   149056    
                             , '4': (None, 16, 16, 1             
                             28),                                
                              '3': (None, 32, 32, 12             
                             8),                                 
                              '6': (None, 4, 4, 128)             
                             , '7': (None, 2, 2, 128             
                             )}                                  
                                                                 
 multilevel_detection_gener  multiple                  0 (unused)
 ator_2 (MultilevelDetectio                                      
 nGenerator)                                                     
                                                                 
 retina_net_head_1 (RetinaN  ({'3': (None, 32, 32, 3   173384    
 etHead)                     6),                                 
                              '4': (None, 16, 16, 36             
                             ),                                  
                              '5': (None, 8, 8, 36),             
                              '6': (None, 4, 4, 36),             
                              '7': (None, 2, 2, 36)}             
                             , {'3': (None, 32, 32,              
                             36),                                
                              '4': (None, 16, 16, 36             
                             ),                                  
                              '5': (None, 8, 8, 36),             
                              '6': (None, 4, 4, 36),             
                              '7': (None, 2, 2, 36)}             
                             , {})                               
                                                                 
=================================================================
Total params: 2580424 (9.84 MB)
Trainable params: 2534792 (9.67 MB)
Non-trainable params: 45632 (178.25 KB)
_________________________________________________________________
Iniciando QAT...
WARNING:tensorflow:`tf.keras.layers.experimental.SyncBatchNormalization` endpoint is deprecated and will be removed in a future release. Please use `tf.keras.layers.BatchNormalization` with parameter `synchronized` set to True.
WARNING:tensorflow:`tf.keras.layers.experimental.SyncBatchNormalization` endpoint is deprecated and will be removed in a future release. Please use `tf.keras.layers.BatchNormalization` with parameter `synchronized` set to True.
Epoch 1/3
/mnt/sda1/code/si/ProyectoRedesNeuronales/.venv/lib/python3.9/site-packages/keras/src/backend.py:452: UserWarning: `tf.keras.backend.set_learning_phase` is deprecated and will be removed after 2020-10-11. To update it, simply pass a True/False value to the `training` argument of the `__call__` method of your layer or model.
  warnings.warn(
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
52/52 [==============================] - 83s 871ms/step - total_loss: 1.6346 - cls_loss: 0.8168 - box_loss: 0.0164 - model_loss: 1.6346 - val_total_loss: 1.7312 - val_cls_loss: 1.1115 - val_box_loss: 0.0124 - val_model_loss: 1.7312
Epoch 2/3
52/52 [==============================] - 40s 692ms/step - total_loss: 1.0843 - cls_loss: 0.6476 - box_loss: 0.0087 - model_loss: 1.0843 - val_total_loss: 1.5567 - val_cls_loss: 1.0416 - val_box_loss: 0.0103 - val_model_loss: 1.5567
Epoch 3/3
52/52 [==============================] - 37s 707ms/step - total_loss: 0.9597 - cls_loss: 0.5908 - box_loss: 0.0074 - model_loss: 0.9597 - val_total_loss: 1.4058 - val_cls_loss: 0.9614 - val_box_loss: 0.0089 - val_model_loss: 1.4058

Evaluando modelo cuantizado...
20/20 [==============================] - 1s 41ms/step - total_loss: 1.3795 - cls_loss: 0.9329 - box_loss: 0.0089 - model_loss: 1.3795
creating index...
index created!
creating index...
index created!
Running per image evaluation...
Evaluate annotation type *bbox*
DONE (t=0.11s).
Accumulating evaluation results...
DONE (t=0.20s).
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.022
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.068
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.008
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.031
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.017
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.014
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.029
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.029
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.042
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.017
QAT model - Loss:  [1.3795297145843506, 0.9328759908676147, 0.008933073841035366, 1.3795297145843506]
Métricas: {'AP': 0.021526774, 'AP50': 0.06806162, 'AP75': 0.008250825, 'APs': 0.0, 'APm': 0.031231662, 'APl': 0.016831683, 'ARmax1': 0.014074074, 'ARmax10': 0.028888889, 'ARmax100': 0.028888889, 'ARs': 0.0, 'ARm': 0.04222222, 'ARl': 0.016666668}


----------------------------------------------
-------------------------------------------------


Usamos:
EPOCHS = 3
LEARNING_RATE = 0.15
BATCH_SIZE = 4
DECAY_STEPS = 8
DECAY_RATE = 0.96


=== PASO 1: Entrenando modelo FLOAT ===
/mnt/sda1/code/si/ProyectoRedesNeuronales/.venv/lib/python3.9/site-packages/keras/src/engine/functional.py:642: UserWarning: Input dict contained keys ['6'] which did not match any model input. They will be ignored by the model.
  inputs = self._flatten_to_reference_inputs(inputs)
WARNING:tensorflow:`tf.keras.layers.experimental.SyncBatchNormalization` endpoint is deprecated and will be removed in a future release. Please use `tf.keras.layers.BatchNormalization` with parameter `synchronized` set to True.
WARNING:tensorflow:`tf.keras.layers.experimental.SyncBatchNormalization` endpoint is deprecated and will be removed in a future release. Please use `tf.keras.layers.BatchNormalization` with parameter `synchronized` set to True.
Using existing files at /tmp/model_maker/object_detector/mobilenetv2_i256
Model: "retina_net_model"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 mobile_net (MobileNet)      {'2': (None, 64, 64, 24   2257984   
                             ),                                  
                              '3': (None, 32, 32, 32             
                             ),                                  
                              '4': (None, 16, 16, 96             
                             ),                                  
                              '5': (None, 8, 8, 320)             
                             , '6': (None, 8, 8, 128             
                             0)}                                 
                                                                 
 fpn (FPN)                   {'5': (None, 8, 8, 128)   149056    
                             , '4': (None, 16, 16, 1             
                             28),                                
                              '3': (None, 32, 32, 12             
                             8),                                 
                              '6': (None, 4, 4, 128)             
                             , '7': (None, 2, 2, 128             
                             )}                                  
                                                                 
 multilevel_detection_gener  multiple                  0 (unused)
 ator (MultilevelDetectionG                                      
 enerator)                                                       
                                                                 
 retina_net_head (RetinaNet  ({'3': (None, 32, 32, 3   173384    
 Head)                       6),                                 
                              '4': (None, 16, 16, 36             
                             ),                                  
                              '5': (None, 8, 8, 36),             
                              '6': (None, 4, 4, 36),             
                              '7': (None, 2, 2, 36)}             
                             , {'3': (None, 32, 32,              
                             36),                                
                              '4': (None, 16, 16, 36             
                             ),                                  
                              '5': (None, 8, 8, 36),             
                              '6': (None, 4, 4, 36),             
                              '7': (None, 2, 2, 36)}             
                             , {})                               
                                                                 
=================================================================
Total params: 2580424 (9.84 MB)
Trainable params: 2534792 (9.67 MB)
Non-trainable params: 45632 (178.25 KB)
_________________________________________________________________
Epoch 1/15
/mnt/sda1/code/si/ProyectoRedesNeuronales/.venv/lib/python3.9/site-packages/keras/src/backend.py:452: UserWarning: `tf.keras.backend.set_learning_phase` is deprecated and will be removed after 2020-10-11. To update it, simply pass a True/False value to the `training` argument of the `__call__` method of your layer or model.
  warnings.warn(
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_1/batch_normalization/gamma:0', 'conv2dbn_block_1/batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
2025-11-24 18:14:32.248569: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 50331648 exceeds 10% of free system memory.
2025-11-24 18:14:34.282930: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 50331648 exceeds 10% of free system memory.
2025-11-24 18:14:34.285484: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 50331648 exceeds 10% of free system memory.
2025-11-24 18:14:34.979280: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 50331648 exceeds 10% of free system memory.
2025-11-24 18:14:42.576268: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 50331648 exceeds 10% of free system memory.
26/26 [==============================] - 69s 1s/step - total_loss: 4.2605 - cls_loss: 3.7147 - box_loss: 0.0098 - model_loss: 4.2055 - val_total_loss: 1.4395 - val_cls_loss: 1.0882 - val_box_loss: 0.0059 - val_model_loss: 1.3845
Epoch 2/15
26/26 [==============================] - 29s 1s/step - total_loss: 1.3365 - cls_loss: 0.9476 - box_loss: 0.0067 - model_loss: 1.2815 - val_total_loss: 1.0548 - val_cls_loss: 0.7710 - val_box_loss: 0.0046 - val_model_loss: 0.9998
Epoch 3/15
26/26 [==============================] - 51s 2s/step - total_loss: 0.9797 - cls_loss: 0.6600 - box_loss: 0.0053 - model_loss: 0.9247 - val_total_loss: 0.8952 - val_cls_loss: 0.6438 - val_box_loss: 0.0039 - val_model_loss: 0.8402
Epoch 4/15
26/26 [==============================] - 32s 1s/step - total_loss: 0.7877 - cls_loss: 0.5192 - box_loss: 0.0043 - model_loss: 0.7327 - val_total_loss: 0.7576 - val_cls_loss: 0.5253 - val_box_loss: 0.0035 - val_model_loss: 0.7026
Epoch 5/15
26/26 [==============================] - 28s 1s/step - total_loss: 0.7049 - cls_loss: 0.4563 - box_loss: 0.0039 - model_loss: 0.6499 - val_total_loss: 0.7097 - val_cls_loss: 0.4613 - val_box_loss: 0.0039 - val_model_loss: 0.6548
Epoch 6/15
26/26 [==============================] - 35s 1s/step - total_loss: 0.6295 - cls_loss: 0.3957 - box_loss: 0.0036 - model_loss: 0.5745 - val_total_loss: 0.7216 - val_cls_loss: 0.4524 - val_box_loss: 0.0043 - val_model_loss: 0.6666
Epoch 7/15
26/26 [==============================] - 27s 1s/step - total_loss: 0.5784 - cls_loss: 0.3665 - box_loss: 0.0031 - model_loss: 0.5235 - val_total_loss: 0.6694 - val_cls_loss: 0.4053 - val_box_loss: 0.0042 - val_model_loss: 0.6145
Epoch 8/15
26/26 [==============================] - 27s 1s/step - total_loss: 0.5470 - cls_loss: 0.3438 - box_loss: 0.0030 - model_loss: 0.4921 - val_total_loss: 0.6519 - val_cls_loss: 0.3762 - val_box_loss: 0.0044 - val_model_loss: 0.5969
Epoch 9/15
26/26 [==============================] - 26s 994ms/step - total_loss: 0.5419 - cls_loss: 0.3379 - box_loss: 0.0030 - model_loss: 0.4869 - val_total_loss: 0.6381 - val_cls_loss: 0.3609 - val_box_loss: 0.0044 - val_model_loss: 0.5831
Epoch 10/15
26/26 [==============================] - 27s 1s/step - total_loss: 0.4930 - cls_loss: 0.3053 - box_loss: 0.0027 - model_loss: 0.4380 - val_total_loss: 0.6079 - val_cls_loss: 0.3435 - val_box_loss: 0.0042 - val_model_loss: 0.5529
Epoch 11/15
26/26 [==============================] - 30s 1s/step - total_loss: 0.4712 - cls_loss: 0.2915 - box_loss: 0.0025 - model_loss: 0.4162 - val_total_loss: 0.6114 - val_cls_loss: 0.3415 - val_box_loss: 0.0043 - val_model_loss: 0.5564
Epoch 12/15
26/26 [==============================] - 26s 1s/step - total_loss: 0.4643 - cls_loss: 0.2837 - box_loss: 0.0025 - model_loss: 0.4093 - val_total_loss: 0.6096 - val_cls_loss: 0.3375 - val_box_loss: 0.0043 - val_model_loss: 0.5546
Epoch 13/15
26/26 [==============================] - 26s 992ms/step - total_loss: 0.4463 - cls_loss: 0.2670 - box_loss: 0.0025 - model_loss: 0.3913 - val_total_loss: 0.5697 - val_cls_loss: 0.3119 - val_box_loss: 0.0041 - val_model_loss: 0.5147
Epoch 14/15
26/26 [==============================] - 32s 1s/step - total_loss: 0.4677 - cls_loss: 0.2754 - box_loss: 0.0027 - model_loss: 0.4127 - val_total_loss: 0.6029 - val_cls_loss: 0.3521 - val_box_loss: 0.0039 - val_model_loss: 0.5479
Epoch 15/15
26/26 [==============================] - 27s 1s/step - total_loss: 0.4399 - cls_loss: 0.2632 - box_loss: 0.0024 - model_loss: 0.3849 - val_total_loss: 0.5748 - val_cls_loss: 0.3259 - val_box_loss: 0.0039 - val_model_loss: 0.5198

Evaluando modelo float...
20/20 [==============================] - 3s 76ms/step - total_loss: 0.5650 - cls_loss: 0.3155 - box_loss: 0.0039 - model_loss: 0.5100
creating index...
index created!
creating index...
index created!
Running per image evaluation...
Evaluate annotation type *bbox*
DONE (t=0.09s).
Accumulating evaluation results...
DONE (t=0.06s).
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.270
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.556
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.272
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.239
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.285
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.725
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.199
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.500
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.526
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.256
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.535
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.767
Float model - Loss:  [0.5650215744972229, 0.3155274987220764, 0.00389036163687706, 0.51004558801651]
Métricas: {'AP': 0.27023366, 'AP50': 0.55564123, 'AP75': 0.2715503, 'APs': 0.23919141, 'APm': 0.2850917, 'APl': 0.72541255, 'ARmax1': 0.19851851, 'ARmax10': 0.49962962, 'ARmax100': 0.52555555, 'ARs': 0.25555557, 'ARm': 0.53481483, 'ARl': 0.76666665}
  AP: 0.2702336609363556
  AP50: 0.555641233921051
  AP75: 0.2715502977371216
  APs: 0.23919141292572021
  APm: 0.28509169816970825
  APl: 0.7254125475883484
  ARmax1: 0.1985185146331787
  ARmax10: 0.4996296167373657
  ARmax100: 0.5255555510520935
  ARs: 0.25555557012557983
  ARm: 0.5348148345947266
  ARl: 0.7666666507720947




=== PASO 2: Quantization Aware Training ===
Restaurando checkpoint float...
/mnt/sda1/code/si/ProyectoRedesNeuronales/.venv/lib/python3.9/site-packages/keras/src/engine/functional.py:642: UserWarning: Input dict contained keys ['6'] which did not match any model input. They will be ignored by the model.
  inputs = self._flatten_to_reference_inputs(inputs)
Using existing files at /tmp/model_maker/object_detector/mobilenetv2_i256
Model: "retina_net_model_2"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 mobile_net_1 (MobileNet)    {'2': (None, 64, 64, 24   2257984   
                             ),                                  
                              '3': (None, 32, 32, 32             
                             ),                                  
                              '4': (None, 16, 16, 96             
                             ),                                  
                              '5': (None, 8, 8, 320)             
                             , '6': (None, 8, 8, 128             
                             0)}                                 
                                                                 
 fpn_1 (FPN)                 {'5': (None, 8, 8, 128)   149056    
                             , '4': (None, 16, 16, 1             
                             28),                                
                              '3': (None, 32, 32, 12             
                             8),                                 
                              '6': (None, 4, 4, 128)             
                             , '7': (None, 2, 2, 128             
                             )}                                  
                                                                 
 multilevel_detection_gener  multiple                  0 (unused)
 ator_2 (MultilevelDetectio                                      
 nGenerator)                                                     
                                                                 
 retina_net_head_1 (RetinaN  ({'3': (None, 32, 32, 3   173384    
 etHead)                     6),                                 
                              '4': (None, 16, 16, 36             
                             ),                                  
                              '5': (None, 8, 8, 36),             
                              '6': (None, 4, 4, 36),             
                              '7': (None, 2, 2, 36)}             
                             , {'3': (None, 32, 32,              
                             36),                                
                              '4': (None, 16, 16, 36             
                             ),                                  
                              '5': (None, 8, 8, 36),             
                              '6': (None, 4, 4, 36),             
                              '7': (None, 2, 2, 36)}             
                             , {})                               
                                                                 
=================================================================
Total params: 2580424 (9.84 MB)
Trainable params: 2534792 (9.67 MB)
Non-trainable params: 45632 (178.25 KB)
_________________________________________________________________
Iniciando QAT...
WARNING:tensorflow:`tf.keras.layers.experimental.SyncBatchNormalization` endpoint is deprecated and will be removed in a future release. Please use `tf.keras.layers.BatchNormalization` with parameter `synchronized` set to True.
WARNING:tensorflow:`tf.keras.layers.experimental.SyncBatchNormalization` endpoint is deprecated and will be removed in a future release. Please use `tf.keras.layers.BatchNormalization` with parameter `synchronized` set to True.
Epoch 1/15
/mnt/sda1/code/si/ProyectoRedesNeuronales/.venv/lib/python3.9/site-packages/keras/src/backend.py:452: UserWarning: `tf.keras.backend.set_learning_phase` is deprecated and will be removed after 2020-10-11. To update it, simply pass a True/False value to the `training` argument of the `__call__` method of your layer or model.
  warnings.warn(
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
WARNING:tensorflow:Gradients do not exist for variables ['conv2dbn_block_5/quant_conv2d/kernel:0', 'conv2dbn_block_5/quant_sync_batch_normalization/gamma:0', 'conv2dbn_block_5/quant_sync_batch_normalization/beta:0'] when minimizing the loss. If you're using `model.compile()`, did you forget to provide a `loss` argument?
52/52 [==============================] - 104s 855ms/step - total_loss: 1.5296 - cls_loss: 0.7655 - box_loss: 0.0153 - model_loss: 1.5296 - val_total_loss: 2.0611 - val_cls_loss: 1.3814 - val_box_loss: 0.0136 - val_model_loss: 2.0611
Epoch 2/15
52/52 [==============================] - 35s 593ms/step - total_loss: 0.9572 - cls_loss: 0.5540 - box_loss: 0.0081 - model_loss: 0.9572 - val_total_loss: 1.7071 - val_cls_loss: 1.1646 - val_box_loss: 0.0109 - val_model_loss: 1.7071
Epoch 3/15
52/52 [==============================] - 43s 775ms/step - total_loss: 0.8011 - cls_loss: 0.4834 - box_loss: 0.0064 - model_loss: 0.8011 - val_total_loss: 1.4589 - val_cls_loss: 1.0328 - val_box_loss: 0.0085 - val_model_loss: 1.4589
Epoch 4/15
52/52 [==============================] - 48s 922ms/step - total_loss: 0.7364 - cls_loss: 0.4457 - box_loss: 0.0058 - model_loss: 0.7364 - val_total_loss: 1.2617 - val_cls_loss: 0.8956 - val_box_loss: 0.0073 - val_model_loss: 1.2617
Epoch 5/15
52/52 [==============================] - 41s 784ms/step - total_loss: 0.7077 - cls_loss: 0.4361 - box_loss: 0.0054 - model_loss: 0.7077 - val_total_loss: 1.0859 - val_cls_loss: 0.7473 - val_box_loss: 0.0068 - val_model_loss: 1.0859
Epoch 6/15
52/52 [==============================] - 50s 968ms/step - total_loss: 0.7218 - cls_loss: 0.4504 - box_loss: 0.0054 - model_loss: 0.7218 - val_total_loss: 0.9351 - val_cls_loss: 0.6128 - val_box_loss: 0.0064 - val_model_loss: 0.9351
Epoch 7/15
52/52 [==============================] - 36s 698ms/step - total_loss: 0.6767 - cls_loss: 0.4146 - box_loss: 0.0052 - model_loss: 0.6767 - val_total_loss: 0.8139 - val_cls_loss: 0.5110 - val_box_loss: 0.0061 - val_model_loss: 0.8139
Epoch 8/15
52/52 [==============================] - 40s 765ms/step - total_loss: 0.6641 - cls_loss: 0.4064 - box_loss: 0.0052 - model_loss: 0.6641 - val_total_loss: 0.7360 - val_cls_loss: 0.4381 - val_box_loss: 0.0060 - val_model_loss: 0.7360
Epoch 9/15
52/52 [==============================] - 42s 818ms/step - total_loss: 0.6665 - cls_loss: 0.4135 - box_loss: 0.0051 - model_loss: 0.6665 - val_total_loss: 0.6888 - val_cls_loss: 0.4059 - val_box_loss: 0.0057 - val_model_loss: 0.6888
Epoch 10/15
52/52 [==============================] - 44s 836ms/step - total_loss: 0.6340 - cls_loss: 0.3963 - box_loss: 0.0048 - model_loss: 0.6340 - val_total_loss: 0.6818 - val_cls_loss: 0.3939 - val_box_loss: 0.0058 - val_model_loss: 0.6818
Epoch 11/15
52/52 [==============================] - 46s 882ms/step - total_loss: 0.6451 - cls_loss: 0.4017 - box_loss: 0.0049 - model_loss: 0.6451 - val_total_loss: 0.6712 - val_cls_loss: 0.3864 - val_box_loss: 0.0057 - val_model_loss: 0.6712
Epoch 12/15
52/52 [==============================] - 40s 770ms/step - total_loss: 0.6626 - cls_loss: 0.4101 - box_loss: 0.0051 - model_loss: 0.6626 - val_total_loss: 0.6609 - val_cls_loss: 0.3839 - val_box_loss: 0.0055 - val_model_loss: 0.6609
Epoch 13/15
52/52 [==============================] - 38s 734ms/step - total_loss: 0.6383 - cls_loss: 0.3937 - box_loss: 0.0049 - model_loss: 0.6383 - val_total_loss: 0.6665 - val_cls_loss: 0.3848 - val_box_loss: 0.0056 - val_model_loss: 0.6665
Epoch 14/15
52/52 [==============================] - 34s 662ms/step - total_loss: 0.6414 - cls_loss: 0.4024 - box_loss: 0.0048 - model_loss: 0.6414 - val_total_loss: 0.6678 - val_cls_loss: 0.3889 - val_box_loss: 0.0056 - val_model_loss: 0.6678
Epoch 15/15
52/52 [==============================] - 36s 692ms/step - total_loss: 0.6443 - cls_loss: 0.3959 - box_loss: 0.0050 - model_loss: 0.6443 - val_total_loss: 0.6674 - val_cls_loss: 0.3897 - val_box_loss: 0.0056 - val_model_loss: 0.6674

Evaluando modelo cuantizado...
20/20 [==============================] - 2s 59ms/step - total_loss: 0.7040 - cls_loss: 0.4027 - box_loss: 0.0060 - model_loss: 0.7040
creating index...
index created!
creating index...
index created!
Running per image evaluation...
Evaluate annotation type *bbox*
DONE (t=0.14s).
Accumulating evaluation results...
DONE (t=0.17s).
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.163
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.407
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.135
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.078
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.168
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.686
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.085
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.254
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.270
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.078
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.283
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.733
QAT model - Loss:  [0.703951358795166, 0.4027152955532074, 0.0060247210785746574, 0.703951358795166]
Métricas: {'AP': 0.16294047, 'AP50': 0.40668327, 'AP75': 0.135322, 'APs': 0.07821782, 'APm': 0.16829619, 'APl': 0.686174, 'ARmax1': 0.08481482, 'ARmax10': 0.25407407, 'ARmax100': 0.26962963, 'ARs': 0.07777778, 'ARm': 0.28296295, 'ARl': 0.73333335}




---------------------------------------------
---------------------------------------------

