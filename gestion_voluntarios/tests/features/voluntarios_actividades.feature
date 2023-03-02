# Created by ferna at 3/1/2023
# language: es

Característica: Asignar un voluntario a una actividad
  Como administrador del personal médico deseo gestionar los horarios del personal para así organizar
  la atención de pacientes y determinar tiempos críticos faltantes

  Escenario: El administrador del personal médico desea asignar un voluntario a una emergencia
    Dado que tengo un voluntario llamado "Juan" con las habilidades necesarias para atender la emergencia
    Y Juan tiene disponibilidad el día "jueves" de "11:00" hasta "13:00"
    Y se presenta una emergencia el día "jueves" a las "12:00"
    Cuando el administrador del personal médico asigna a Juan para atender la emergencia
    Entonces el sistema actualiza automáticamente el horario de Juan
    Y Juan recibe una notificación sobre su participación en la emergencia

  Escenario: El administrador del personal médico necesita cubrir una ausencia imprevista del personal
    Dado que tengo un personal médico que ha informado de una ausencia imprevista en el horario de 12:00 hasta 16:00
    Y necesito encontrar uno o mas voluntario para cubrir su turno en ese horario
    Cuando el administrador del personal médico busca los voluntario disponible para cubrir el turno
    Entonces el sistema muestra una lista de voluntarios disponibles y con las habilidades necesarias
    Y el administrador del personal médico selecciona uno o mas voluntarios adecuado y lo asigna para cubrir el turno
    Y el sistema actualiza automáticamente el horario del voluntario seleccionado