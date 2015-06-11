/**
 * Created by Lenin on 21/08/2014.
 */

$(function () {
    var dlg = $("#formDialogCambioClave");
    dlg.dialog({
        show: {effect: 'blind', duration: 350, /* SPECIF ARGUMENT */ times: 3},
        hide: {effect: 'blind', duration: 350, /* SPECIF ARGUMENT */ times: 3},
        autoOpen: false,
        modal:true
    });

    $("#btnCambioClave").button();

    dlg.submit(function(){
        if($("#txtClave1").val()==$("#txtClave2").val()){
            $.AJAX("/principalEmpleado/cambioClave/",$("#formDialogCambioClave").serialize(),$.cambiaClave);
        }
        return false;
    });

    $.cambiaClave = function (respuesta) {
        if(respuesta.ok){
            dlg.dialog('close');
        }
    };

    $('#cambioClave').click(function() {
        dlg.dialog('open');
    });

    $("#btnBuscar").tooltip();
    $( "#txtFechaDesde" ).datepicker({});
    $( "#txtFechaHasta" ).datepicker({});

    $.cmbAreaTrabajo = function (respuesta) {
        var cmbAreaLaboral = $("#cmbAreaLaboral")
        var option = ""
        $.each(respuesta.Options, function(i, item) {
            option += "<option value="+item.Value+">"+item.DisplayText+"</option>";
        });
        cmbAreaLaboral.html(option);

    }
    $.AJAX('/principalEmpleado/hojaVida/experiencia/cmbAreaTrabajo/', "", $.cmbAreaTrabajo)

    /*=====Cargan Ofertas=====*/
    $.paginaOfertas = function (respuesta) {
        var content = $("#content")
        var contenido = ""
        $.each(respuesta.ofertas, function(i, item) {
            contenido+="<li><h5>"+item.id_Oferta__Cargo_Solicitado+"</h5><span>OFERTA-"+item.id_Oferta__Num_Oferta+"</span><p>Remuneración: "+item.Remuneracion+"</p><a id='"+item.id_Oferta_id+"' href='/principalEmpleado/ofertasLaborales/cargarOferta/?idOferta="+$(this).attr('id')+"'> Ver Oferta >></a></li>"
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
    $.AJAX('/principalEmpleado/ofertasLaborales/ofertas/', "", $.paginaOfertas)

    $("#btnBuscar").click(function () {
        $.AJAX('/principalEmpleado/ofertasLaborales/filtroOfertas/', $("#frmOfertasLaborales").serialize(), $.paginaOfertas)
    });

})
