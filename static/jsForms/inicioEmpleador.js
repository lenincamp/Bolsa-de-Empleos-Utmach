$(function () {
    $("#inicioPagina").prop("href","/principalEmpleador/");
    $("#inicioPagina1").prop("href","/principalEmpleador/");
    var dlg = $("#formDialogCambioClave");
    dlg.dialog({
        show: {effect: 'blind', duration: 350, /* SPECIF ARGUMENT */ times: 3},
        hide: {effect: 'blind', duration: 350, /* SPECIF ARGUMENT */ times: 3},
        autoOpen: false,
        modal: true
    });

    $("#btnCambioClave").button();

    dlg.submit(function () {
        if ($("#txtClave1").val() == $("#txtClave2").val()) {
            $.AJAX("/principalEmpleador/cambioClave/", $("#formDialogCambioClave").serialize(), $.cambiaClave);
        }
        return false;
    });

    $.cambiaClave = function (respuesta) {
        if (respuesta.ok) {
            dlg.dialog('close');
        }
    };

    $('#cambioClave').click(function () {
        dlg.dialog('open');
    });




});