# Created by el Grupo 5 at 2/23/2023
# language: es

Característica: Solicitar servicios
  Como administrador del personal médico deseo solicitar servicios a los voluntarios, para atender las emergencias médicas

  Esquema del escenario: Solicitar servicios cuando el numero de voluntario son los suficientes para atender la emergencia
    Dado que tengo una emergencia medica que necesita <num_voluntarios_necesarios>" con "<nombre>" y su descripcion es "<asunto>" y se necesita "<habilidad_requerida>" para atender esa emergencia
    Cuando solicite servicios a los "<voluntarios>" registrados en el sistema
    Y si el numero de "<voluntario_seleccionado>" es mayor o igual al "<num_voluntarios_necesarios>"
    Entonces se enviaran "<numero_de_notificaciones>" notificaciones a la lista de voluntarios finales
    Ejemplos:
      | num_voluntarios_necesarios | nombre    | asunto                  | habilidad_requerida | voluntarios                                                                                                                                                                                                                                                                                                   | voluntario_seleccionado  | numero_de_notificaciones |
      | 2                          | Terremoto | Se necesita de su ayuda | Anestesiar          |{"voluntario1": {"nombre":"Carlos", "habilidad": ["Vacunar"]},"voluntario2": {"nombre":"Juan", "habilidad": ["Suturar","Anestesiar"]}, "voluntario3":{"nombre":"Kevin","habilidad":["Suturar"]}, "voluntario4":{"nombre":"Pepe","habilidad":["Anestesiar"]}}|Juan,Pepe                 |  2                        |


  Esquema del escenario: Solicitar servicios cuando el numero de voluntarios no son los suficientes para atender la emergencia
    Dado que tengo una emergencia medica que necesita <num_voluntarios_necesarios>" con "<nombre>" y su descripcion es "<asunto>" y se necesita "<habilidad_requerida>" para atender esa emergencia
    Cuando solicite servicios a los "<voluntarios>" registrados en el sistema
    Y si el numero de "<voluntario_seleccionado>" es menor al "<num_voluntarios_necesarios>"
    Entonces se enviara unicamente "<numero_de_notificaciones_exitosas>" a la lista de voluntarios finales
    Ejemplos:
      | num_voluntarios_necesarios | nombre    | asunto                  | habilidad_requerida | voluntarios            | voluntario_seleccionado | numero_de_notificaciones_exitosas |
      | 10                         | Terremoto | Se necesita de su ayuda | Anestesiar          | {"voluntario1": {"nombre":"Carlos", "habilidad": ["Vacunar"]},"voluntario2": {"nombre":"Juan", "habilidad": ["Suturar","Anestesiar"]}, "voluntario3":{"nombre":"Kevin","habilidad":["Suturar"]}, "voluntario4":{"nombre":"Pepe","habilidad":["Anestesiar"]}}| Juan,Pepe               | 2                                 |

