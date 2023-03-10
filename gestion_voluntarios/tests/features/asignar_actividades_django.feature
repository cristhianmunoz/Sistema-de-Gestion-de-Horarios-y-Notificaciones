# Created by nicol at 27/2/2023
# language: es
  Característica: Asignación de voluntarios a actividades
    Como administrador del personal médico,
    quiero que se asignen voluntarios a las actividades,
    para atender una emergencia.

    Esquema del escenario: Asignar voluntarios a una actividad en una emergencia
      #Dado: precondiciones
      Dado que se tiene una emergencia que aún no es atendida
      Y hay una "<cantidad_voluntarios>" que asistirán sin actividades asignadas
      Y existe una actividad con un "<nombre_actividad>" sin voluntarios asignados
      #Cuando: eventos
      Cuando se le asigna voluntarios a una actividad existente
      #Entonces: resultados
      Entonces el estado de voluntario sera"<es_asignado>"
      Y el estado de la actividad sera"<tiene_voluntario>"
      Y el estado de la emergencia sera"<estado_emergencia>"

      Ejemplos: Asignaciones
      | cantidad_voluntarios | nombre_actividad    | es_asignado | tiene_voluntario | estado_emergencia |
      | 3                    |"Suturar"            | "True"      | "True"           | "True"            |
      | 3                    |"Evacuar"            | "True"      | "True"           | "True"            |
