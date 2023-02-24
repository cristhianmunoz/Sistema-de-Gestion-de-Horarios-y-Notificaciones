# Created by Cris at 2/23/2023
  # language: es
Característica: Confirmación de asistencia de voluntario en emergencia médica
  Como voluntario,
  quiero confirmar mi asistencia a una emergencia médica
  para ayudar rápidamente cuando se me necesite.

Escenario: Confirmación de asistencia de voluntario en emergencia médica
  Dado que soy un voluntario registrado en el programa de emergencia médica
  Cuando recibo una notificación de emergencia
  Y selecciono la opción "Confirmar"
  Entonces mi asistencia es registrada en el sistema
  Y se me notifica mi asignación en la emergencia médica
