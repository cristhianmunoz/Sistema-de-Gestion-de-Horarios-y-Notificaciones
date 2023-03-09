$('#mensajeAdministrador').on('show.bs.modal', function(event) {
    const button = $(event.relatedTarget) // Button that triggered the modal
    const recipient = button.data('whatever') // Extract info from data-* attributes

    if(recipient){
        const modal = $(this);
        const parts = recipient.split('-')
        modal.find('.modal-title').text(`Notificación:`)
        const articuloVerbal = parts[0] === 'habilidad' ? 'esta' : 'este'
        modal.find('.modal-question').text(`¿Está seguro de que desea eliminar ${articuloVerbal} ${parts[0]}?`)
        modal.find('#operacion').val('eliminacion')

        const id_eliminacion = parts[0] === 'habilidad' ? '#id_habilidad' : '#id_periodo'
        modal.find(id_eliminacion).val(parts[1])
        modal.find('.formEliminar').attr('action', `/gestion_voluntarios/${parts[0]}`);
    }
})