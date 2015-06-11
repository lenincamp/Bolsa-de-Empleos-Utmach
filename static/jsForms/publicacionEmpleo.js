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
    $("#btnGuardar").tooltip();
    $("#txtFechaInicio").datepicker({});
    $("#txtFechaFin").datepicker({});
    var contenidoAjax = $('div#contenidoAjax')
    $.guardaDatosPublicacion = function (respuesta) {
        if (respuesta.ok){
            contenidoAjax.dialog('close');
            $("#frmPublicacionEmpleo input").val("");
        }

    }

    $("#btnGuardar").click(function () {
        if ($("#txtNumeroCargos").val()!=''){
            contenidoAjax.html('<img style="width:100%;height:100%;"src="../../../static/css/images/loading.gif" />');
            contenidoAjax.dialog('open');
            $.AJAX("/principalEmpleador/publicacionEmpleo/guardar/",$("#frmPublicacionEmpleo").serialize(), $.guardaDatosPublicacion, false);
        }
        else{
            alert("ingrese el numero de cargos disponibles")
        }

    });

    $.cmbAreaTrabajo = function (respuesta) {
        var cmbAreaLaboral = $("#cmbAreaEstudios")
        var option = ""
        $.each(respuesta.Options, function(i, item) {
            option += "<option value="+item.Value+">"+item.DisplayText+"</option>";
        });
        cmbAreaLaboral.html(option);

    }
    $.AJAX('/principalEmpleado/hojaVida/experiencia/cmbAreaTrabajo/', "", $.cmbAreaTrabajo)
})
