# Creado por el Grupo 2 el 2/24/2023
# language: es

  @expensive_setup
  Característica: Registro de habilidades de los voluntarios
    Como voluntario inscrito en el programa de voluntariado,
    quiero que tomen en cuenta mis habilidades y mi disponibilidad
    para ganar experiencia y adquirir conocimientos prácticos en el área médica.

  Escenario: El voluntario intenta registrar una habilidad médica registrada previamente
    Dado que el voluntario tiene registrada “1.0” habilidad médica con el título “Suturar” con “24.0” horas de experiencia y la descripción “Curso de sutura quirúrgica aprobado”
    Y únicamente existen las habilidades médicas “Suturar”, “Vacunar” y “Anestesiar”
    Cuando el voluntario intente registrar una nueva habilidad médica con el título “Suturar”, con “12.0” horas de experiencia y la descripción “Prácticas informales”
    Entonces el voluntario tendrá registrada “1.0” habilidad médica con el título “Suturar”, con “24.0” horas de experiencia y la descripción “Curso de sutura quirúrgica aprobado”

  Escenario: El voluntario intenta registrar una habilidad médica que no existe
    Dado que el voluntario tiene registradas “0.0” habilidades médicas
    Y únicamente existen las habilidades médicas “Suturar”, “Vacunar” y “Anestesiar”
    Cuando el voluntario intente registrar una nueva habilidad médica con el título “Reanimación Cardiopulmonar”, con “48.0” horas de experiencia y la descripción “Curso de RCP aprobado”
    Entonces el voluntario tendrá registradas “0.0” habilidades médicas

  Escenario: El voluntario registra una nueva habilidad médica
    Dado que el voluntario tiene registradas “0.0” habilidades médicas
    Y únicamente existen las habilidades médicas “Suturar”, “Vacunar” y “Anestesiar”
    Cuando el voluntario intente registrar una nueva habilidad médica con el título “Suturar”, con “24.0” horas de experiencia y la descripción “Curso de sutura quirúrgica aprobado”
    Entonces el voluntario tendrá registrada “1.0” habilidad médica registrada con el título “Suturar”, con “24.0” horas de experiencia y la descripción “Curso de sutura quirúrgica aprobado”

  Esquema del escenario: El voluntario intenta registrar una habilidad médica con horas de experiencia incorrectas
    Dado que el voluntario tiene registradas “0.0” habilidades médicas
    Y únicamente existen las habilidades médicas “Suturar”, “Vacunar” y “Anestesiar”
    Cuando el voluntario intente registrar una nueva habilidad médica con el título “Suturar”, con “<horas_experiencia>” horas de experiencia y la descripción “Curso de sutura quirúrgica aprobado”
    Entonces el voluntario tendrá registradas “0.0” habilidades médicas

    Ejemplos:
      | horas_experiencia |
      | 0.0               |
      | -12.0             |
