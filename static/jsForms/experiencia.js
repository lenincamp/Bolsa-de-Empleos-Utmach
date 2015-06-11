/**
 * Created by Lenin on 12/08/2014.
 */
$(function () {

    $('#tblExperiencia').jtable({
        title: 'Experiencia',
        actions: {
            listAction: "/principalEmpleado/hojaVida/experiencia/list/",
            createAction: "/principalEmpleado/hojaVida/experiencia/add/",
            updateAction: '/principalEmpleado/hojaVida/experiencia/edit/',
            deleteAction: '/principalEmpleado/hojaVida/experiencia/del/'
        },
        fields: {
            id: {
                key: true,
                list: false
            },
            Institucion: {
                title: 'Institución',
                width: '20%'

            },
            Area_Trabajo__Nombre: {
                title: 'Área de Trabajo',
                width: '20%',
                options: '/principalEmpleado/hojaVida/experiencia/cmbAreaTrabajo/'
            },
            Puesto: {
                title: 'Puesto',
                width: '20%'
            },
            Fecha_Desde: {
                title: 'Fecha Desde',
                width: '15%',
                type:'date',
                displayFormat: 'dd/mm/yy'
            },
            Fecha_Hasta: {
                title: 'Fecha Hasta',
                width: '15%',
                type:'date',
                displayFormat: 'dd/mm/yy'
            },
            Actividades: {
                title: 'Actividades',
                width: '40%',
                type:'textarea'
            }
        }
    });
    $('#tblExperiencia').jtable('load');

});
