/**
 * Created by Lenin on 23/08/2014.
 */
$(function () {
    $.paginaOfertas = function (respuesta) {
        var content = $("#content")
        var contenido = ""
        $.each(respuesta.ofertas, function(i, item) {
            contenido+="<li><h5>"+item.id_Oferta__Cargo_Solicitado+"</h5><span>OFERTA-"+item.id_Oferta__Num_Oferta+"</span><p>Remuneración: "+item.Remuneracion+"</p><a id='"+item.id_Oferta_id+"' href='/principalEmpleador/ofertasLaborales/aplicaciones/?idOferta="+$(this).attr('id')+"'> Ver Aplicaciones >></a></li>"
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
    $.AJAX('/principalEmpleador/ofertasLaborales/ofertas/', "", $.paginaOfertas)
})