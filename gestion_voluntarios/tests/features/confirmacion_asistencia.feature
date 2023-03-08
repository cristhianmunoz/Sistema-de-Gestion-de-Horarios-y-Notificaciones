# Created by Cris at 2/23/2023
  # language: es
Característica: Confirmación de asistencia de voluntario en emergencia médica
  Como voluntario,
  quiero confirmar mi asistencia a una emergencia médica
  para ayudar rápidamente cuando se me necesite.

Esquema del escenario: Confirmación de asistencia de voluntarios en emergencia médica
  Dado que se tiene el grupo de '<n>' voluntario y se requiere '<numero_requerido>' voluntarios para la emergencia médica
  Cuando se notifica la emergencia médica a este grupo
  Y el numero de voluntarios que confirmaron su asistencia es '<numero_confirmados>'
  Entonces el número de voluntarios que atenderán la emergencia es '<numero_confirmados>'

  Ejemplos: Confirmar Asistencia Parcial
  |n  |numero_requerido|numero_confirmados|
  |5  |3               |3                 |
  |10 |5               |5                 |


