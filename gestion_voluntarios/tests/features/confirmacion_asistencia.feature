# Created by Cris at 2/23/2023
  # language: es
Característica: Confirmación de asistencia de voluntario en emergencia médica
  Como voluntario,
  quiero confirmar mi asistencia a una emergencia médica
  para ayudar rápidamente cuando se me necesite.

Esquema del escenario: Confirmación de asistencia de voluntario en emergencia médica
  Dado que yo, '<nombre>' '<apellido>', soy un voluntario registrado en el programa de emergencia médica
  Cuando recibo una notificación informándome de una emergencia que contiene los siguientes datos '<asunto>', '<tipo_emergencia>', '<ubicacion>', '<hora_entrada>', '<encargado>', '<dirigido_a>', '<actividades>' y '<detalle>'
  Y selecciono la opción '<deseada>'
  Entonces la opción escogida se registra en el sistema
  Y se me informa que '<mensaje>'

  Ejemplos: Confirmar Asistencia
  |nombre     |apellido |asunto                              |   tipo_emergencia    |ubicacion    |hora_entrada |encargado     |dirigido_a      |actividades |detalle                   |   deseada   | mensaje                               |
  |Cristopher |Perez    |Accidente en la avenida 10 de Agosto|Accidente de transito |Quito-Norte |18:30         |William Zapata|Cristopher Perez|asasdsad   |Presentarse en el Hospital |  Confirmar  | Se ha confirmado la solicitud enviada |
  |Cristopher |Perez    |Accidente en la avenida 10 de Agosto|Accidente de transito |Quito-Norte |18:30         |William Zapata|Cristopher Perez|asasdsad   |Presentarse en el Hospital |  Confirmar  | Se ha rechazado la solicitud enviada  |

  Ejemplos: Rechazar Asistencia
  |nombre     |apellido |asunto                              |   tipo_emergencia    |ubicacion    |hora_entrada |encargado     |dirigido_a      |actividades |detalle                   |   deseada   | mensaje                               |
  |Cristopher |Perez    |Accidente en la avenida 10 de Agosto|Accidente de transito |Quito-Norte |18:30         |William Zapata|Cristopher Perez|asasdsad   |Presentarse en el Hospital |  Cancelar   | Se ha rechazado la solicitud enviada  |
  |Cristopher |Perez    |Accidente en la avenida 10 de Agosto|Accidente de transito |Quito-Norte |18:30         |William Zapata|Cristopher Perez|asasdsad   |Presentarse en el Hospital |  Cancelar   | Se ha confirmado la solicitud enviada |
