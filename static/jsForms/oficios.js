/**
 * Created by Lenin on 13/08/2014.
 */
/**
 * Created by Lenin on 12/08/2014.
 */
$(function () {

    $('#tblOficios').jtable({
        title: 'Oficios / Sub Actividades',
        actions: {
            listAction: "/principalEmpleado/hojaVida/oficiosSubactividades/list/",
            createAction: "/principalEmpleado/hojaVida/oficiosSubactividades/add/",
            updateAction: '/principalEmpleado/hojaVida/oficiosSubactividades/edit/',
            deleteAction: '/principalEmpleado/hojaVida/oficiosSubactividades/del/'
        },
        fields: {
            id: {
                key: true,
                list: false
            },
            id_oficio__Nombre: {
                title: 'Oficio: ',
                width: '20%',
                options: '/principalEmpleado/hojaVida/oficiosSubactividades/cmbOficios/'

            },
            Descripcion:{
                title:'Descripción',
                width: '40%',
                type:'textarea'
            }
        }
    });
    $('#tblOficios').jtable('load');

});

