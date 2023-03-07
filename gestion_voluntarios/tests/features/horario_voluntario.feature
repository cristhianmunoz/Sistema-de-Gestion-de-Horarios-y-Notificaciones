# Creado por el Grupo 2 el 2/24/2023
# language: es

  Característica: Registro de horarios de los voluntarios
    Como voluntario inscrito en el programa de voluntariado,
    quiero que tomen en cuenta mis habilidades y mi disponibilidad
    para ganar experiencia y adquirir conocimientos prácticos en el área médica.

  Esquema del escenario: Se comprueba la disponibilidad del voluntario en un horario específico
    Dado que el voluntario está disponible los días “<dia_disponible>” en el periodo de “<inicio_disponible>” a “<final_disponible>” horas
    Cuando se requiera saber si el voluntario está disponible los días “<dia_solicitado>” en el periodo de “<inicio_solicitado>“ a “<final_solicitado>”
    Entonces se tendrá que la disponibilidad del voluntario en el momento requerido es “<disponibilidad>”

    Ejemplos:
      | dia_disponible | inicio_disponible | final_disponible | dia_solicitado | inicio_solicitado | final_solicitado | disponibilidad |
      | Lunes          | 14:00             | 16:00            | Lunes          | 14:00             | 20:00            | False          |
      | Viernes        | 14:00             | 16:00            | Martes         | 14:00             | 16:00            | False          |
      | Martes         | 14:00             | 21:00            | Martes         | 18:00             | 20:00            | True           |
      | Jueves         | 7:00              | 9:00             | Jueves         | 7:00              | 9:00             | True           |

    Esquema del escenario: El voluntario intenta registrar horarios de disponibilidad con horas incorrectas
    Dado que el voluntario tiene registrados “<dias_disponibles_iniciales>” días disponibles
    Cuando el voluntario quiera registrar su disponibilidad los días “<dia_solicitado>” en el periodo de “<inicio_solicitado>” a “<final_solicitado>” horas
    Entonces el voluntario tendrá registrados “<dias_disponibles_finales>” días disponibles

    Ejemplos:
      | dias_disponibles_iniciales | dia_solicitado | inicio_solicitado | final_solicitado | dias_disponibles_finales |
      | 0.0                        | Jueves         | 20:00             | 13:00            | 0.0                      |
      | 0.0                        | Lunes          | 20:00             | 27:00            | 0.0                      |
      | 0.0                        | Lunes          | -10:00            | 12:00            | 0.0                      |

    Escenario: El voluntario registra su horario de disponibilidad
    Dado que el voluntario está disponible los días “Lunes” en el periodo de “14:00” a “16:00” horas
    Cuando el voluntario quiera registrar su disponibilidad los días “Lunes” en el periodo de “15:00” a “16:00” horas
    Entonces el voluntario estará disponible los días “Lunes” en el periodo de “14:00” a “16:00” horas
