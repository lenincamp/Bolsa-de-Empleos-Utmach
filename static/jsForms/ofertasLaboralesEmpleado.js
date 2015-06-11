/**
 * Created by Lenin on 23/08/2014.
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
    $("#img").tooltip();
    $("#imgAplicar").tooltip();
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

    $.cmbAreaTrabajo = function (respuesta) {
        var cmbAreaLaboral = $("#cmbAreaEstudios")
        var option = ""
        $.each(respuesta.Options, function(i, item) {
            option += "<option value="+item.Value+">"+item.DisplayText+"</option>";
        });
        cmbAreaLaboral.html(option);

    }
    $.AJAX('/principalEmpleado/hojaVida/experiencia/cmbAreaTrabajo/', "", $.cmbAreaTrabajo)
    /*===Cargar Datos Oferta===*/
    $.cargaDatosOferta = function (respuesta) {
        $("#frmPublicacionEmpleo input").attr("readonly",true)
        $("#frmPublicacionEmpleo select").attr("disabled",true)
        $("#txtCargoSolicitado").val(respuesta.ofertas[0].Cargo_Solicitado);
        $("#cmbTipoContrato").val(respuesta.ofertas[0].Tipo_Contrato);
        $("#cmbRelacionLaboral").val(respuesta.ofertas[0].Relacion_Laboral);
        $("#txtCorreo").val(respuesta.ofertas[0].Correo);
        $("#txtFechaInicio").val(respuesta.ofertas[0].Fecha_inicio);
        $("#txtFechaFin").val(respuesta.ofertas[0].Fecha_fin);
        $("#txtContacto").val(respuesta.ofertas[0].Contacto);
        $("#txtTelefono").val(respuesta.ofertas[0].Telefono);
        $("#txtFax").val(respuesta.ofertas[0].Fax);
        $("#txtCelular").val(respuesta.ofertas[0].Celular);
        $("#cmbInstruccion").val(respuesta.perfil[0].Instruccion);
        $("#cmbRemuneracion").val(respuesta.perfil[0].Remuneracion);
        $("#cmbAreaEstudios").val(respuesta.perfil[0].Area_Estudio);
        $("#txtExperienciaMinima").val(respuesta.perfil[0].Experiencia_minima);
        $("#txtExperienciaMaxima").val(respuesta.perfil[0].Experiencia_maxima);
        $("#txtConocimientosCargo").val(respuesta.perfil[0].Conocimientos_cargo);
        $("#txtActividadesDesem").val(respuesta.perfil[0].Actividades_Desem);
        $("#cmbCapacitacion").val(respuesta.perfil[0].Capacitacion);
        $("#cmbJornadasTrabajo").val(respuesta.perfil[0].Jornadas_Trabajo);
        $("#txtInforAd").val(respuesta.perfil[0].Informacion_Adicional);
        $("#txtNumeroCargos").val(respuesta.ofertas[0].Numero_Cargos);
        $("input:radio[value='"+respuesta.ofertas[0].Discapacidad+"']").prop('checked', true);




    }
    $.AJAX("/principalEmpleado/ofertasLaborales/cargarDatosOferta/","", $.cargaDatosOferta)

    $.aplicarOferta= function (respuesta) {
        if(respuesta.ok){
            alert("Aplicación Exitosa");
        }
        if (respuesta.error){
            alert("Ud ya aplico para el empleo");
        }
    }

    $("#imgAplicar").click(function () {
        $.AJAX("/principalEmpleado/ofertasLaborales/aplicarOferta/","", $.aplicarOferta)
    })

});
