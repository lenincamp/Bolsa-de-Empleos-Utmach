/**
 * Created by Lenin on 05/08/2014.
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

     /*========ACCIONES MENU HOJA VIDA=========*/
     $("#informacionPersonal").click(function () {
         $("#cargaMenuHojaVida").attr({"src":"/principalEmpleado/hojaVida/informacionPersonal/","style":"width: 100%;min-height: 475px;height:auto;border: 0;",scrolling:"yes"});
     });

     $("#preferenciasLaborales").click(function () {
         $("#cargaMenuHojaVida").attr({"src":"/principalEmpleado/hojaVida/preferenciasLaborales/","style":"min-height:295px;width:100%;",scrolling:"yes"});
     });

     $("#idiomas").click(function () {
         $("#cargaMenuHojaVida").attr({"src":"/principalEmpleado/hojaVida/idiomas/","style":"min-height:295px;width:100%;",scrolling:"yes"});
     });

     $("#oficiosSubactividades").click(function () {
         $("#cargaMenuHojaVida").attr({"src":"/principalEmpleado/hojaVida/oficiosSubactividades/","style":"min-height:295px;width:100%;",scrolling:"yes"});
     });

     $("#logrosPersonales").click(function () {
         $("#cargaMenuHojaVida").attr({"src":"/principalEmpleado/hojaVida/logros/","style":"min-height:295px;width:100%;",scrolling:"yes"});
     });

     $("#referenciasPersonales").click(function () {
         $("#cargaMenuHojaVida").attr({"src":"/principalEmpleado/hojaVida/referenciasPersonales/","style":"width: 100%;min-height: 475px;",scrolling:"no"});
     });

     $("#experiencia").click(function () {
         $("#cargaMenuHojaVida").attr({"src":"/principalEmpleado/hojaVida/experiencia/","style":"width: 100%;min-height: 475px;",scrolling:"yes"});
     });

     $("#capacitaciones").click(function () {
         $("#cargaMenuHojaVida").attr({"src":"/principalEmpleado/hojaVida/capacitaciones/","style":"width: 100%;min-height: 475px;",scrolling:"yes"});
     });

     $("#instruccionFormal").click(function () {
         $("#cargaMenuHojaVida").attr({"src":"/principalEmpleado/hojaVida/instruccionFormal/","style":"width: 100%;min-height: 475px;",scrolling:"yes"});
     });
 });

