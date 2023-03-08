# Created by el Grupo 5 at 2/23/2023
# language: es

Característica: Solicitar servicios
  Como administrador del personal médico deseo solicitar servicios a los voluntarios, para atender las emergencias médicas

  Esquema del escenario: Solicitar servicios cuando el voluntario no tiene las habilidades requeridas para atender la emergencia
    Dado que tengo una emergencia medica que necesita <num_voluntarios_necesarios>" con "<nombre>" y su descripcion es "<asunto>" y se necesita "<habilidad_requerida>" para atender esa emergencia
    Cuando solicite servicios a los "<voluntarios>" registrados en el sistema
    Y consiga la "<lista_voluntarios_ordenados>" de mayor a menor segun el número de habilidades del voluntario que cumplen de la habilidad requerida"
    Y si el numero de "<voluntario_seleccionado>" es igual al "<num_voluntarios_necesarios>"
    Entonces se enviaran "<numero_de_notificaciones>" notificaciones a la lista de "<voluntario_seleccionado>"
    Ejemplos:
      | num_voluntarios_necesarios | nombre    | asunto                  | habilidad_requerida | voluntarios            | lista_voluntarios_ordenados | voluntario_seleccionado | numero_de_notificaciones |
      | 2                          | Terremoto | Se necesita de su ayuda | Sutura              | Carlos,Juan,Kevin,Pepe | Pepe,Juan,Kevin,Carlos      | Pepe,Juan               | 2                        |