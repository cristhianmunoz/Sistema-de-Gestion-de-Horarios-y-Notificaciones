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

  Escenario: El administrador del personal médico desea asignar un voluntario a una actividad que ya tiene un voluntario asignado
    Dado que tengo un voluntario llamado "Ana" con las habilidades necesarias para la actividad
    Y Ana tiene disponibilidad el día "lunes" de "9:00" hasta "11:00"
    Y existe una actividad el día "lunes" a las "10:00" que ya tiene asignado un voluntario llamado "Juan"
    Cuando el administrador del personal médico asigna a Ana para la actividad
    Entonces el sistema muestra un mensaje de error indicando que la actividad ya tiene asignado un voluntario
    Y no se realiza ninguna actualización del horario de Ana.

  Escenario: El administrador del personal médico desea asignar un voluntario a una actividad regular
    Dado que tengo un voluntario llamado "Pedro" con las habilidades necesarias para atender la actividad regular
    Y Pedro tiene disponibilidad los días "lunes" y "miércoles" de "10:00" a "14:00"
    Y hay una actividad regular los días "lunes" y "miércoles" de "12:00" a "13:00"
    Cuando el administrador del personal médico asigna a Pedro para atender la actividad regular los días "lunes" y "miércoles"
    Entonces el sistema actualiza automáticamente el horario de Pedro
    Y Pedro recibe una notificación sobre su participación en la actividad regular los días "lunes" y "miércoles"

  Escenario: El administrador del personal médico desea asignar un voluntario con horario fijo
    Dado que tengo un voluntario llamado "María" con horario fijo de "9:00" a "17:00" de lunes a viernes
    Y hay una emergencia que requiere atención el día "sábado" a las "14:00"
    Cuando el administrador del personal médico asigna a María para atender la emergencia el día "sábado" a las "14:00"
    Entonces el sistema valida que María no está disponible en ese horario
    Y sugiere al administrador asignar a otro voluntario disponible en ese horario

  Escenario: El administrador del personal médico desea asignar a un voluntario no disponible
    Dado que tengo un voluntario llamado "Mario" que no está disponible para atender una actividad el día "jueves"
    Y hay una actividad el día "jueves" a las "16:00"
    Cuando el administrador del personal médico intenta asignar a Mario para atender la actividad el día "jueves" a las "16:00"
    Entonces el sistema muestra un mensaje de error indicando que Mario no está disponible en ese horario