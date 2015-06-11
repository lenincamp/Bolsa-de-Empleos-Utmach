/**
 * Created by Lenin on 13/08/2014.
 */
/**
 * Created by Lenin on 12/08/2014.
 */
$(function () {

    $('#tblLogros').jtable({
        title: 'Logros Personales',
        actions: {
            listAction: "/principalEmpleado/hojaVida/logros/list/",
            createAction: "/principalEmpleado/hojaVida/logros/add/",
            updateAction: '/principalEmpleado/hojaVida/logros/edit/',
            deleteAction: '/principalEmpleado/hojaVida/logros/del/'
        },
        fields: {
            id: {
                key: true,
                list: false
            },
            Tipo_Logro: {
                title: 'Tipo de Logro: ',
                width: '20%',
                options: {
                    'Academico' : 'Academico',
                    'Artisticos': 'Artisticos',
                    'Deportivo' : 'Deportivo',
                    'Laboral'   : 'Laboral'
                }

            },
            Descripcion:{
                title:'Descripción',
                width: '40%',
                type:'textarea'
            }
        }
    });
    $('#tblLogros').jtable('load');

});

