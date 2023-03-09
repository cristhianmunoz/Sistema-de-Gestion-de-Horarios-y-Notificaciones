function obtenerFormatoHora(horaDB){
    let valorExtra = 0;
    if (horaDB.endsWith('p.m.')) {
        valorExtra = 12
    }
    const partesHora = horaDB.split(' ')[0].split(':')
    partesHora[0] = partesHora[0].length === 1 ? `0${partesHora[0]}` : partesHora[0]
    if(partesHora.length === 1){
        return `${parseInt(partesHora[0]) + valorExtra}:00`
    }
    return `${parseInt(partesHora[0]) + valorExtra}:${partesHora[1]}`
}

$('#horarioModal').on('show.bs.modal', function(event) {
    const button = $(event.relatedTarget) // Button that triggered the modal
    const recipient = button.data('whatever') // Extract info from data-* attributes
    const modal = $(this);
    const parts = recipient.toString().split('-')
    console.log(parts)

    if(parts.length === 1){
        modal.find('#tituloModalHorario').text('Nuevo horario')
        modal.find('#dia_semana_periodo').val('')
        modal.find('#hora_inicio_periodo').val('')
        modal.find('#hora_fin_periodo').val('')
        modal.find('#id_horario').val(parts[0])
        modal.find('.btn-primary').text('Agregar horario')
        modal.find('#operacion').val('creacion')
    }else{
        modal.find('#tituloModalHorario').text('Actualización de horario')
        modal.find('#dia_semana_periodo').val(parts[0])
        modal.find('#hora_inicio_periodo').val(obtenerFormatoHora(parts[1]))
        modal.find('#hora_fin_periodo').val(obtenerFormatoHora(parts[2]))
        modal.find('#id_horario').val(parts[3])
        modal.find('#id_periodo').val(parts[4])
        modal.find('.btn-primary').text('Actualizar horario')
        modal.find('#operacion').val('edicion')
    }
})

$('#habilidadesModal').on('show.bs.modal', function(event) {
    const button = $(event.relatedTarget) // Button that triggered the modal
    const recipient = button.data('whatever') // Extract info from data-* attributes
    const modal = $(this);

    if(recipient){
        const parts = recipient.split('-')
        modal.find('#tituloModalHabilidad').text('Actualización de habilidad')
        modal.find('#titulo_habilidad').val(parts[0])
        modal.find('#titulo_habilidad').prop('disabled', true)
        modal.find('#descripcion_habilidad').val(parts[1])
        modal.find('#horas_experiencia_habilidad').val(parts[2])
        modal.find('#id_habilidad').val(parts[3])
        modal.find('#operacion').val('edicion')
        modal.find('.btn-primary').text('Actualizar habilidad')
    }else{
        modal.find('#tituloModalHabilidad').text('Nueva habilidad')
        modal.find('#titulo_habilidad').val('')
        modal.find('#titulo_habilidad').prop('disabled', false)
        modal.find('#descripcion_habilidad').val('')
        modal.find('#horas_experiencia_habilidad').val('')
        modal.find('#operacion').val('creacion')
        modal.find('.btn-primary').text('Agregar habilidad')
    }
})

$('#eliminarModal').on('show.bs.modal', function(event) {
    const button = $(event.relatedTarget) // Button that triggered the modal
    const recipient = button.data('whatever') // Extract info from data-* attributes

    if(recipient){
        const modal = $(this);
        const parts = recipient.split('-')
        modal.find('.modal-title').text(`Eliminar ${parts[0]}`)
        const articuloVerbal = parts[0] === 'habilidad' ? 'esta' : 'este'
        modal.find('.modal-question').text(`¿Está seguro de que desea eliminar ${articuloVerbal} ${parts[0]}?`)
        modal.find('#operacion').val('eliminacion')

        const id_eliminacion = parts[0] === 'habilidad' ? '#id_habilidad' : '#id_periodo'
        modal.find(id_eliminacion).val(parts[1])
        modal.find('.formEliminar').attr('action', `/gestion_voluntarios/${parts[0]}`);
    }
})
