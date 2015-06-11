/**
 * Created by Lenin on 23/08/2014.
 */
$(function () {
    $.paginaOfertas = function (respuesta) {
        var content = $("#content")
        var contenido = ""
        $.each(respuesta.empleados, function(i, item) {
            contenido+="<li><h5 style='font-size:14px; width:50%;float:left;'>"+item.Nombre+" "+ item.Apellido+"</h5><a id='"+item.id+"' href='/principalEmpleado/curriculo/?emp="+$(this).attr('id')+"'> Curriculum Vitae >></a></li>"
        });
        content.html(contenido)
        $("div.holder").jPages({
            containerID : "content",
            perPage: 5,
            first       : "Inicio",
            previous    : "Atras",
            next        : "Siguiente",
            last        : "Fin"
        });
    }
    $.AJAX('/principalEmpleador/ofertasLaborales/aplicadas/', "", $.paginaOfertas)
});
