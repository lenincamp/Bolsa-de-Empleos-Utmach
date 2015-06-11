/**
 * Created by Lenin on 21/08/2014.
 */
/**
 * Created by Lenin on 12/08/2014.
 */
$(function () {

    $('#tblCapacitaciones').jtable({
        title: 'Capacitaciones',
        actions: {
            listAction: "/principalEmpleado/hojaVida/capacitaciones/list/",
            createAction: "/principalEmpleado/hojaVida/capacitaciones/add/",
            updateAction: '/principalEmpleado/hojaVida/capacitaciones/edit/',
            deleteAction: '/principalEmpleado/hojaVida/capacitaciones/del/'
        },
        fields: {
            id: {
                key: true,
                list: false
            },
            Institucion: {
                title: 'Institución'

            },
            Tipo_Evento: {
                title: 'Tipo Evento',
                options: {
                    'Conferencia':'Conferencia',
                    'Congreso':'Congreso',
                    'Jornada':'Jornada',
                    'Panel':'Panel',
                    'Pasantia':'Pasantia',
                    'Seminario':'Seminario',
                    'Taller':'Taller',
                    'Vista de Observación':'Vista de Observación'
                }
            },

            Nombre_Evento: {
                title: 'Nombre Evento'
            },

            Tipo_Certificado: {
                title: 'Tipo Certificado',
                options: {
                    'Aprobación':'Aprobación',
                    'Asistencia':'Asistencia'
                }
            },
            Area_Estudios: {
                title: 'Area Estudios',
                options:{
                    'Administración/oficina':'Administración/Oficina',
                    'Agricultura/Pesca/Ganadería':'Agricultura/Pesca/Ganadería',
                    'Arte/Diseño/Medios':'Arte/Diseño/Medios',
                    'Científico/Investigación':'Científico/Investigación',
                    'Dirección/Gerencia':'Dirección/Gerencia',
                    'Economía/Contabilidad':'Economía/Contabilidad',
                    'Educación Básica/Cursos':'Educación Básica/Cursos',
                    'Educación/Universidad':'Educación/Universidad',
                    'Entretenimiento/Deportes':'Entretenimiento/Deportes',
                    'Fabricación':'Fabricación',
                    'Finanzas/Banca':'Finanzas/Banca',
                    'Gobierno':'Gobierno',
                    'Hotelería/Turismo':'Hotelería/Turismo',
                    'Infomática/Hardware':'Infomática/Hardware',
                    'Infomática/Software':'Infomática/Software',
                    'Infomática/Telecomunicaciones':'Infomática/Telecomunicaciones',
                    'Ingeniería/Técnico':'Ingeniería/Técnico',
                    'Internet':'Internet',
                    'Legal/Asesoría':'Legal/Asesoría',
                    'Marketing/Ventas':'Marketing/Ventas',
                    'Materia Prima':'Materia Prima',
                    'Medicina/Salud':'Medicina/Salud',
                    'Recursos Humanos/Personal':'Recursos Humanos/Personal',
                    'Sin Área de Estudio':'Sin Área de Estudio',
                    'Ventas al Consumidor':'Ventas al Consumidor'
                }

            },
            Fecha_Desde: {
                title: 'Fecha Desde',
                type:'date',
                displayFormat: 'dd/mm/yy',
                width:'7%'
            },
            Fecha_Hasta: {
                title: 'Fecha Hasta',
                type:'date',
                displayFormat: 'dd/mm/yy',
                width:'6%'

            },
            Dias: {
                title: 'Días',
                width:'1%'
            },
            Horas:{
                title:'Horas',
                width:'1%'
            }

        }
    });
    $('#tblCapacitaciones').jtable('load');

});
