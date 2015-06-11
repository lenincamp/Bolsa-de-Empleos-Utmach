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



    $.cargarReferenciasLaborales = function (respuesta) {
        if(!respuesta.primeraVez){
            for (var i=0; i<=2; i++){
                $("#txtNombres"+i).val(respuesta.referencias[i].Nombres);
                $("#txtApellidos"+i).val(respuesta.referencias[i].Apellidos);
                $("#txtTelefono"+i).val(respuesta.referencias[i].Telefono);
                $("#txtEmail"+i).val(respuesta.referencias[i].Correo);
            }


        }

    }
    $.AJAX("/principalEmpleado/hojaVida/CargarReferenciasPersonales/", "", $.cargarReferenciasLaborales);
    /*======================================*/
    $.guardarReferenciasLaborales= function (respuesta) {
        if(respuesta.ok){
            $("#contenidoAjax").dialog('close');
        }
    }

    $("#btnGuardar").click(function () {
        var $contenidoAjax = $('div#contenidoAjax').html('<img style="width:100%;height:100%;"src="../../../static/css/images/loading.gif" />');
        $contenidoAjax.dialog('open');
        $.AJAX("/principalEmpleado/hojaVida/GuardarReferenciasPersonales/", $("#referenciasLaborales").serialize(), $.guardarReferenciasLaborales);
    })

})
