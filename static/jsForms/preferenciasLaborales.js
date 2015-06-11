/**
 * Created by Lenin on 10/08/2014.
 */
$(function () {
    $("#contenidoAjax").dialog({
        title:"Cargando....",
        dialogClass: "no-close",
        resizable:false,
        width:50,
        height:80,
        autoOpen: false,
        modal: true,
        show: function() {$(this).fadeIn(300);},
        hide: function() {$(this).fadeOut(300);}
    });
    var btn =  $("#btnGuardarPreferenciasLaborales")
    btn.tooltip();

    $.cargaCiudadEmpleado = function (respuesta) {
        $("#cmbProvincia").val(respuesta.idProvincia).change();
        $("#cmbCiudad").val(respuesta.idCiudad);
    }

    $("#chBtnMismoLugarResidencia").change( function(){
        if($(this).is(':checked')) {
            $("tr[class='trOculta']").fadeIn(300);

        } else {
            $("tr[class='trOculta']").fadeOut(300);
            $.AJAX("/principalEmpleado/hojaVida/preferenciasLaborales/cargarCiudad/","", $.cargaCiudadEmpleado)
        }

    });
    /*========================================*/
    $("#cmbProvincia").change(function(){
        $.CmbCiudad($(this).val());
    });

    $.cargarCmbProvincia=function(respuesta){
        var cmbProvincias = $("#cmbProvincia")
        var option = ""
        $.each(respuesta, function(i, item) {
            option += "<option value="+item.idProvincia+">"+item.NombreP+"</option>";
        });
        cmbProvincias.html(option);
        $.CmbCiudad(respuesta[0].idProvincia);
    }

    $.CmbCiudad = function(idProvincia){
        $.AJAX("/inicio/CmbCiudades/",{"idP":idProvincia}, $.cargarCmbCiudad, false);
    };
    $.cargarCmbCiudad =  function(respuesta){
        var cmbCiudades = $("#cmbCiudad")
        var option = ""
        $.each(respuesta, function(i, item) {
            option += "<option value="+item.idCiudad+">"+item.NombreC+"</option>";
        });
        cmbCiudades.html(option);
    };
    $.AJAX("/inicio/CmbProvincias/","", $.cargarCmbProvincia, false);
    /*===========================================*/

    $.cargarPreferenciasLaborales = function (respuesta) {
        console.log(respuesta);
        $("input[name='rBtnSectorPublico'][value='"+respuesta.preferencias.Sector_Publico+"']").attr('checked', true);
        $("input[name='rBtnSectorPrivado'][value='"+respuesta.preferencias.Sector_Privado+"']").attr('checked', true);
        $("#cmbAspiracionSalarial").val(respuesta.preferencias.Aspiracion_Salarial);
        $("#chBtnMismoLugarResidencia").prop("checked", respuesta.preferencias.Lugar_Residencia).change()
        $("#cmbProvincia").val(respuesta.idProvincia).change();
        $("#cmbCiudad").val(respuesta.detallePreferencia.ciudad_id);
    }
    $.AJAX("/principalEmpleado/hojaVida/CargarPreferenciasLaborales/", "", $.cargarPreferenciasLaborales);
    /*======================================*/
    $.guardarPreferenciasLaborales= function (respuesta) {
        if(respuesta.ok){
            $("#contenidoAjax").dialog('close');
        }
    }
    $("#btnGuardar").click(function () {
        var $contenidoAjax = $('div#contenidoAjax').html('<img style="width:100%;height:100%;"src="../../../static/css/images/loading.gif" />');
        $contenidoAjax.dialog('open');
        $.AJAX("/principalEmpleado/hojaVida/GuardarPreferenciasLaborales/?chBtnMismoLugarResidencia="+($('#chBtnMismoLugarResidencia:checked').val()||false), $("#preferenciasLaborales").serialize(), $.guardarPreferenciasLaborales);
    })

})
