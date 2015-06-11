/**
 * Created by Lenin on 03/08/2014.
 */
$(function () {
    var invialido=0;
    $("#formDialog").dialog({
        autoOpen: false,
        modal: true,
         show: function() {$(this).fadeIn(300);},
         hide: function() {$(this).fadeOut(300);}
	});
    $("#registroEmpleador").dialog({
        autoOpen: false,
        modal: true,
         show: function() {$(this).fadeIn(300);},
         hide: function() {$(this).fadeOut(300);}
    });

    $("#txtCedulaEmpleador").validarCedulaEC({
        strict: true,
        events: "change",
        //the_classes: "invalid",
        onValid: function () {
            $("#error-empleador").html("");
            //$('<p>').text('Cédula Valida').appendTo('#error-list').asHighlight();
            invalido = 0;
        },
        onInvalid: function () {
            invalido = 1;
            $("#error-empleador").html("");
            $('<p>').text('Cédula Invalida').appendTo('#error-empleador').asError();
        }
    });

    $("#btnGuardarRegistroEmpleador").button();
    $("#btnCancelarRegistroEmpleador").button().on('click',function(){
        $("#registroEmpleador").dialog("close");
        $("#registroEmpleador").form().reset();
        return false;
    });

    $.registroEmpleador = function(respuesta){
        if(respuesta.ok){
            invalido=0;
            $("#error-empleador").html("");
            $('<p>').text('El Usuario Ya Existe').appendTo('#error-empleador').asHighlight();
            $("#registroEmpleador").dialog("close");
        }
        if(respuesta.error){
            invialido = 1;
            $("#error-empleador").html("");
            $('<p>').text('El Usuario Ya Existe').appendTo('#error-empleador').asError();
            //$("#formDialog").dialog("close");
        }

    };

    $("#registroEmpleador").submit(function () {
        var data = $("#registroEmpleador").serialize();
        if (invalido == 0){
            $.AJAX("/inicio/registroEmpleador/",data, $.registroEmpleador);
        }
        return false;
    });

    $("#btnRegistroEmpleador").click(function () {
        $.AJAX("/inicio/CmbProvincias/","", $.cargarCmbProvincia);
        $("#registroEmpleador").dialog("option", "width", 730);
        //$("#formDialog").dialog("option", "height", 600);
        $("#registroEmpleador").dialog("option", "resizable", false);
        $("#registroEmpleador").dialog("open");
        return false;
    });

    $("#txtCedulaLogin").validarCedulaEC({
        strict: true,
        events: "change",
        //the_classes: "invalid",

        onValid: function () {
            $("#error-login").html("");
            //$('<p>').text('Cédula Valida').appendTo('#error-login').asHighlight();
        },
        onInvalid: function () {
            $("#error-login").html("");
            if($("#txtCedulaLogin").val()!=""){
                $('<p>').text('Cédula Invalida').appendTo('#error-login').asError();
            }

        }
    });

    $("#txtCedulaELogin").validarCedulaEC({
        strict: true,
        events: "change",
        //the_classes: "invalid",

        onValid: function () {
            $("#error-loginE").html("");
            //$('<p>').text('Cédula Valida').appendTo('#error-login').asHighlight();
        },
        onInvalid: function () {
            $("#error-loginE").html("");
            if($("#txtCedulaELogin").val()!=""){
                $('<p>').text('Cédula Invalida').appendTo('#error-loginE').asError();
            }

        }
    });


    $("#txtCedula").validarCedulaEC({
        strict: true,
        events: "change",
        //the_classes: "invalid",
        onValid: function () {
            $("#error-list").html("");
            //$('<p>').text('Cédula Valida').appendTo('#error-list').asHighlight();
            invalido = 0;
          },
          onInvalid: function () {
              invalido = 1;
              $("#error-list").html("");
              $('<p>').text('Cédula Invalida').appendTo('#error-list').asError();
          }
    });

    $("#formDialog").submit(function () {

        var data = $("#formDialog").serialize();
        if (invalido == 0){
            $.AJAX("/inicio/Registro/",data, $.registroEmpleado);
        }
        return false;
    });

    $("#btnRegistro").button();
    $("#btnCancelarRegistro").button().on('click',function(){
        $("#formDialog").dialog("close");
        $("#formDialog").form().reset();
        return false;
    });

    $( "#txtFechaNacimiento" ).datepicker({
        changeMonth: true,
        changeYear: true
    });

    $.registroEmpleado = function(respuesta){
        if(respuesta.ok){
            invalido=0;
            $("#error-list").html("");
            $('<p>').text('El Usuario Ya Existe').appendTo('#error-list').asHighlight();
            $("#formDialog").dialog("close");
        }
        if(respuesta.error){
            invialido = 1;
            $("#error-list").html("");
            $('<p>').text('El Usuario Ya Existe').appendTo('#error-list').asError();
            //$("#formDialog").dialog("close");
        }

    };

	$("#frmEmpleados").click(function () {
        $.AJAX("/inicio/CmbProvincias/","", $.cargarCmbProvincia);
		$("#formDialog").dialog("option", "width", 730);
		//$("#formDialog").dialog("option", "height", 600);
		$("#formDialog").dialog("option", "resizable", false);
		$("#formDialog").dialog("open");
		return false;
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
        $.AJAX("/inicio/CmbCiudades/",{"idP":idProvincia}, $.cargarCmbCiudad);
    };
    $.cargarCmbCiudad =  function(respuesta){
         var cmbCiudades = $("#cmbCiudad")
         var option = ""
         $.each(respuesta, function(i, item) {
            option += "<option value="+item.idCiudad+">"+item.NombreC+"</option>";
         });
         cmbCiudades.html(option);
    };
    $("#frmLoginEmpleados").submit(function () {
        $.AJAX('/inicio/login/',$("#frmLoginEmpleados").serialize(), $.frmLoginEmpleados)
        return false;
    });
    $.frmLoginEmpleados = function (respuesta) {

        if(respuesta.url){
            $(location).attr('href',"/principalEmpleado/");
        }
        if(respuesta.error){
            alert(respuesta.error);
        }
    }

    $("#frmLoginEmpleador").submit(function () {
        $.AJAX('/inicio/loginEmpleador/',$("#frmLoginEmpleador").serialize(), $.frmLoginEmpleador)
        return false;
    });
    $.frmLoginEmpleador = function (respuesta) {

        if(respuesta.url){
            $(location).attr('href',"/principalEmpleador/");
        }
        if(respuesta.error){
            alert(respuesta.error);
        }
    }


});
