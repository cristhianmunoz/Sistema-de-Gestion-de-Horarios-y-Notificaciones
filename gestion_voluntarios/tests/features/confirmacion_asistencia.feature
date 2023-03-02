# Created by Cris at 2/23/2023
  # language: es
Característica: Confirmación de asistencia de voluntario en emergencia médica
  Como voluntario,
  quiero confirmar mi asistencia a una emergencia médica
  para ayudar rápidamente cuando se me necesite.

Esquema del escenario: Confirmación de asistencia de voluntarios en emergencia médica
  Dado que se tiene el grupo de voluntarios conformado por '<lista_voluntarios>'
  Cuando se notifica la emergencia médica a '<n>' personas
  Y el numero de voluntarios es '<numero_confirmados>' confirmados
  Y el numero de voluntarios es '<numero_rechazados>' que rechazaron la emergencia
  Entonces el número de voluntarios que atenderán la '<emergencia>' es '<numero_confirmados>'
  Y los voluntarios asignados a esta emergencia son '<lista_confirmados>'

  Ejemplos: Confirmar Asistencia
  |lista_voluntarios     |n |numero_confirmados|numero_rechazados|emergencia   |lista_confirmados|
  |VOLUNTARIOS 1         |5 |0                 |5                |terremoto    |LISTA 1          |


