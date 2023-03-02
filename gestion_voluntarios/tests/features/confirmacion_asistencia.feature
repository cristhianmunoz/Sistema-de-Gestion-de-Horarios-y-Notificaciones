# Created by Cris at 2/23/2023
  # language: es
Característica: Confirmación de asistencia de voluntario en emergencia médica
  Como voluntario,
  quiero confirmar mi asistencia a una emergencia médica
  para ayudar rápidamente cuando se me necesite.

Esquema del escenario: Confirmación de asistencia de voluntarios en emergencia médica
  Dado que se tiene el grupo de voluntarios conformado por '<lista_voluntarios>'
  Cuando se notifica la emergencia médica a '<n>' personas
  Y el numero de voluntarios que confirmaron su asistencia es '<n_c>'
  Y el numero de voluntarios que rechazaron la emergencia es '<n_r>'
  Entonces el número de voluntarios que atenderán la '<emergencia>' es '<n_c>'
  Y los voluntarios asignados a esta emergencia son '<lista_confirmados>'

  Ejemplos: Confirmar Asistencia
  |nombre     |apellido |asunto                              |   tipo_emergencia    |ubicacion   |hora_entrada  |encargado     |dirigido_a      |actividades |detalle                    |   deseada   | mensaje                               |
  |Cristopher |Perez    |Accidente en la avenida 10 de Agosto|Accidente de transito |Quito-Norte |18:30         |William Zapata|Cristopher Perez|asasdsad    |Presentarse en el Hospital |  Confirmar  | Se ha confirmado la solicitud enviada |
  |Cristopher |Perez    |Accidente en la avenida 10 de Agosto|Accidente de transito |Quito-Norte |18:30         |William Zapata|Cristopher Perez|asasdsad    |Presentarse en el Hospital |  Cancelar   | Se ha rechazado la solicitud enviada  |

  Ejemplos: Rechazar Asistencia
  |nombre     |apellido |asunto                              |   tipo_emergencia    |ubicacion   |hora_entrada  |encargado     |dirigido_a      |actividades |detalle                    |   deseada   | mensaje                               |
  |Cristopher |Perez    |Accidente en la avenida 10 de Agosto|Accidente de transito |Quito-Norte |18:30         |William Zapata|Cristopher Perez|asasdsad    |Presentarse en el Hospital |  Cancelar   | Se ha rechazado la solicitud enviada  |
  |Cristopher |Perez    |Accidente en la avenida 10 de Agosto|Accidente de transito |Quito-Norte |18:30         |William Zapata|Cristopher Perez|asasdsad    |Presentarse en el Hospital |  Confirmar  | Se ha confirmado la solicitud enviada |
