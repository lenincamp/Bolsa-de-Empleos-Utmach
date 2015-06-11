/**
 * Created by Lenin on 06/08/2014.
 */
$(function() {
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
   //$("#informacionPersonal :input[type='textarea']").removeClass('contact_form textarea');
    $("#btnRegistro").tooltip();
    $( "#txtFechaNacimiento" ).datepicker({
        /*changeMonth: true,
        changeYear: true*/
    });

    $("#txtFechaNacimiento").change(function () {
        var today = new Date();
        var birthDate = new Date($("#txtFechaNacimiento").datepicker("getDate"));
        var age = today.getFullYear() - birthDate.getFullYear();
        var m = today.getMonth() - birthDate.getMonth();
        if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
            age--;
        }
        $("#txtEdad").val(age);
    });


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
    /*==========================================*/
    $.cargarDatosEmpleado = function (respuesta) {
        $("#txtCedula").val(respuesta.datosEmpleado.CedulaRuc);
        $("#txtNombres").val(respuesta.datosEmpleado.Nombre);
        $("#txtApellidos").val(respuesta.datosEmpleado.Apellido);
        $("#txtApellidos").val(respuesta.datosEmpleado.Apellido);
        $("#txtEmail").val(respuesta.datosEmpleado.Correo);
        $("#txtEmail").val(respuesta.datosEmpleado.Correo);
        $("#txtTelefono1").val(respuesta.datosEmpleado.Telefono1);
        $("#txtTelefono2").val(respuesta.datosEmpleado.Telefono2);
        var fecha_nacimiento = $.datepicker.formatDate( "dd/mm/yy", new Date(respuesta.datosEmpleado.Fecha_Nacimiento));
        $("#txtFechaNacimiento").val(fecha_nacimiento).change();
        $("#cmbEtnia").val(respuesta.datosEmpleado.Etnia||1);
        $("#cmbEstadoCivil").val(respuesta.datosEmpleado.Estado_Civil||1);
        $("#cmbEstadoLaboral").val(respuesta.datosEmpleado.Estado_Laboral||"D");
        $("#cmbSexo").val(respuesta.datosEmpleado.Sexo||"m");
        $("#cmbTipoSangre").val(respuesta.datosEmpleado.Tipo_Sangre||1);
        //console.log(respuesta.direction);
        $("#txtCallePrincipal").val(respuesta.direccion.Calle_Principal);
        $("#txtCalleSecundaria").val(respuesta.direccion.Calle_Secundaria);
        $("#txtNumero").val(respuesta.direccion.Numero);
        $("#cmbProvincia").val(respuesta.idProvincia).change();
        $("#cmbCiudad").val(respuesta.direccion.id_ciudad_id);
        $("#cmbSector").val(respuesta.direccion.Sector);
        $("#txtReferencia").val(respuesta.direccion.Referencia);
        $("input[name='rBtnDiscapacidad'][value='"+respuesta.datosEspeciales.Discapacidad+"']").attr('checked', true);
        $("input[name='rBtnEnfermedadCatastrofica'][value='"+respuesta.datosEspeciales.Enf_Catastrofica+"']").attr('checked', true);
        $("input[name='rBtnCargoFamiliarDiscapacidad'][value='"+respuesta.datosEspeciales.Fam_enf_Severa+"']").attr('checked', true);
        $("input[name='rBtnCargoFamiliarCatastrofica'][value='"+respuesta.datosEspeciales.Fam_enf_Catastrofica+"']").attr('checked', true);
    }
    $.AJAX("/principalEmpleado/hojaVida/informacionPersonal/CargarDatosEmpleado/", "", $.cargarDatosEmpleado);
    /*======================================*/
    $.guardarDatosEmpleado = function (respuesta) {
        if(respuesta.ok){
            $("#contenidoAjax").dialog('close');
        }
    }
    $("#btnRegistro").click(function () {
        var $contenidoAjax = $('div#contenidoAjax').html('<img style="width:100%;height:100%;"src="../../../static/css/images/loading.gif" />');
        $contenidoAjax.dialog('open');
        $.AJAX("/principalEmpleado/hojaVida/informacionPersonal/GuardarDatosEmpleado/",$("#informacionPersonal").serialize(), $.guardarDatosEmpleado);
    });
});

