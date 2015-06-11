/**
 * Created by Lenin on 05/08/2014.
 */
$(function () {
    jQuery.fn.asError = function() {
        return this.each(function() {
            $(this).replaceWith(function(i, html) {
                var newHtml = "<div class='ui-state-error ui-corner-all' style='padding: 0 .7em;'>";
                newHtml += "<p><span class='ui-icon ui-icon-alert' style='float: left; margin-right: .3em;'>";
                newHtml += "</span><strong>Error: </strong>";
                newHtml += html;
                newHtml += "</p></div>";
                return newHtml;
            });
        });
    };

    jQuery.fn.asHighlight = function() {
        return this.each(function() {
            $(this).replaceWith(function(i, html) {
                var newHtml = "<div class='ui-state-highlight ui-corner-all' style='padding: 0 .7em;'>";
                newHtml += "<p><span class='ui-icon ui-icon-info' style='float: left; margin-right: .3em;'>";
                newHtml += "</span>";
                newHtml += html;
                newHtml += "</p></div>";
                return newHtml;
            });
        });
    };

    $.AJAX = function(url, data, funcion, async){
        $.ajax({
            async:async,
            dataType:"json",
            type: 'POST',
            url: url,
            data: data,
            success:  function(respuesta){
                funcion(respuesta);
            }
        });
    };

    $.datepicker.regional['es'] = {
        closeText: 'Cerrar',
        prevText: '<Ant',
        nextText: 'Sig>',
        currentText: 'Hoy',
        monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        monthNamesShort: ['Ene','Feb','Mar','Abr', 'May','Jun','Jul','Ago','Sep', 'Oct','Nov','Dic'],
        dayNames: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
        dayNamesShort: ['Dom','Lun','Mar','Mié','Juv','Vie','Sáb'],
        dayNamesMin: ['Do','Lu','Ma','Mi','Ju','Vi','Sá'],
        weekHeader: 'Sm',
        dateFormat: 'dd/mm/yy',
        firstDay: 1,
        isRTL: false,
        showMonthAfterYear: false,
        yearSuffix: '',
        changeMonth: true,
        changeYear: true
    };
    $.datepicker.setDefaults($.datepicker.regional['es']);

});
