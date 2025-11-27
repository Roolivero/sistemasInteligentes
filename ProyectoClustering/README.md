package com.bluegin.tramites.servicio;

import com.bluegin.tramites.clientes.NomadeApiClient;
import com.bluegin.tramites.clientes.dto.*;
import com.bluegin.tramites.clientes.dto.anidado.CondicionNomadeDTO;
import com.bluegin.tramites.clientes.dto.anidado.DatoEtapaNomadeDTO;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import jakarta.enterprise.context.ApplicationScoped;
import jakarta.inject.Inject;
import org.eclipse.microprofile.rest.client.inject.RestClient;
import java.util.Collections;
import java.util.List;

import com.bluegin.tramites.dto.UsuarioIdentificadoDTO;
import com.bluegin.tramites.clientes.dto.anidado.EtapaNomadeDTO;
import com.bluegin.tramites.clientes.dto.anidado.TransicionNomadeDTO;
import com.bluegin.tramites.dto.LoginRequestDTO;
import com.bluegin.tramites.dto.SessionDTO;

import io.quarkus.logging.Log;
import jakarta.ws.rs.NotFoundException;
import java.util.Optional;
import java.util.ArrayList;
import java.util.Map;
import com.bluegin.tramites.dto.VariableConValorDTO;
import com.bluegin.tramites.dto.CargarArchivoRequestDTO;
import com.bluegin.tramites.dto.CargarArchivoResponseDTO;
import com.bluegin.tramites.clientes.dto.DatoInstanciaNomadeDTO;
import com.bluegin.tramites.clientes.dto.anidado.ValorDatoNomadeDTO;
import com.bluegin.tramites.clientes.dto.anidado.ArchivoValorNomadeDTO;
import com.bluegin.tramites.clientes.dto.anidado.DatoProcesoNomadeDTO;
import com.bluegin.tramites.dto.DescargarArchivoRequestDTO;
import com.bluegin.tramites.dto.DescargarArchivoResponseDTO;

import java.util.HashMap;

@ApplicationScoped
public class InstanciaService {

    @Inject
    @RestClient
    NomadeApiClient nomadeApiClient;

    @Inject
    ObjectMapper objectMapper;

    @Inject
    ProcesoService procesoService;

    @Inject 
    IdentificacionService identificacionService;

    private SessionDTO getAdminToken(){
        LoginRequestDTO usuarioContrasenia = new LoginRequestDTO();
        usuarioContrasenia.setUsername("admin");
        usuarioContrasenia.setPassword("admin");

        SessionDTO adminToken = identificacionService.login(usuarioContrasenia,true); 
        return adminToken;
    }

    public List<InstanciaNomadeDTO> getInstancias(String token) {
        try {
            Log.info("=== INICIO getInstancias ===");
            Log.info("Token recibido: " + (token != null ? token.substring(0, Math.min(10, token.length())) + "..." : "null"));
            
            Log.info("PASO 1: Obteniendo total de instancias...");
            NomadePedidoDTO pedidoTotal = new NomadePedidoDTO(token);
            pedidoTotal.setListado(new NomadePedidoListadoDTO(0, -1)); // -1 = solo obtener total
            pedidoTotal.setEstructuraCompleta(true);
            
            String pedidoTotalJson = objectMapper.writeValueAsString(pedidoTotal);
            Log.info("JSON para obtener total: " + pedidoTotalJson);
            
            NomadeRespuestaDTO<InstanciaNomadeDTO> respuestaTotal = nomadeApiClient.getInstancias(pedidoTotalJson);
            Log.info("Respuesta total recibida: " + (respuestaTotal != null ? "NO NULL" : "NULL"));
            
            if (respuestaTotal != null) {
                Log.info("Respuesta total procesado: " + respuestaTotal.isProcesado());
                Log.info("Respuesta total error: " + respuestaTotal.getError());
                Log.info("Respuesta total total: " + respuestaTotal.getTotal());
                Log.info("Respuesta total listado: " + (respuestaTotal.getListado() != null ? respuestaTotal.getListado().size() + " elementos" : "NULL"));
            }
            
            if (respuestaTotal == null || !respuestaTotal.isProcesado() || respuestaTotal.getTotal() == null) {
                Log.warn("No se pudo obtener el total de instancias");
                Log.warn("respuestaTotal == null: " + (respuestaTotal == null));
                Log.warn("!respuestaTotal.isProcesado(): " + (respuestaTotal != null && !respuestaTotal.isProcesado()));
                Log.warn("respuestaTotal.getTotal() == null: " + (respuestaTotal != null && respuestaTotal.getTotal() == null));
                return Collections.emptyList();
            }
            
            int total = respuestaTotal.getTotal();
            Log.info("Total de instancias encontradas: " + total);
            
            if (total == 0) {
                Log.info("No hay instancias para obtener");
                return Collections.emptyList();
            }
            
            Log.info("PASO 2: Obteniendo todas las instancias...");
            NomadePedidoDTO pedido = new NomadePedidoDTO(token);
            pedido.setListado(new NomadePedidoListadoDTO(0, total));
            pedido.setEstructuraCompleta(true);
            
            String pedidoJson = objectMapper.writeValueAsString(pedido);
            Log.info("JSON para obtener instancias: " + pedidoJson);
            
            NomadeRespuestaDTO<InstanciaNomadeDTO> respuesta = nomadeApiClient.getInstancias(pedidoJson);
            Log.info("Respuesta instancias recibida: " + (respuesta != null ? "NO NULL" : "NULL"));

            if (respuesta != null) {
                Log.info("Respuesta instancias procesado: " + respuesta.isProcesado());
                Log.info("Respuesta instancias error: " + respuesta.getError());
                Log.info("Respuesta instancias total: " + respuesta.getTotal());
                Log.info("Respuesta instancias listado: " + (respuesta.getListado() != null ? respuesta.getListado().size() + " elementos" : "NULL"));
            }

            if (respuesta != null && respuesta.isProcesado() && respuesta.getListado() != null) {
                Log.info("Instancias obtenidas exitosamente: " + respuesta.getListado().size());
                Log.info("=== FIN getInstancias (EXITOSO) ===");
                return respuesta.getListado();
            } else {
                Log.warn("No se pudieron obtener las instancias");
                Log.warn("respuesta == null: " + (respuesta == null));
                Log.warn("!respuesta.isProcesado(): " + (respuesta != null && !respuesta.isProcesado()));
                Log.warn("respuesta.getListado() == null: " + (respuesta != null && respuesta.getListado() == null));
                Log.info("=== FIN getInstancias (FALLIDO) ===");
                return Collections.emptyList();
            }
        } catch (JsonProcessingException e) {
            Log.error("Error creando JSON para Nomade API: " + e.getMessage());
            throw new RuntimeException("Error creating JSON for Nomade API", e);
        } catch (Exception e) {
            Log.error("Error inesperado en getInstancias: " + e.getMessage());
            e.printStackTrace();
            return Collections.emptyList();
        }
    }

    public InstanciaNomadeDTO getInstancia(String token, int id){
        try {
            Log.info("=== INICIO getInstancia ===");
            Log.info("Obteniendo instancia con ID: " + id);
            Log.info("Token recibido: " + (token != null ? token.substring(0, Math.min(10, token.length())) + "..." : "null"));
            
            NomadePedidoDTO pedido = new NomadePedidoDTO(token);
            pedido.setNumero(id); 
            pedido.setEstructuraCompleta(true);
            
            String pedidoJson = objectMapper.writeValueAsString(pedido);
            Log.info("JSON para obtener instancia específica: " + pedidoJson);
            
            NomadeRespuestaDTO<InstanciaNomadeDTO> respuesta = nomadeApiClient.getInstancias(pedidoJson);
            Log.info("Respuesta recibida: " + (respuesta != null ? "NO NULL" : "NULL"));
            
            if (respuesta != null) {
                Log.info("Respuesta procesado: " + respuesta.isProcesado());
                Log.info("Respuesta error: " + respuesta.getError());
                Log.info("Respuesta total: " + respuesta.getTotal());
                Log.info("Respuesta listado: " + (respuesta.getListado() != null ? respuesta.getListado().size() + " elementos" : "NULL"));
            }
            
            if (respuesta != null && respuesta.isProcesado() && respuesta.getListado() != null && !respuesta.getListado().isEmpty()) {
                Log.info("Instancia obtenida exitosamente: " + respuesta.getListado().get(0).getNumero());
                Log.info("=== FIN getInstancia (EXITOSO) ===");
                return respuesta.getListado().get(0);
            } else {
                Log.warn("No se pudo obtener la instancia con ID " + id);
                Log.warn("respuesta == null: " + (respuesta == null));
                Log.warn("!respuesta.isProcesado(): " + (respuesta != null && !respuesta.isProcesado()));
                Log.warn("respuesta.getListado() == null: " + (respuesta != null && respuesta.getListado() == null));
                Log.warn("respuesta.getListado().isEmpty(): " + (respuesta != null && respuesta.getListado() != null && respuesta.getListado().isEmpty()));
                Log.info("=== FIN getInstancia (FALLIDO) ===");
                return null;
            }
        } catch (JsonProcessingException e) {
            Log.error("Error creando JSON para Nomade API: " + e.getMessage());
            throw new RuntimeException("Error creating JSON for Nomade API", e);
        } catch (org.jboss.resteasy.reactive.ClientWebApplicationException e) {
            int statusCode = e.getResponse() != null ? e.getResponse().getStatus() : 500;
            String errorMessage = e.getMessage();

            Log.warnf("API de Nomade devolvió error %d para instancia ID %d: %s", statusCode, id, errorMessage);

            // Lanzar excepción específica según el código de estado
            if (statusCode == 401) {
                throw new com.bluegin.tramites.excepciones.NomadeUnauthorizedException(
                    "No autorizado para acceder a la instancia " + id + ": " + errorMessage, e);
            } else if (statusCode == 404) {
                throw new com.bluegin.tramites.excepciones.NomadeNotFoundException(
                    "Instancia " + id + " no encontrada: " + errorMessage, e);
            } else {
                throw new com.bluegin.tramites.excepciones.NomadeApiException(
                    "Error de API de Nomade al obtener instancia " + id + ": " + errorMessage, statusCode, e);
            }
        } catch (Exception e) {
            Log.error("Error inesperado en getInstancia: " + e.getMessage());
            e.printStackTrace();
            throw new RuntimeException("Error inesperado al obtener instancia: " + e.getMessage(), e);
        }
    }

    public InstanciaNomadeDTO crearInstancia(String token, Integer procesoId) {
        
        if (procesoId == null) {
            throw new IllegalArgumentException("ID de proceso no puede ser nulo");
        }

        try {
            Optional<UsuarioIdentificadoDTO> usuarioOpt = identificacionService.getUserIdFromSession(token);
            if (usuarioOpt.isEmpty()) {
                throw new RuntimeException("No se pudo identificar al usuario con el token proporcionado");
            }
            
            Long userId = usuarioOpt.get().getUsuarioId();
            
            NomadeRespuestaDTO<ProcesoNomadeDTO> procesoNomade = procesoService.getProcesoNomadeById(procesoId, token);
            if (procesoNomade == null || !procesoNomade.isProcesado() || 
                procesoNomade.getListado() == null || procesoNomade.getListado().isEmpty()) {
                throw new NotFoundException("Proceso con ID " + procesoId + " no encontrado");
            }
            
            Log.warn("proceso: " + procesoNomade.getListado().get(0).getNombre());
            
            InstanciaCrearDTO instanciaData = new InstanciaCrearDTO();
            instanciaData.setNumero(0);
            instanciaData.setProceso(procesoId);
            instanciaData.setDatos(List.of());
            instanciaData.setEtapas(List.of());
            instanciaData.setCreacion(java.time.LocalDateTime.now().toString());
            instanciaData.setCreador(userId);
            instanciaData.setEnProceso(null);
            
            String instanciaDataJson = objectMapper.writeValueAsString(instanciaData);
            Log.warn("instanciaData: " + instanciaDataJson);

            NomadeCrearInstanciaDTO body = new NomadeCrearInstanciaDTO();
            body.setSesion(token);
            body.setInstancia(instanciaData);
            
            Log.warn("token: " + body.getSesion());

            String bodyJson = objectMapper.writeValueAsString(body);
            Log.warn("JSON enviado: " + bodyJson); 
        
            NomadeRespuestaDTO<InstanciaNomadeDTO> respuesta = nomadeApiClient.crearInstancia(bodyJson);
            String respuestaJson = objectMapper.writeValueAsString(respuesta);
            Log.warn("respuestaJson: " + respuestaJson);

            Log.warn("respuesta: " + respuesta.isProcesado());
            Log.warn("respuesta.getListado(): " + respuesta.getListado() != null);
            Log.warn("respuesta.getListado().isEmpty(): " + respuesta.getListado().isEmpty());
            
            if (respuesta != null && respuesta.isProcesado() && respuesta.getListado() != null && !respuesta.getListado().isEmpty()) {
                return respuesta.getListado().get(0);
            } else {
                String errorMessage = respuesta != null && respuesta.getError() != null ? respuesta.getError() : "Error al crear instancia";
                throw new RuntimeException("Error al crear instancia: " + errorMessage);
            }
        } catch (JsonProcessingException e) {
            throw new RuntimeException("Error creating JSON for Nomade API", e);
        }
    }

    public InstanciaNomadeDTO avanzarEtapa(String token, int instanciaId) {
        
        try {
            Optional<UsuarioIdentificadoDTO> usuarioOpt = identificacionService.getUserIdFromSession(token);
            if (usuarioOpt.isEmpty()) {
                throw new RuntimeException("No se pudo identificar al usuario con el token proporcionado");
            }
            
            Long userId = usuarioOpt.get().getUsuarioId();
            
            InstanciaNomadeDTO instanciaActual = getInstancia(token, instanciaId);
            if (instanciaActual == null) {
                throw new NotFoundException("No se encontró la instancia con ID " + instanciaId);
            }
            
            Log.warn("Estado de la instancia: enProceso = " + instanciaActual.getEnProceso());
            if (instanciaActual.getEnProceso() != null) {
                Log.warn("La instancia está en procesamiento. Esto puede causar que Nomade rechace la petición.");
                Log.warn("Se intentará avanzar etapa, pero puede fallar si el procesamiento no se ha completado.");
            }
            
            NomadeRespuestaDTO<ProcesoNomadeDTO> procesoNomade = procesoService.getProcesoNomadeById(instanciaActual.getProceso(), token);
            if (procesoNomade == null || !procesoNomade.isProcesado() || 
                procesoNomade.getListado() == null || procesoNomade.getListado().isEmpty()) {
                throw new NotFoundException("Proceso con ID " + instanciaActual.getProceso() + " no encontrado");
            }
            
            ProcesoNomadeDTO proceso = procesoNomade.getListado().get(0);
            
            EtapaInstanciaNomadeDTO etapaActual = null;
            if (instanciaActual.getEtapas() != null && !instanciaActual.getEtapas().isEmpty()) {
                etapaActual = instanciaActual.getEtapas().get(instanciaActual.getEtapas().size() - 1);
            }
            
            if (etapaActual == null) {
                throw new RuntimeException("No se pudo determinar la etapa actual de la instancia");
            }
            
            EtapaNomadeDTO etapaProceso = null;
            for (EtapaNomadeDTO etapa : proceso.getEtapas()) {
                if (etapa.getNumero() == etapaActual.getEtapa()) {
                    etapaProceso = etapa;
                    break;
                }
            }
            
            if (etapaProceso == null) {
                throw new RuntimeException("No se encontró la etapa actual en la definición del proceso");
            }
            
            if (etapaProceso.getTransiciones() == null || etapaProceso.getTransiciones().isEmpty()) {
                throw new RuntimeException("No hay transiciones disponibles desde la etapa actual " + etapaActual.getEtapa());
            }
            
            Log.warn("Transiciones disponibles desde etapa " + etapaActual.getEtapa() + ":");
            for (TransicionNomadeDTO transicion : etapaProceso.getTransiciones()) {
                Log.warn("  - Transición " + transicion.getNumero() + " (" + transicion.getNombre() + 
                        "): origen=" + transicion.getOrigen() + ", destino=" + transicion.getDestino() + 
                        ", tipo=" + transicion.getTipo() + " (" + (transicion.getTipo() == 0 ? "Interactiva" : "Automática") + ")");
            }
            
            TransicionNomadeDTO transicionSeleccionada = null;
            
            // Para transición MANUAL (sin body), buscar solo transiciones manuales (tipo == 0)
            for (TransicionNomadeDTO transicion : etapaProceso.getTransiciones()) {
                if (transicion.getTipo() == 0) { // Solo transiciones manuales
                    transicionSeleccionada = transicion;
                    Log.warn("Seleccionada transición manual: " + transicion.getNumero() + " (" + transicion.getNombre() + ")");
                    break;
                }
            }
            
            if (transicionSeleccionada == null) {
                throw new RuntimeException("No hay transiciones manuales disponibles desde la etapa actual " + etapaActual.getEtapa());
            }
            
            int etapaDestinoId = transicionSeleccionada.getDestino();
            int transicionId = transicionSeleccionada.getNumero();
            
            String nombreEtapaDestino = "";
            for (EtapaNomadeDTO etapa : proceso.getEtapas()) {
                if (etapa.getNumero() == etapaDestinoId) {
                    nombreEtapaDestino = etapa.getNombre();
                    break;
                }
            }
            
            if (nombreEtapaDestino.isEmpty()) {
                throw new RuntimeException("No se pudo determinar el nombre de la etapa destino");
            }
            
            Log.warn("Avanzando de etapa " + etapaActual.getEtapa() + " (" + etapaActual.getNombre() + 
                    ") a etapa " + etapaDestinoId + " (" + nombreEtapaDestino + 
                    ") usando transición " + transicionId + " (" + transicionSeleccionada.getNombre() + 
                    ") - Tipo: " + (transicionSeleccionada.getTipo() == 0 ? "Interactiva" : "Automática"));
            
            EtapaInstanciaNomadeDTO nuevaEtapa = new EtapaInstanciaNomadeDTO();
            nuevaEtapa.setNumero(0);
            nuevaEtapa.setNombre(nombreEtapaDestino);
            nuevaEtapa.setEtapa(etapaDestinoId);
            nuevaEtapa.setTransicion(transicionId);
            nuevaEtapa.setUsuario(userId.intValue());
            nuevaEtapa.setIngreso("");
            
            InstanciaNomadeDTO instanciaActualizada = new InstanciaNomadeDTO();
            instanciaActualizada.setNumero(instanciaActual.getNumero());
            instanciaActualizada.setProceso(instanciaActual.getProceso());
            instanciaActualizada.setDatos(instanciaActual.getDatos() != null ? instanciaActual.getDatos() : List.of());
            instanciaActualizada.setCreacion(instanciaActual.getCreacion());
            instanciaActualizada.setCreador(instanciaActual.getCreador());
            instanciaActualizada.setEnProceso(null);
            
            instanciaActualizada.setEtapas(List.of(nuevaEtapa));
            
            AvanzarEtapaRequestDTO request = new AvanzarEtapaRequestDTO();
            request.setSesion(token);
            request.setInstancia(instanciaActualizada);
            
            String requestJson = objectMapper.writeValueAsString(request);
            Log.warn("Request para avanzar etapa: " + requestJson);
            
            Log.warn("Estructura del request:");
            Log.warn("  - Sesión: " + token);
            Log.warn("  - Instancia ID: " + instanciaActualizada.getNumero());
            Log.warn("  - Proceso ID: " + instanciaActualizada.getProceso());
            Log.warn("  - Nueva etapa: " + nuevaEtapa.getEtapa() + " (" + nuevaEtapa.getNombre() + ")");
            Log.warn("  - Transición utilizada: " + nuevaEtapa.getTransicion());
            Log.warn("  - Usuario: " + nuevaEtapa.getUsuario());
            Log.warn("  - Timestamp: " + nuevaEtapa.getIngreso());
            Log.warn("  - Datos: " + (instanciaActualizada.getDatos() != null ? instanciaActualizada.getDatos().size() : 0) + " elementos");
            Log.warn("  - Etapas: " + instanciaActualizada.getEtapas().size() + " elementos");
            Log.warn("  - Etapas previas: " + (instanciaActual.getEtapas() != null ? instanciaActual.getEtapas().size() : 0) + " elementos");
            Log.warn("  - enProceso: " + instanciaActualizada.getEnProceso());
            
            NomadeRespuestaDTO<InstanciaNomadeDTO> respuesta = nomadeApiClient.avanzarEtapa(requestJson);
            
            Log.warn("Respuesta de Nomade:");
            Log.warn("  - Procesado: " + (respuesta != null ? respuesta.isProcesado() : "null"));
            Log.warn("  - Error: " + (respuesta != null ? respuesta.getError() : "null"));
            Log.warn("  - Listado: " + (respuesta != null && respuesta.getListado() != null ? respuesta.getListado().size() : 0) + " elementos");
            
            if (respuesta != null && respuesta.isProcesado() && respuesta.getListado() != null && !respuesta.getListado().isEmpty()) {
                return respuesta.getListado().get(0);
            } else {
                String errorMessage = respuesta != null && respuesta.getError() != null ? respuesta.getError() : "Error al avanzar etapa";
                throw new RuntimeException("Error al avanzar etapa: " + errorMessage);
            }
            
        } catch (JsonProcessingException e) {
            throw new RuntimeException("Error creating JSON for Nomade API", e);
        }
    }

    public InstanciaNomadeDTO avanzarEtapaAutomatica(String token, int instanciaId, List<VariableConValorDTO> variables) {
        try {
            Log.info("=== INICIO avanzarEtapaAutomatica ===");
            Log.info("Instancia ID: " + instanciaId);
            Log.info("Variables recibidas: " + (variables != null ? variables.size() : 0));
            
            InstanciaNomadeDTO instanciaActual = getInstancia(token, instanciaId);
            if (instanciaActual == null) {
                throw new NotFoundException("No se encontró la instancia con ID " + instanciaId);
            }
            
    
            NomadeRespuestaDTO<ProcesoNomadeDTO> procesoNomade = procesoService.getProcesoNomadeById(instanciaActual.getProceso(), token);
            if (procesoNomade == null || !procesoNomade.isProcesado() || 
                procesoNomade.getListado() == null || procesoNomade.getListado().isEmpty()) {
                throw new NotFoundException("Proceso con ID " + instanciaActual.getProceso() + " no encontrado");
            }
            
            ProcesoNomadeDTO proceso = procesoNomade.getListado().get(0);
            
            EtapaInstanciaNomadeDTO etapaActual = null;
            if (instanciaActual.getEtapas() != null && !instanciaActual.getEtapas().isEmpty()) {
                etapaActual = instanciaActual.getEtapas().get(instanciaActual.getEtapas().size() - 1);
            }
            
            if (etapaActual == null) {
                throw new RuntimeException("No se pudo determinar la etapa actual de la instancia");
            }
            
            // Buscar transición automática
            EtapaNomadeDTO etapaProceso = null;
            for (EtapaNomadeDTO etapa : proceso.getEtapas()) {
                if (etapa.getNumero() == etapaActual.getEtapa()) {
                    etapaProceso = etapa;
                    break;
                }
            }
            
            if (etapaProceso == null) {
                throw new RuntimeException("No se encontró la etapa actual en la definición del proceso");
            }
            
            // Buscar transición automática
            TransicionNomadeDTO transicionAutomatica = null;
            if (etapaProceso.getTransiciones() != null) {
                for (TransicionNomadeDTO transicion : etapaProceso.getTransiciones()) {
                    if (transicion.getTipo() == 1) { // Tipo 1 = Automática
                        transicionAutomatica = transicion;
                        break;
                    }
                }
            }
            
            if (transicionAutomatica == null) {
                throw new RuntimeException("No hay transiciones automáticas disponibles desde la etapa actual " + etapaActual.getEtapa());
            }
            
            Log.info("Transición automática encontrada: " + transicionAutomatica.getNumero() + " (" + transicionAutomatica.getNombre() + ")");
            
            List<DatoInstanciaNomadeDTO> datosParaNomade = construirDatosParaNomade(variables, etapaActual.getEtapa());
            
            // Construir instancia para Nomade
            InstanciaNomadeDTO instanciaParaNomade = new InstanciaNomadeDTO();
            instanciaParaNomade.setNumero(instanciaActual.getNumero());
            instanciaParaNomade.setProceso(instanciaActual.getProceso());
            instanciaParaNomade.setDatos(datosParaNomade);
            instanciaParaNomade.setEtapas(List.of()); // Array vacío para transiciones automáticas
            
            AvanzarEtapaRequestDTO request = new AvanzarEtapaRequestDTO();
            request.setSesion(token);
            request.setInstancia(instanciaParaNomade);
            
            String requestJson = objectMapper.writeValueAsString(request);
            Log.info("Request para Nomade: " + requestJson);
            
            // Enviar a Nomade
            NomadeRespuestaDTO<InstanciaNomadeDTO> respuesta = nomadeApiClient.avanzarEtapa(requestJson);
            
            Log.info("Respuesta de Nomade:");
            Log.info("  - Procesado: " + (respuesta != null ? respuesta.isProcesado() : "null"));
            Log.info("  - Error: " + (respuesta != null ? respuesta.getError() : "null"));
            Log.info("  - Listado: " + (respuesta != null && respuesta.getListado() != null ? respuesta.getListado().size() : 0) + " elementos");
            
            if (respuesta != null && respuesta.isProcesado() && respuesta.getListado() != null && !respuesta.getListado().isEmpty()) {
                Log.info("=== FIN avanzarEtapaAutomatica (EXITOSO) ===");
                return respuesta.getListado().get(0);
            } else {
                String errorMessage = respuesta != null && respuesta.getError() != null ? respuesta.getError() : "Error al avanzar etapa automática";
                throw new RuntimeException("Error al avanzar etapa automática: " + errorMessage);
            }
            
        } catch (JsonProcessingException e) {
            throw new RuntimeException("Error creating JSON for Nomade API", e);
        } catch (Exception e) {
            Log.error("Error inesperado en avanzarEtapaAutomatica: " + e.getMessage());
            e.printStackTrace();
            throw e;
        }
    }

    private List<DatoInstanciaNomadeDTO> construirDatosParaNomade(List<VariableConValorDTO> variables, Integer etapaActual) {
        List<DatoInstanciaNomadeDTO> datos = new ArrayList<>();
        
        if (variables != null) {
            for (VariableConValorDTO variable : variables) {
                DatoInstanciaNomadeDTO dato = new DatoInstanciaNomadeDTO();
                dato.setNumero(0); // Siempre 0 según especificación
                dato.setDato(variable.getDato());
                dato.setEtapa(etapaActual);
    
                
                // Construir valor según el tipo
                ValorDatoNomadeDTO valor = new ValorDatoNomadeDTO();
                valor.setTipo(variable.getTipo());
                valor.setDato(variable.getDato());
                valor.setTipoDeDato("valor"); // Siempre "valor" según especificación
                
                // Asignar solo el valor correspondiente al tipo
                switch (variable.getTipo()) {
                    case 0: // Numérico
                        if (variable.getValor() instanceof Number) {
                            valor.setNumero(((Number) variable.getValor()).doubleValue());
                        }
                        break;
                    case 1: // Cadena
                        valor.setCadena(variable.getValor().toString());
                        break;
                    case 2: // Archivo
                        // Para archivos, el valor debe contener tanto el objeto archivo como el base64
                        if (variable.getValor() instanceof Map) {
                            @SuppressWarnings("unchecked")
                            Map<String, Object> archivoData = (Map<String, Object>) variable.getValor();
                            
                            // Construir el objeto archivo
                            ArchivoValorNomadeDTO archivo = new ArchivoValorNomadeDTO();
                            if (archivoData.containsKey("instancia")) {
                                archivo.setInstancia(((Number) archivoData.get("instancia")).intValue());
                            }
                            if (archivoData.containsKey("numero")) {
                                archivo.setNumero(((Number) archivoData.get("numero")).intValue());
                            }
                            if (archivoData.containsKey("nombre")) {
                                archivo.setNombre((String) archivoData.get("nombre"));
                            }
                            valor.setArchivo(archivo);
                            
                            // Establecer el base64 si está presente
                            if (archivoData.containsKey("base64")) {
                                valor.setBase64((String) archivoData.get("base64"));
                            }
                        }
                        break;
                    case 3: // Lógico
                        if (variable.getValor() instanceof Boolean) {
                            valor.setVerdadero((Boolean) variable.getValor());
                        }
                        break;
                    case 4: // Fecha
                        // Aceptar fechas como String en formato ISO 8601
                        if (variable.getValor() instanceof String) {
                            valor.setFecha((String) variable.getValor());
                        } else if (variable.getValor() instanceof java.util.Date) {
                            // Convertir Date a String ISO 8601
                            java.util.Date date = (java.util.Date) variable.getValor();
                            java.time.Instant instant = date.toInstant();
                            valor.setFecha(instant.toString());
                        } else {
                            // Intentar convertir a String
                            valor.setFecha(variable.getValor().toString());
                        }
                        break;
                    case 5: // Opción
                        valor.setOpcion(variable.getValor().toString());
                        break;
                    case 6: // Respuesta Servicio
                        // Para respuesta de servicio, almacenamos el objeto completo
                        valor.setRespuestaServicio(variable.getValor());
                        break;
                }
                
                dato.setValor(valor);
                datos.add(dato);
            }
        }
        
        return datos;
    }

    public List<InstanciaNomadeDTO> getInstanciasFinalizadas(String token) {
        try {
            Log.info("=== INICIO getInstanciasFinalizadas ===");
            
            // PASO 1: Obtener instancias del usuario usando su propio token
            // Nomade ya filtra automáticamente por el usuario del token
            Log.info("Obteniendo instancias del usuario con su token...");
            List<InstanciaNomadeDTO> instanciasUsuario = getInstancias(token);
            Log.info("Instancias del usuario obtenidas: " + instanciasUsuario.size());
            
            List<InstanciaNomadeDTO> instanciasFinalizadas = new ArrayList<>();
            
            Log.info("Verificando cuáles están finalizadas...");
            for (InstanciaNomadeDTO instancia : instanciasUsuario) {
                Log.info("Verificando instancia " + instancia.getNumero() + " (proceso " + instancia.getProceso() + ")");
                if (isInstanciaFinalizada(token, instancia)) {
                    Log.info("Instancia " + instancia.getNumero() + " está finalizada - AGREGADA");
                    instanciasFinalizadas.add(instancia);
                } else {
                    Log.info("Instancia " + instancia.getNumero() + " NO está finalizada - OMITIDA");
                }
            }
            
            Log.info("Total de instancias finalizadas del usuario: " + instanciasFinalizadas.size());
            Log.info("=== FIN getInstanciasFinalizadas ===");
            return instanciasFinalizadas;
        } catch (Exception e) {
            Log.error("Error obteniendo instancias finalizadas: " + e.getMessage());
            e.printStackTrace();
            return Collections.emptyList();
        }
    }

    public InstanciaNomadeDTO getInstanciaFinalizadaById(String token, int id) {
        try {
            Log.info("=== INICIO getInstanciaFinalizadaById ===");
            Log.info("Buscando instancia finalizada con ID: " + id);
            
            Log.info("Obteniendo instancia específica con token del usuario...");
            InstanciaNomadeDTO instancia = getInstancia(token, id);
            
            if (instancia == null) {
                Log.warn("Instancia con ID " + id + " no encontrada");
                return null;
            }
            
            Log.info("Instancia encontrada: " + instancia.getNumero() + " (proceso " + instancia.getProceso() + ")");
            
            Log.info("Verificando si la instancia está finalizada...");
            if (isInstanciaFinalizada(token, instancia)) {
                Log.info("Instancia " + instancia.getNumero() + " está finalizada - RETORNANDO");
                Log.info("=== FIN getInstanciaFinalizadaById ===");
                return instancia;
            } else {
                Log.warn("Instancia " + instancia.getNumero() + " NO está finalizada - NO RETORNANDO");
                Log.info("=== FIN getInstanciaFinalizadaById ===");
                return null;
            }
            
        } catch (Exception e) {
            Log.error("Error obteniendo instancia finalizada por ID: " + e.getMessage());
            e.printStackTrace();
            return null;
        }
    }

    private boolean isInstanciaFinalizada(String token, InstanciaNomadeDTO instancia) {
        try {
            Log.info("  Verificando instancia " + instancia.getNumero() + " del proceso " + instancia.getProceso());
            
            Log.info("  Obteniendo estructura del proceso " + instancia.getProceso());
            NomadeRespuestaDTO<ProcesoNomadeDTO> procesoRespuesta = procesoService.getProcesoNomadeById(instancia.getProceso(), token);
            
            if (procesoRespuesta == null || !procesoRespuesta.isProcesado() || 
                procesoRespuesta.getListado() == null || procesoRespuesta.getListado().isEmpty()) {
                Log.warn("  No se pudo obtener el proceso " + instancia.getProceso());
                return false;
            }
            
            ProcesoNomadeDTO proceso = procesoRespuesta.getListado().get(0);
            Log.info("  Proceso obtenido: " + proceso.getNumero() + " - " + proceso.getNombre());
            Log.info("  Etapas del proceso: " + (proceso.getEtapas() != null ? proceso.getEtapas().size() : 0) + " etapas");
            
            Log.info("  Buscando etapas finales del proceso...");
            List<EtapaNomadeDTO> etapasFinales = encontrarEtapasFinales(proceso.getEtapas());
            if (etapasFinales.isEmpty()) {
                Log.warn("  Proceso " + proceso.getNumero() + " no tiene etapas finales definidas (teFin == 1). La instancia " + instancia.getNumero() + " no se considera finalizada.");
                return false;
            }
            
            Log.info("  Etapas finales encontradas: " + etapasFinales.size());
            for (EtapaNomadeDTO etapaFinal : etapasFinales) {
                Log.info("    - Etapa " + etapaFinal.getNumero() + " - " + etapaFinal.getNombre() + " (tipo: " + etapaFinal.getTipo() + ")");
            }
            
            boolean llegoAEtapaFinal = instanciaLlegoAEtapaFinal(instancia, etapasFinales);
            Log.info("  ¿Llegó a alguna etapa final? " + llegoAEtapaFinal);
            
            return llegoAEtapaFinal;
            
        } catch (Exception e) {
            Log.error("  Error verificando si instancia está finalizada: " + e.getMessage());
            e.printStackTrace();
            return false;
        }
    }

    private List<EtapaNomadeDTO> encontrarEtapasFinales(List<EtapaNomadeDTO> etapas) {
        if (etapas == null || etapas.isEmpty()) {
            return Collections.emptyList();
        }
        
        List<EtapaNomadeDTO> etapasFinales = new ArrayList<>();
        
        for (EtapaNomadeDTO etapa : etapas) {
            if (etapa.getTipo() == 1) {
                etapasFinales.add(etapa);
            }
        }
        
        return etapasFinales;
    }

    public boolean deleteInstancia(int id) {
        try {
            Log.info("=== INICIO deleteInstancia ===");
            Log.info("ID de instancia a eliminar: " + id);

            SessionDTO adminToken = getAdminToken();
            if (adminToken == null || adminToken.getToken() == null) {
                Log.error("No se pudo obtener el token de administrador.");
                return false;
            }
            Log.info("Token de administrador obtenido.");

            InstanciaDeleteNomadeDTO deleteRequest = new InstanciaDeleteNomadeDTO(adminToken.getToken(), id);
            String pedidoJson = objectMapper.writeValueAsString(deleteRequest);
            Log.info("JSON para eliminar instancia: " + pedidoJson);

            NomadeRespuestaDTO<InstanciaNomadeDTO> respuesta = nomadeApiClient.deleteInstancia(pedidoJson);
            Log.info("Respuesta de Nomade recibida.");

            if (respuesta != null) {
                Log.info("Procesado: " + respuesta.isProcesado());
                Log.info("Error: " + respuesta.getError());
                Log.info("Total: " + respuesta.getTotal());
            }

            if (respuesta != null && respuesta.isProcesado()) {
                Log.info("Instancia " + id + " eliminada exitosamente.");
                Log.info("=== FIN deleteInstancia (EXITOSO) ===");
                return true;
            } else {
                Log.error("Error al eliminar la instancia " + id + ". Respuesta de Nomade: " + (respuesta != null ? respuesta.getError() : "Respuesta nula"));
                Log.info("=== FIN deleteInstancia (FALLIDO) ===");
                return false;
            }
        } catch (JsonProcessingException e) {
            Log.error("Error creando JSON para la API de Nomade: " + e.getMessage(), e);
            throw new RuntimeException("Error al crear JSON para la API de Nomade", e);
        } catch (Exception e) {
            Log.error("Error inesperado en deleteInstancia: " + e.getMessage(), e);
            return false;
        }
    }

    private boolean instanciaLlegoAEtapaFinal(InstanciaNomadeDTO instancia, List<EtapaNomadeDTO> etapasFinales) {
        if (instancia.getEtapas() == null || instancia.getEtapas().isEmpty()) {
            Log.info("    Instancia no tiene etapas");
            return false;
        }
        
        Log.info("    Etapas de la instancia:");
        for (EtapaInstanciaNomadeDTO etapaInstancia : instancia.getEtapas()) {
            Log.info("      - Etapa " + etapaInstancia.getNumero() + ": " + etapaInstancia.getEtapa() + " (" + etapaInstancia.getNombre() + ")");
        }
        
        Log.info("    Etapas finales del proceso:");
        for (EtapaNomadeDTO etapaFinal : etapasFinales) {
            Log.info("      - Etapa " + etapaFinal.getNumero() + " (" + etapaFinal.getNombre() + ")");
        }
        

        EtapaInstanciaNomadeDTO ultimaEtapaInstancia = instancia.getEtapas().get(instancia.getEtapas().size() - 1);
        Log.info("    Última etapa de la instancia: " + ultimaEtapaInstancia.getEtapa() + " (" + ultimaEtapaInstancia.getNombre() + ")");
        
        boolean llegoAEtapaFinal = false;
        if (ultimaEtapaInstancia.getEtapa() != null) {
            for (EtapaNomadeDTO etapaFinal : etapasFinales) {
                if (ultimaEtapaInstancia.getEtapa().equals(etapaFinal.getNumero())) {
                    Log.info("    La instancia llegó a la etapa final: " + etapaFinal.getNumero() + " (" + etapaFinal.getNombre() + ")");
                    llegoAEtapaFinal = true;
                    break;
                }
            }
        }
        
        Log.info("¿La última etapa es alguna etapa final? " + llegoAEtapaFinal);
        
        return llegoAEtapaFinal;
    }


    public CargarArchivoResponseDTO cargarArchivo(String token, int instanciaId, CargarArchivoRequestDTO request) {
        try {
            Log.info("=== INICIO cargarArchivo ===");
            Log.info("Instancia ID: " + instanciaId);
            Log.info("Request: " + request.toString());

            // 1. Validar que la instancia existe
            InstanciaNomadeDTO instanciaActual = getInstancia(token, instanciaId);
            if (instanciaActual == null) {
                Log.warn("Instancia con ID " + instanciaId + " no encontrada");
                return CargarArchivoResponseDTO.error("Instancia con ID " + instanciaId + " no encontrada");
            }

            Log.info("Instancia encontrada: " + instanciaActual.getNumero() + " (proceso " + instanciaActual.getProceso() + ")");

            // 2. Obtener el proceso para validar la variable
            NomadeRespuestaDTO<ProcesoNomadeDTO> procesoRespuesta = procesoService.getProcesoNomadeById(instanciaActual.getProceso(), token);
            if (procesoRespuesta == null || !procesoRespuesta.isProcesado() || 
                procesoRespuesta.getListado() == null || procesoRespuesta.getListado().isEmpty()) {
                Log.warn("Proceso con ID " + instanciaActual.getProceso() + " no encontrado");
                return CargarArchivoResponseDTO.error("Proceso con ID " + instanciaActual.getProceso() + " no encontrado");
            }

            ProcesoNomadeDTO proceso = procesoRespuesta.getListado().get(0);
            Log.info("Proceso obtenido: " + proceso.getNumero() + " - " + proceso.getNombre());

            // 3. Validar que la variable existe y es de tipo archivo
            DatoProcesoNomadeDTO variableEncontrada = null;
            if (proceso.getDatos() != null) {
                for (DatoProcesoNomadeDTO dato : proceso.getDatos()) {
                    if (dato.getNumero() == request.getVariableId()) {
                        variableEncontrada = dato;
                        break;
                    }
                }
            }

            if (variableEncontrada == null) {
                Log.warn("Variable con ID " + request.getVariableId() + " no encontrada en el proceso");
                return CargarArchivoResponseDTO.error("Variable con ID " + request.getVariableId() + " no encontrada en el proceso");
            }

            if (variableEncontrada.getTipo() != 2) { // Tipo 2 = Archivo
                Log.warn("Variable " + request.getVariableId() + " no es de tipo archivo (tipo actual: " + variableEncontrada.getTipo() + ")");
                return CargarArchivoResponseDTO.error("La variable especificada no es de tipo archivo");
            }

            Log.info("Variable validada: " + variableEncontrada.getNumero() + " - " + variableEncontrada.getNombre() + " (tipo: " + variableEncontrada.getTipo() + ")");

            // 4. Obtener la etapa actual
            EtapaInstanciaNomadeDTO etapaActual = null;
            if (instanciaActual.getEtapas() != null && !instanciaActual.getEtapas().isEmpty()) {
                etapaActual = instanciaActual.getEtapas().get(instanciaActual.getEtapas().size() - 1);
            }

            if (etapaActual == null) {
                Log.warn("No se pudo determinar la etapa actual de la instancia");
                return CargarArchivoResponseDTO.error("No se pudo determinar la etapa actual de la instancia");
            }

            Log.info("Etapa actual: " + etapaActual.getEtapa() + " - " + etapaActual.getNombre());

            // 5. Construir el dato para Nomade
            DatoInstanciaNomadeDTO datoParaNomade = new DatoInstanciaNomadeDTO();
            datoParaNomade.setNumero(0); // Siempre 0 según especificación
            datoParaNomade.setDato(request.getVariableId());
            datoParaNomade.setEtapa(etapaActual.getEtapa());

            // Construir el valor con el archivo
            ValorDatoNomadeDTO valor = new ValorDatoNomadeDTO();
            valor.setTipo(2); // Tipo 2 = Archivo
            valor.setDato(request.getVariableId());
            valor.setBase64(request.getBase64());

            // Construir el objeto archivo
            ArchivoValorNomadeDTO archivo = new ArchivoValorNomadeDTO();
            archivo.setInstancia(instanciaId);
            archivo.setNumero(request.getVariableId());
            archivo.setNombre(request.getNombreArchivo());
            valor.setArchivo(archivo);

            datoParaNomade.setValor(valor);

            // 6. Construir la instancia para Nomade
            InstanciaNomadeDTO instanciaParaNomade = new InstanciaNomadeDTO();
            instanciaParaNomade.setNumero(instanciaActual.getNumero());
            instanciaParaNomade.setProceso(instanciaActual.getProceso());
            instanciaParaNomade.setDatos(List.of(datoParaNomade));
            instanciaParaNomade.setEtapas(List.of()); // Array vacío para modificación de datos

            // 7. Construir el request para Nomade
            AvanzarEtapaRequestDTO requestNomade = new AvanzarEtapaRequestDTO();
            requestNomade.setSesion(token);
            requestNomade.setInstancia(instanciaParaNomade);

            String requestJson = objectMapper.writeValueAsString(requestNomade);
            Log.info("Request para Nomade: " + requestJson);

            // 8. Enviar a Nomade
            NomadeRespuestaDTO<InstanciaNomadeDTO> respuesta = nomadeApiClient.avanzarEtapa(requestJson);

            Log.info("Respuesta de Nomade:");
            Log.info("  - Procesado: " + (respuesta != null ? respuesta.isProcesado() : "null"));
            Log.info("  - Error: " + (respuesta != null ? respuesta.getError() : "null"));
            Log.info("  - Listado: " + (respuesta != null && respuesta.getListado() != null ? respuesta.getListado().size() : 0) + " elementos");

            if (respuesta != null && respuesta.isProcesado() && respuesta.getListado() != null && !respuesta.getListado().isEmpty()) {
                Log.info("Archivo cargado exitosamente en la instancia " + instanciaId);
                Log.info("=== FIN cargarArchivo (EXITOSO) ===");
                return CargarArchivoResponseDTO.exito(instanciaId, request.getVariableId(), request.getNombreArchivo());
            } else {
                String errorMessage = respuesta != null && respuesta.getError() != null ? respuesta.getError() : "Error al cargar archivo";
                Log.warn("Error al cargar archivo: " + errorMessage);
                Log.info("=== FIN cargarArchivo (FALLIDO) ===");
                return CargarArchivoResponseDTO.error("Error al cargar archivo: " + errorMessage);
            }

        } catch (JsonProcessingException e) {
            Log.error("Error creando JSON para Nomade API: " + e.getMessage());
            return CargarArchivoResponseDTO.error("Error interno del servidor al procesar la solicitud");
        } catch (Exception e) {
            Log.error("Error inesperado en cargarArchivo: " + e.getMessage());
            e.printStackTrace();
            return CargarArchivoResponseDTO.error("Error interno del servidor: " + e.getMessage());
        }
    }

    public DescargarArchivoResponseDTO descargarArchivo(String token, int instanciaId, DescargarArchivoRequestDTO request) {
        try {
            Log.info("=== INICIO descargarArchivo ===");
            Log.info("Instancia ID: " + instanciaId);
            Log.info("Request: " + request.toString());

            // 1. Validar que la instancia existe
            InstanciaNomadeDTO instanciaActual = getInstancia(token, instanciaId);
            if (instanciaActual == null) {
                Log.warn("Instancia con ID " + instanciaId + " no encontrada");
                return DescargarArchivoResponseDTO.error("Instancia con ID " + instanciaId + " no encontrada");
            }

            Log.info("Instancia encontrada: " + instanciaActual.getNumero() + " (proceso " + instanciaActual.getProceso() + ")");

            // 2. Construir el pedido para Nomade
            // El formato debe ser: {"sesion":"token","instancia":id,"archivo":archivoId,"enBase64":boolean}
            Map<String, Object> pedidoMap = new HashMap<>();
            pedidoMap.put("sesion", token);
            pedidoMap.put("instancia", instanciaId);
            pedidoMap.put("archivo", request.getArchivoId());
            pedidoMap.put("enBase64", request.getEnBase64() != null ? request.getEnBase64() : false);

            String pedidoJson = objectMapper.writeValueAsString(pedidoMap);
            Log.info("Pedido para Nomade: " + pedidoJson);
            Log.info("Instancia ID: " + instanciaId);
            Log.info("Archivo ID: " + request.getArchivoId());
            Log.info("EnBase64: " + request.getEnBase64());

            // 3. Llamar a Nomade (sin codificar manualmente, el REST Client lo hace automáticamente)
            String respuestaNomade = nomadeApiClient.descargarArchivo(pedidoJson);
            Log.info("Respuesta de Nomade recibida: " + (respuestaNomade != null ? "NO NULL" : "NULL"));

            if (respuestaNomade != null && !respuestaNomade.trim().isEmpty()) {
                Log.info("Archivo descargado exitosamente");
                Log.info("=== FIN descargarArchivo (EXITOSO) ===");
                
                String tipoContenido = (request.getEnBase64() != null && request.getEnBase64()) ? "base64" : "archivo";
                return DescargarArchivoResponseDTO.exito(
                    instanciaId, 
                    request.getArchivoId(), 
                    "archivo_" + request.getArchivoId(), // Nombre genérico, Nomade no devuelve el nombre
                    respuestaNomade, 
                    tipoContenido
                );
            } else {
                Log.warn("Respuesta vacía de Nomade");
                Log.info("=== FIN descargarArchivo (FALLIDO) ===");
                return DescargarArchivoResponseDTO.error("No se pudo descargar el archivo. Respuesta vacía del servidor.");
            }

        } catch (JsonProcessingException e) {
            Log.error("Error creando JSON para Nomade API: " + e.getMessage());
            return DescargarArchivoResponseDTO.error("Error interno del servidor al procesar la solicitud");
        } catch (Exception e) {
            Log.error("Error inesperado en descargarArchivo: " + e.getMessage());
            e.printStackTrace();
            return DescargarArchivoResponseDTO.error("Error interno del servidor: " + e.getMessage());
        }
    }

    public TransicionNomadeDTO determinarTransicionPorVariables(
            ProcesoNomadeDTO proceso, 
            EtapaInstanciaNomadeDTO etapaActual, 
            List<VariableConValorDTO> variablesEnviadas
    ) {
        try {
            Log.info("=== INICIO determinarTransicionPorVariables ===");
            Log.info("Etapa actual: " + etapaActual.getEtapa());
            Log.info("Variables enviadas: " + (variablesEnviadas != null ? variablesEnviadas.size() : 0));
            
            // 1. Buscar la etapa actual en la definición del proceso
            EtapaNomadeDTO etapaProceso = null;
            for (EtapaNomadeDTO etapa : proceso.getEtapas()) {
                if (etapa.getNumero() == etapaActual.getEtapa()) {
                    etapaProceso = etapa;
                    break;
                }
            }
            
            if (etapaProceso == null) {
                throw new RuntimeException("No se encontró la etapa actual en la definición del proceso");
            }
            
            List<TransicionNomadeDTO> transicionesDisponibles = etapaProceso.getTransiciones();
            if (transicionesDisponibles == null || transicionesDisponibles.isEmpty()) {
                throw new RuntimeException("No hay transiciones disponibles desde la etapa actual");
            }
            
            // 2. Crear mapa de variables enviadas para búsqueda rápida
            Map<Integer, Object> variablesMap = new HashMap<>();
            if (variablesEnviadas != null) {
                for (VariableConValorDTO variable : variablesEnviadas) {
                    variablesMap.put(variable.getDato(), variable.getValor());
                }
            }
            
            Log.info("Variables mapeadas: " + variablesMap.keySet());
            
            // 3. Evaluar transiciones automáticas primero (tienen condiciones)
            Log.info("Evaluando " + transicionesDisponibles.size() + " transiciones disponibles");
            for (TransicionNomadeDTO transicion : transicionesDisponibles) {
                Log.info("Transición: " + transicion.getNombre() + " (tipo: " + transicion.getTipo() + ")");
                if (transicion.getTipo() == 1) { // Automática
                    Log.info("Evaluando transición automática: " + transicion.getNombre());
                    if (evaluarCondicionTransicion(transicion, variablesMap, proceso)) {
                        Log.info("Transición automática seleccionada: " + transicion.getNombre());
                        Log.info("=== FIN determinarTransicionPorVariables (AUTOMÁTICA) ===");
                        return transicion;
                    } else {
                        Log.info("Transición automática " + transicion.getNombre() + " no cumple condiciones");
                    }
                }
            }
            
            // 4. Si no hay transiciones automáticas válidas, validar manuales
            Log.info("No se encontraron transiciones automáticas válidas, evaluando manuales");
            for (TransicionNomadeDTO transicion : transicionesDisponibles) {
                if (transicion.getTipo() == 0) { // Manual
                    Log.info("Evaluando transición manual: " + transicion.getNombre());
                    if (validarVariablesParaTransicionManual(transicion, variablesMap, etapaProceso)) {
                        Log.info("Transición manual seleccionada: " + transicion.getNombre());
                        Log.info("=== FIN determinarTransicionPorVariables (MANUAL) ===");
                        return transicion;
                    } else {
                        Log.info("Transición manual " + transicion.getNombre() + " no es válida");
                    }
                }
            }
            
            throw new RuntimeException("No hay transiciones válidas para las variables enviadas");
            
        } catch (Exception e) {
            Log.error("Error determinando transición por variables: " + e.getMessage());
            e.printStackTrace();
            throw e;
        }
    }

    private boolean evaluarCondicionTransicion(
            TransicionNomadeDTO transicion, 
            Map<Integer, Object> variablesMap,
            ProcesoNomadeDTO proceso
    ) {
        try {
            CondicionNomadeDTO condicion = transicion.getCondicion();
            if (condicion == null || condicion.getCondicion() == null) {
                return false;
            }
            
            // Extraer la operación de la condición
            Object condicionObj = condicion.getCondicion();
            if (condicionObj instanceof Map) {
                @SuppressWarnings("unchecked")
                Map<String, Object> condicionMap = (Map<String, Object>) condicionObj;
                
                if (condicionMap.containsKey("operacion")) {
                    @SuppressWarnings("unchecked")
                    Map<String, Object> operacion = (Map<String, Object>) condicionMap.get("operacion");
                    
                    String operador = (String) operacion.get("operador");
                    @SuppressWarnings("unchecked")
                    List<String> operandos = (List<String>) operacion.get("operandos");
                    
                    if ("=".equals(operador) && operandos.size() == 2) {
                        String datoRef = operandos.get(0); // "DATO.cancelarTramite"
                        String valorEsperado = operandos.get(1); // "true"
                        
                        // Extraer ID de la variable del formato "DATO.cancelarTramite"
                        if (datoRef.startsWith("DATO.")) {
                            String nombreVariable = datoRef.substring(5); // "cancelarTramite"
                            Integer variableId = obtenerIdVariablePorNombre(nombreVariable, proceso);
                            
                            if (variableId != null && variablesMap.containsKey(variableId)) {
                                Object valorActual = variablesMap.get(variableId);
                                boolean resultado = valorEsperado.equals(valorActual.toString());
                                Log.info("Condición evaluada: " + datoRef + " = " + valorEsperado + 
                                        " (actual: " + valorActual + ") = " + resultado);
                                return resultado;
                            }
                        }
                    }
                }
            }
            
            return false;
            
        } catch (Exception e) {
            Log.error("Error evaluando condición de transición: " + e.getMessage());
            return false;
        }
    }

    private Integer obtenerIdVariablePorNombre(String nombreVariable, ProcesoNomadeDTO proceso) {
        // Buscar la variable por nombre en la definición del proceso actual
        if (proceso.getDatos() != null) {
            for (DatoProcesoNomadeDTO dato : proceso.getDatos()) {
                if (nombreVariable.equals(dato.getNombre())) {
                    Log.info("Variable encontrada: " + nombreVariable + " -> ID: " + dato.getNumero());
                    return dato.getNumero();
                }
            }
        }
        Log.warn("Variable no encontrada en el proceso: " + nombreVariable);
        return null;
    }

    private boolean validarVariablesParaTransicionManual(
            TransicionNomadeDTO transicion, 
            Map<Integer, Object> variablesMap, 
            EtapaNomadeDTO etapaProceso
    ) {
        try {
            Log.info("Validando variables para transición manual: " + transicion.getNombre());
            
            // 1. Obtener las variables configuradas en la etapa actual
            List<Integer> variablesEtapaActual = new ArrayList<>();
            if (etapaProceso.getDatos() != null) {
                for (DatoEtapaNomadeDTO dato : etapaProceso.getDatos()) {
                    variablesEtapaActual.add(dato.getDato());
                }
            }
            
            Log.info("Variables configuradas en la etapa: " + variablesEtapaActual);
            Log.info("Variables enviadas: " + variablesMap.keySet());
            
            // 2. Verificar que todas las variables enviadas existan en la etapa
            for (Integer variableId : variablesMap.keySet()) {
                if (!variablesEtapaActual.contains(variableId)) {
                    Log.warn("Variable " + variableId + " no existe en la etapa actual");
                    return false;
                }
            }
            
            // 3. Si no se enviaron variables, la transición manual es válida
            if (variablesMap.isEmpty()) {
                Log.info("No se enviaron variables, transición manual válida");
                return true;
            }
            
            // 4. Si se enviaron variables, todas deben ser válidas para la etapa
            Log.info("Todas las variables enviadas son válidas para la etapa");
            return true;
            
        } catch (Exception e) {
            Log.error("Error validando variables para transición manual: " + e.getMessage());
            return false;
        }
    }

    public InstanciaNomadeDTO avanzarEtapaManualConDatos(String token, int instanciaId, List<VariableConValorDTO> variables) {
        try {
            Log.info("=== INICIO avanzarEtapaManualConDatos ===");
            Log.info("Instancia ID: " + instanciaId);
            Log.info("Variables recibidas: " + (variables != null ? variables.size() : 0));
            
            // PASO 1: Guardar datos primero
            Log.info("PASO 1: Guardando datos en la etapa actual...");
            try {
                cargarDatosEnEtapaActual(token, instanciaId, variables);
                Log.info("PASO 1 EXITOSO: Datos guardados correctamente");
            } catch (Exception e) {
                Log.error("PASO 1 FALLIDO: Error guardando datos: " + e.getMessage());
                throw new RuntimeException("Error guardando datos: " + e.getMessage());
            }
            
            // PASO 2: Avanzar etapa después
            Log.info("PASO 2: Avanzando a la siguiente etapa...");
            InstanciaNomadeDTO instanciaFinal;
            try {
                instanciaFinal = avanzarEtapa(token, instanciaId);
                Log.info("PASO 2 EXITOSO: Etapa avanzada correctamente");
            } catch (Exception e) {
                Log.error("PASO 2 FALLIDO: Error avanzando etapa: " + e.getMessage());
                throw new RuntimeException("Error avanzando etapa: " + e.getMessage() + 
                    ". Los datos fueron guardados correctamente. Intente nuevamente.");
            }
            
            Log.info("=== FIN avanzarEtapaManualConDatos (EXITOSO) ===");
            return instanciaFinal;
            
        } catch (Exception e) {
            Log.error("=== FIN avanzarEtapaManualConDatos (FALLIDO) ===");
            throw e;
        }
    }

    public InstanciaNomadeDTO cargarDatosEnEtapaActual(String token, int instanciaId, List<VariableConValorDTO> variables) {
        try {
            Log.info("=== INICIO cargarDatosEnEtapaActual ===");
            Log.info("Instancia ID: " + instanciaId);
            Log.info("Variables recibidas: " + (variables != null ? variables.size() : 0));

            // 1. Validar que la instancia existe
            InstanciaNomadeDTO instanciaActual = getInstancia(token, instanciaId);
            if (instanciaActual == null) {
                throw new NotFoundException("Instancia con ID " + instanciaId + " no encontrada");
            }

            Log.info("Instancia encontrada: " + instanciaActual.getNumero() + " (proceso " + instanciaActual.getProceso() + ")");

            // 2. Obtener el proceso para validar las variables
            NomadeRespuestaDTO<ProcesoNomadeDTO> procesoRespuesta = procesoService.getProcesoNomadeById(instanciaActual.getProceso(), token);
            if (procesoRespuesta == null || !procesoRespuesta.isProcesado() || 
                procesoRespuesta.getListado() == null || procesoRespuesta.getListado().isEmpty()) {
                throw new NotFoundException("Proceso con ID " + instanciaActual.getProceso() + " no encontrado");
            }

            ProcesoNomadeDTO proceso = procesoRespuesta.getListado().get(0);
            Log.info("Proceso obtenido: " + proceso.getNumero() + " - " + proceso.getNombre());

            // 3. Obtener la etapa actual
            EtapaInstanciaNomadeDTO etapaActual = null;
            if (instanciaActual.getEtapas() != null && !instanciaActual.getEtapas().isEmpty()) {
                etapaActual = instanciaActual.getEtapas().get(instanciaActual.getEtapas().size() - 1);
            }

            if (etapaActual == null) {
                throw new RuntimeException("No se pudo determinar la etapa actual de la instancia");
            }

            Log.info("Etapa actual: " + etapaActual.getEtapa() + " - " + etapaActual.getNombre());

            // 4. Construir los datos para Nomade
            List<DatoInstanciaNomadeDTO> datosParaNomade = construirDatosParaNomade(variables, etapaActual.getEtapa());

            // 5. Construir la instancia para Nomade
            InstanciaNomadeDTO instanciaParaNomade = new InstanciaNomadeDTO();
            instanciaParaNomade.setNumero(instanciaActual.getNumero());
            instanciaParaNomade.setProceso(instanciaActual.getProceso());
            instanciaParaNomade.setDatos(datosParaNomade);
            instanciaParaNomade.setEtapas(List.of()); // Array vacío para modificación de datos

            // 6. Construir el request para Nomade
            AvanzarEtapaRequestDTO requestNomade = new AvanzarEtapaRequestDTO();
            requestNomade.setSesion(token);
            requestNomade.setInstancia(instanciaParaNomade);

            String requestJson = objectMapper.writeValueAsString(requestNomade);
            Log.info("Request para Nomade: " + requestJson);

            // 7. Enviar a Nomade
            NomadeRespuestaDTO<InstanciaNomadeDTO> respuesta = nomadeApiClient.avanzarEtapa(requestJson);

            Log.info("Respuesta de Nomade:");
            Log.info("  - Procesado: " + (respuesta != null ? respuesta.isProcesado() : "null"));
            Log.info("  - Error: " + (respuesta != null ? respuesta.getError() : "null"));
            Log.info("  - Listado: " + (respuesta != null && respuesta.getListado() != null ? respuesta.getListado().size() : 0) + " elementos");

            if (respuesta != null && respuesta.isProcesado() && respuesta.getListado() != null && !respuesta.getListado().isEmpty()) {
                Log.info("Datos cargados exitosamente en la instancia " + instanciaId);
                Log.info("=== FIN cargarDatosEnEtapaActual (EXITOSO) ===");
                return respuesta.getListado().get(0);
            } else {
                String errorMessage = respuesta != null && respuesta.getError() != null ? respuesta.getError() : "Error al cargar datos";
                throw new RuntimeException("Error al cargar datos: " + errorMessage);
            }

        } catch (JsonProcessingException e) {
            Log.error("Error creando JSON para Nomade API: " + e.getMessage());
            throw new RuntimeException("Error interno del servidor al procesar la solicitud", e);
        } catch (Exception e) {
            Log.error("Error inesperado en cargarDatosEnEtapaActual: " + e.getMessage());
            e.printStackTrace();
            throw e;
        }
    }

    public InstanciaNomadeDTO avanzarEtapaConLogicaInteligente(String token, int instanciaId, List<VariableConValorDTO> variables) {
        try {
            Log.info("=== INICIO avanzarEtapaConLogicaInteligente ===");
            Log.info("Instancia ID: " + instanciaId);
            Log.info("Variables recibidas: " + (variables != null ? variables.size() : 0));
            
            // 1. Obtener instancia y proceso
            InstanciaNomadeDTO instancia = getInstancia(token, instanciaId);
            if (instancia == null) {
                throw new NotFoundException("No se encontró la instancia con ID " + instanciaId);
            }
            
            NomadeRespuestaDTO<ProcesoNomadeDTO> procesoRespuesta = procesoService.getProcesoNomadeById(instancia.getProceso(), token);
            if (procesoRespuesta == null || !procesoRespuesta.isProcesado() || 
                procesoRespuesta.getListado() == null || procesoRespuesta.getListado().isEmpty()) {
                throw new NotFoundException("Proceso con ID " + instancia.getProceso() + " no encontrado");
            }
            
            ProcesoNomadeDTO proceso = procesoRespuesta.getListado().get(0);
            
            // 2. Obtener etapa actual
            EtapaInstanciaNomadeDTO etapaActual = null;
            if (instancia.getEtapas() != null && !instancia.getEtapas().isEmpty()) {
                etapaActual = instancia.getEtapas().get(instancia.getEtapas().size() - 1);
            }
            
            if (etapaActual == null) {
                throw new RuntimeException("No se pudo determinar la etapa actual de la instancia");
            }
            
            // 3. Determinar qué transición usar
            TransicionNomadeDTO transicionSeleccionada = determinarTransicionPorVariables(proceso, etapaActual, variables);
            
            // 4. Ejecutar según el tipo de transición
            InstanciaNomadeDTO resultado;
            if (transicionSeleccionada.getTipo() == 1) { // Automática
                Log.info("Ejecutando transición automática: " + transicionSeleccionada.getNombre());
                resultado = avanzarEtapaAutomatica(token, instanciaId, variables);
            } else { // Manual - guardar datos y avanzar
                Log.info("Ejecutando transición manual: " + transicionSeleccionada.getNombre());
                resultado = avanzarEtapaManualConDatos(token, instanciaId, variables);
            }
            
            Log.info("=== FIN avanzarEtapaConLogicaInteligente (EXITOSO) ===");
            return resultado;
            
        } catch (Exception e) {
            Log.error("Error inesperado en avanzarEtapaConLogicaInteligente: " + e.getMessage());
            e.printStackTrace();
            throw e;
        }
    }

    public InstanciaNomadeDTO procesarInstancia(String token, int instanciaId, List<VariableConValorDTO> variables) {
        try {
            Log.info("=== INICIO procesarInstancia ===");
            Log.info("Instancia ID: " + instanciaId);
            Log.info("Variables recibidas: " + (variables != null ? variables.size() : 0));
            
            if (variables == null || variables.isEmpty()) {
                // CASO 1: Solo avanzar etapa (transición manual sin datos)
                Log.info("CASO 1: Transición manual sin datos");
                return avanzarEtapa(token, instanciaId);
            } else {
                // CASO 2: Usar lógica inteligente existente
                Log.info("CASO 2: Usando lógica inteligente para determinar transición");
                return avanzarEtapaConLogicaInteligente(token, instanciaId, variables);
            }
            
        } catch (Exception e) {
            Log.error("Error inesperado en procesarInstancia: " + e.getMessage());
            e.printStackTrace();
            throw e;
        }
    }

    /**
     * Elimina todas las instancias de un proceso específico.
     * Utiliza credenciales de administrador para la operación.
     *
     * @param procesoId ID del proceso cuyas instancias se eliminarán
     * @return Objeto con el resultado de la operación (total intentado, exitosos, fallidos)
     */
    public DeleteInstanciasPorProcesoResultDTO deleteInstanciasPorProceso(int procesoId) {
        try {
            Log.info("=== INICIO deleteInstanciasPorProceso ===");
            Log.info("ID de proceso: " + procesoId);

            // Obtener token de administrador
            SessionDTO adminToken = getAdminToken();
            if (adminToken == null || adminToken.getToken() == null) {
                Log.error("No se pudo obtener el token de administrador.");
                return new DeleteInstanciasPorProcesoResultDTO(0, 0, 0, "No se pudo obtener token de administrador");
            }
            Log.info("Token de administrador obtenido.");

            // Obtener todas las instancias del proceso
            Log.info("Obteniendo instancias del proceso " + procesoId);
            List<InstanciaNomadeDTO> instancias = getInstanciasPorProceso(adminToken.getToken(), procesoId);

            if (instancias == null || instancias.isEmpty()) {
                Log.info("No hay instancias para eliminar del proceso " + procesoId);
                return new DeleteInstanciasPorProcesoResultDTO(0, 0, 0, "No hay instancias para eliminar");
            }

            int total = instancias.size();
            int exitosos = 0;
            int fallidos = 0;

            Log.info("Total de instancias a eliminar: " + total);

            // Eliminar cada instancia
            for (InstanciaNomadeDTO instancia : instancias) {
                Log.info("Eliminando instancia " + instancia.getNumero());
                boolean resultado = deleteInstancia(instancia.getNumero());

                if (resultado) {
                    exitosos++;
                    Log.info("Instancia " + instancia.getNumero() + " eliminada exitosamente.");
                } else {
                    fallidos++;
                    Log.warn("Falló la eliminación de instancia " + instancia.getNumero());
                }
            }

            Log.info("=== FIN deleteInstanciasPorProceso ===");
            Log.info("Total: " + total + ", Exitosos: " + exitosos + ", Fallidos: " + fallidos);

            return new DeleteInstanciasPorProcesoResultDTO(total, exitosos, fallidos,
                exitosos == total ? "Todas las instancias eliminadas exitosamente" :
                    "Se eliminaron " + exitosos + " de " + total + " instancias");

        } catch (Exception e) {
            Log.error("Error inesperado en deleteInstanciasPorProceso: " + e.getMessage(), e);
            return new DeleteInstanciasPorProcesoResultDTO(0, 0, 0, "Error: " + e.getMessage());
        }
    }

    /**
     * Obtiene todas las instancias de un proceso específico.
     * Primero obtiene todas las instancias disponibles y luego filtra por proceso.
     *
     * @param token Token de autenticación
     * @param procesoId ID del proceso
     * @return Lista de instancias del proceso
     */
    private List<InstanciaNomadeDTO> getInstanciasPorProceso(String token, int procesoId) {
        try {
            Log.info("Obteniendo instancias del proceso " + procesoId);

            // Obtener todas las instancias (sin filtro de proceso en el pedido)
            NomadePedidoDTO pedidoTotal = new NomadePedidoDTO(token);
            pedidoTotal.setListado(new NomadePedidoListadoDTO(0, -1));
            pedidoTotal.setEstructuraCompleta(true);

            String pedidoTotalJson = objectMapper.writeValueAsString(pedidoTotal);
            NomadeRespuestaDTO<InstanciaNomadeDTO> respuestaTotal = nomadeApiClient.getInstancias(pedidoTotalJson);

            if (respuestaTotal == null || !respuestaTotal.isProcesado() || respuestaTotal.getTotal() == null) {
                Log.warn("No se pudo obtener el total de instancias");
                return Collections.emptyList();
            }

            int total = respuestaTotal.getTotal();
            Log.info("Total de instancias en el sistema: " + total);

            if (total == 0) {
                return Collections.emptyList();
            }

            // Obtener todas las instancias
            NomadePedidoDTO pedidoCompleto = new NomadePedidoDTO(token);
            pedidoCompleto.setListado(new NomadePedidoListadoDTO(0, total));
            pedidoCompleto.setEstructuraCompleta(true);

            String pedidoCompletoJson = objectMapper.writeValueAsString(pedidoCompleto);
            NomadeRespuestaDTO<InstanciaNomadeDTO> respuestaCompleta = nomadeApiClient.getInstancias(pedidoCompletoJson);

            if (respuestaCompleta != null && respuestaCompleta.isProcesado() && respuestaCompleta.getListado() != null) {
                // Filtrar instancias por proceso
                List<InstanciaNomadeDTO> instanciasFiltradas = new ArrayList<>();
                for (InstanciaNomadeDTO instancia : respuestaCompleta.getListado()) {
                    if (instancia.getProceso() != null && instancia.getProceso() == procesoId) {
                        instanciasFiltradas.add(instancia);
                    }
                }

                Log.info("Se encontraron " + instanciasFiltradas.size() + " instancias del proceso " + procesoId);
                return instanciasFiltradas;
            }

            return Collections.emptyList();

        } catch (JsonProcessingException e) {
            Log.error("Error creando JSON para obtener instancias: " + e.getMessage(), e);
            return Collections.emptyList();
        } catch (Exception e) {
            Log.error("Error obteniendo instancias del proceso: " + e.getMessage(), e);
            return Collections.emptyList();
        }
    }

    /**
     * DTO para el resultado de eliminación masiva de instancias
     */
    public static class DeleteInstanciasPorProcesoResultDTO {
        private int total;
        private int exitosos;
        private int fallidos;
        private String mensaje;

        public DeleteInstanciasPorProcesoResultDTO(int total, int exitosos, int fallidos, String mensaje) {
            this.total = total;
            this.exitosos = exitosos;
            this.fallidos = fallidos;
            this.mensaje = mensaje;
        }

        public int getTotal() {
            return total;
        }

        public void setTotal(int total) {
            this.total = total;
        }

        public int getExitosos() {
            return exitosos;
        }

        public void setExitosos(int exitosos) {
            this.exitosos = exitosos;
        }

        public int getFallidos() {
            return fallidos;
        }

        public void setFallidos(int fallidos) {
            this.fallidos = fallidos;
        }

        public String getMensaje() {
            return mensaje;
        }

        public void setMensaje(String mensaje) {
            this.mensaje = mensaje;
        }
    }
}
