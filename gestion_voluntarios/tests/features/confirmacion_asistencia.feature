# Created by Cris at 2/23/2023
  # language: es
Característica: Confirmación de asistencia de voluntario en emergencia médica
  Como voluntario,
  quiero confirmar mi asistencia a una emergencia médica
  para ayudar rápidamente cuando se me necesite.

Esquema del escenario: Confirmación de asistencia de voluntarios en emergencia médica
  Dado que se tiene el grupo de voluntarios conformado por '<lista_voluntarios>'
  Cuando se notifica la emergencia médica a '<n>' personas
  Y el numero de voluntarios que confirmaron su asistencia es '<numero_confirmados>'
  Y el numero de voluntarios que rechazaron la emergencia es '<numero_rechazados>'
  Entonces el número de voluntarios que atenderán la emergencia es '<numero_confirmados>'
  Y los voluntarios asignados a esta emergencia son '<lista_confirmados>'

  Ejemplos: Confirmar Asistencia Parcial
  |lista_voluntarios                                                    |n |numero_confirmados|numero_rechazados   |lista_confirmados                        |
  |Juan Pérez, Pepe Rodríguez, Tomás Muenala, Ana Freire, Gerardo Zapata|5 |3                 |2                   |Juan Pérez, Pepe Rodríguez, Tomás Muenala|


