/**
 * Created by Lenin on 12/08/2014.
 */
$(function () {

    $('#tblIdiomas').jtable({
        title: 'Idiomas',
        actions: {
            listAction: "/principalEmpleado/hojaVida/idiomas/list/",
            createAction: "/principalEmpleado/hojaVida/idiomas/add/",
            updateAction: '/principalEmpleado/hojaVida/idiomas/edit/',
            deleteAction: '/principalEmpleado/hojaVida/idiomas/del/'
        },
        fields: {
            id: {
                key: true,
                list: false
            },
            Idioma: {
                title: 'Idiomas: ',
                width: '40%',
                options: {
                    'Achuar'    : 'Achuar',
                    'Alemán'    : 'Alemán',
                    'Árabe'     : 'Árabe',
                    'Chino'     : 'Chino',
                    'Español'   : 'Español',
                    'Fránces'   : 'Fránces',
                    'Griego'    : 'Griego',
                    'Hebreo'    : 'Hebreo',
                    'Inglés'    : 'Inglés',
                    'Italiano'  : 'Italiano',
                    'Japonés'   : 'Japonés',
                    'Kichua'    : 'Kichua',
                    'Letón'     : 'Letón',
                    'Lituano'   : 'Lituano',
                    'Maltés'    : 'Maltés',
                    'Neerlandés': 'Neerlandés',
                    'Noruego'   : 'Noruego',
                    'Polaco'    : 'Polaco',
                    'Portugués' : 'Portugués'
                }
            },
            Nivel_hablado: {
                title: 'Nivel Hablado: ',
                width: '20%',
                options:{
                    'Básico'     :'Básico',
                    'Intermedio' : 'Intermedio',
                    'Avanzado'   : 'Avanzado',
                    'Nativo'     : 'Nativo'
                }
            },
            Nivel_escrito: {
                title: 'Nivel Escrito: ',
                width: '30%',
                options:{
                    'Básico'     :'Básico',
                    'Intermedio' : 'Intermedio',
                    'Avanzado'   : 'Avanzado',
                    'Nativo'     : 'Nativo'
                }
            }
        }
    });
    $('#tblIdiomas').jtable('load');

});
