/**
 * Created by Lenin on 21/08/2014.
 */
/**
 * Created by Lenin on 12/08/2014.
 */
$(function () {

    $('#tblInstruccionFormal').jtable({
        title: 'Instrucción Formal',
        actions: {
            listAction: "/principalEmpleado/hojaVida/instruccionFormal/list/",
            createAction: "/principalEmpleado/hojaVida/instruccionFormal/add/",
            updateAction: '/principalEmpleado/hojaVida/instruccionFormal/edit/',
            deleteAction: '/principalEmpleado/hojaVida/instruccionFormal/del/'
        },
        fields: {
            id: {
                key: true,
                list: false
            },
            Nivel_Instruccion: {
                title: 'Nivel Instrucción:',
                options: {
                    'Sin Estudios':'Sin Estudios',
                    'Primaria': 'Primaria',
                    'Secundaria':'Secundaria',
                    'Egresado':'Egresado',
                    'Tercel Nivel':'Tercer Nivel',
                    'Cuarto Nivel':'Cuarto Nivel'
                }

            },
            Institucion: {
                title: 'Institución:'
            },

            Titulo_Obtenido: {
                title: 'Título Obtenido:'
            },

            Registro_Senescyt: {
                title: 'Nro del Registro Senescyt:'
            }
        }
    });
    $('#tblInstruccionFormal').jtable('load');

});
