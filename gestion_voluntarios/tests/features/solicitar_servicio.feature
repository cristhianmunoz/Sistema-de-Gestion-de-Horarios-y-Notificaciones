# Created by el Grupo 5 at 2/23/2023
# language: es

Característica: Solicitar servicios
  Como administrador del personal médico deseo solicitar servicios a los voluntarios, para atender las emergencias médicas
  #Falta cuantos para atender la emergencia
  #Los voluntarios tengan habilidades
  #Match de los voluntarios requeridos para atender la emergencia
  #Crear un escenario que permita atender todas las emergencias medicas
  Esquema del escenario: Solicitar servicios cuando el voluntario tiene las habilidades requeridas para atender la emergencia
    Dado que tengo una emergencia medica que necesita <numero_voluntarios_requeridos>" con "<titulo>" y su descripcion es "<descripcion_emergencia>" y se necesita "<habilidades_requeridas>" para atender esa emergencia
    Cuando solicite servicios a los "<voluntarios>" registrados en el sistema
    Y las "<habilidades_voluntario>" "<cumple>" cumplen "<habilidades_requeridas>"
    Entonces conseguire el filtrado con la <lista_voluntarios_seleccionados>"
    Y la cantidad de voluntarios seleccionados sea igual a la cantidad de voluntarios requeridos
    Y se enviaran "<numero_de_notificaciones>" notificaciones en base a la lista de voluntarios seleccionados
    Ejemplos:
      | numero_voluntarios_requeridos | titulo    | descripcion_emergencia                             | habilidades_requeridas | voluntarios              | habilidades_voluntario     | cumple | lista_voluntarios_seleccionados | numero_de_notificaciones |
      | 4                             | Terremoto | Se necesita de su ayuda para atender la emergencia | Saturacion,RCP         | Carlos,Juan,Andres,Kevin | Saturacion,RCP,Respiracion | no     | Carlos,Juan,Andres,Kevin        | 4                        |
      | 4                             | Terremoto | Se necesita de su ayuda para atender la emergencia | Saturacion,RCP         | Carlos,Juan,Andres,Kevin | Saturacion,RCP             | si     | Carlos,Juan,Andres,Kevin        | 4                        |

    #Que sucede cuando la cantidad de voluntarios en la lista de seleccionados es menor al numero de voluntarios requeridos
  # Cuando las habilidades del voluntario son > < = > /2 de las habilidades requeridas