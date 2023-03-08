# Created by Cris at 2/23/2023
  # language: es
Característica: Confirmación de asistencia de voluntario en emergencia médica
  Como voluntario,
  quiero confirmar mi asistencia a una emergencia médica
  para ayudar rápidamente cuando se me necesite.

Esquema del escenario: Confirmación de asistencia de voluntarios en emergencia médica
  Dado que se tiene el grupo de '<n>' voluntarios
  Cuando se notifica la emergencia médica a este grupo
  Y el numero de voluntarios que confirmaron su asistencia es '<numero_confirmados>'
  Y el numero de voluntarios que rechazaron la emergencia es '<numero_rechazados>'
  Entonces el número de voluntarios que atenderán la emergencia es '<numero_confirmados>'

  Ejemplos: Confirmar Asistencia Parcial
  |n |numero_confirmados|numero_rechazados   |
  |4 |4                |0                   |


