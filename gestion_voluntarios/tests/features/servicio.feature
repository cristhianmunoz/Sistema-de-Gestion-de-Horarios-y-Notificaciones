# Created by el Grupo 5 at 2/23/2023
# language: es

Característica: Solicitar servicios
  Como administrador del personal médico deseo solicitar servicios a los voluntarios, para atender las emergencias médicas

  Esquema del escenario: Solicitar servicios para atender una emergencia médica
    Dado que tengo una emergencia con titulo "<tituloEmergencia>" y su descripción "<descripcionEmergencia>" y necesito "<habilidadesRequeridas>"
    Cuando solicite servicios a los "<voluntarios>" registrados en el sistema
    Entonces se enviara una notificacion a los voluntarios con la lista de habilidades requeridas
    Ejemplos:
      | tituloEmergencia | descripcionEmergencia                                            | habilidadesRequeridas            | voluntarios           |
      | Terremoto        | Se necesita voluntarios para atender la emergencia por terremoto | Saturar,Reanimacion, Respiracion | Juan, Pepito, Andres  |
      | Incendio        | Se necesita voluntarios para atender la emergencia por incendio | RCP, Cardiologo                  | Juan, Carlos, Gabriel |