from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

"""Principal y Empleado"""
urlpatterns = patterns('principal.views',
    url(r'^$', 'cargaPagina',{"template":"index.html"}),
    url(r'^inicio/CmbProvincias/$', 'CmbProvincias'),
    url(r'^inicio/CmbCiudades/$', 'CmbCiudades'),
    url(r'^inicio/Registro/$', 'frmRegistro'),

    url(r'^inicio/login/$', 'login'),
    url(r'^principalEmpleado/$', 'principalEmpleado',{"template":"inicioEmpleado.html"}),
    url(r'^principalEmpleado/hojaVida/$', 'principalEmpleado',{"template":"baseHojaVida.html"}),

    url(r'^principalEmpleado/hojaVida/informacionPersonal/$', 'cargaPagina',{"template":"informacionPersonal.html"}),
    url(r'^principalEmpleado/hojaVida/informacionPersonal/CargarDatosEmpleado/$', 'informacionPersonal'),
    url(r'^principalEmpleado/hojaVida/informacionPersonal/GuardarDatosEmpleado/$', 'guardarDatosEmpleado'),

    url(r'^principalEmpleado/hojaVida/preferenciasLaborales/$', 'cargaPagina',{"template":"preferenciasLaborales.html"}),
    url(r'^principalEmpleado/hojaVida/CargarPreferenciasLaborales/$', 'cargarPreferenciasLaborales'),
    url(r'^principalEmpleado/hojaVida/GuardarPreferenciasLaborales/$', 'guardarPreferenciasLaborales'),
    url(r'^principalEmpleado/hojaVida/preferenciasLaborales/cargarCiudad/$', 'cargarCiudad'),

    url(r'^principalEmpleado/hojaVida/idiomas/$', 'cargaPagina',{"template":"idiomas.html"}),
    url(r'^principalEmpleado/hojaVida/idiomas/list/$', 'idiomas',{'accion':'list'}),
    url(r'^principalEmpleado/hojaVida/idiomas/add/$', 'idiomas',{'accion':'add'}),
    url(r'^principalEmpleado/hojaVida/idiomas/edit/$', 'idiomas',{'accion':'edit'}),
    url(r'^principalEmpleado/hojaVida/idiomas/del/$', 'idiomas',{'accion':'del'}),

    url(r'^principalEmpleado/hojaVida/oficiosSubactividades/$', 'cargaPagina',{"template":"oficios.html"}),
    url(r'^principalEmpleado/hojaVida/oficiosSubactividades/list/$', 'oficios',{'accion':'list'}),
    url(r'^principalEmpleado/hojaVida/oficiosSubactividades/add/$', 'oficios',{'accion':'add'}),
    url(r'^principalEmpleado/hojaVida/oficiosSubactividades/edit/$', 'oficios',{'accion':'edit'}),
    url(r'^principalEmpleado/hojaVida/oficiosSubactividades/del/$', 'oficios',{'accion':'del'}),

    url(r'^principalEmpleado/hojaVida/oficiosSubactividades/cmbOficios/$', 'cmbOficiosSub'),

    url(r'^principalEmpleado/hojaVida/logros/$', 'cargaPagina',{"template":"logrosPersonales.html"}),
    url(r'^principalEmpleado/hojaVida/logros/list/$', 'logros',{'accion':'list'}),
    url(r'^principalEmpleado/hojaVida/logros/add/$', 'logros',{'accion':'add'}),
    url(r'^principalEmpleado/hojaVida/logros/edit/$', 'logros',{'accion':'edit'}),
    url(r'^principalEmpleado/hojaVida/logros/del/$', 'logros',{'accion':'del'}),

    url(r'^principalEmpleado/hojaVida/referenciasPersonales/$', 'cargaPagina',{"template":"referenciasPersonales.html"}),

    url(r'^principalEmpleado/hojaVida/experiencia/$', 'cargaPagina',{"template":"experiencia.html"}),
    url(r'^principalEmpleado/hojaVida/experiencia/list/$', 'experiencia',{'accion':'list'}),
    url(r'^principalEmpleado/hojaVida/experiencia/add/$', 'experiencia',{'accion':'add'}),
    url(r'^principalEmpleado/hojaVida/experiencia/edit/$', 'experiencia',{'accion':'edit'}),
    url(r'^principalEmpleado/hojaVida/experiencia/del/$', 'experiencia',{'accion':'del'}),
    url(r'^principalEmpleado/hojaVida/experiencia/cmbAreaTrabajo/$', 'cmbAreaTrabajo'),

    url(r'^principalEmpleado/hojaVida/capacitaciones/$', 'cargaPagina',{"template":"capacitaciones.html"}),
    url(r'^principalEmpleado/hojaVida/capacitaciones/list/$', 'capacitaciones',{'accion':'list'}),
    url(r'^principalEmpleado/hojaVida/capacitaciones/add/$', 'capacitaciones',{'accion':'add'}),
    url(r'^principalEmpleado/hojaVida/capacitaciones/edit/$', 'capacitaciones',{'accion':'edit'}),
    url(r'^principalEmpleado/hojaVida/capacitaciones/del/$', 'capacitaciones',{'accion':'del'}),

    url(r'^principalEmpleado/hojaVida/instruccionFormal/$', 'cargaPagina',{"template":"instruccionFormal.html"}),
    url(r'^principalEmpleado/hojaVida/instruccionFormal/list/$', 'instruccionFormal',{'accion':'list'}),
    url(r'^principalEmpleado/hojaVida/instruccionFormal/add/$', 'instruccionFormal',{'accion':'add'}),
    url(r'^principalEmpleado/hojaVida/instruccionFormal/edit/$', 'instruccionFormal',{'accion':'edit'}),
    url(r'^principalEmpleado/hojaVida/instruccionFormal/del/$', 'instruccionFormal',{'accion':'del'}),

    url(r'^principalEmpleado/ofertasLaborales/$', 'principalEmpleado',{"template":"ofertasLaborales.html"}),
    url(r'^principalEmpleado/ofertasLaborales/ofertas/$', 'ofertasPag'),
    url(r'^principalEmpleado/ofertasLaborales/filtroOfertas/$', 'ofertasFiltro'),
    url(r'^principalEmpleado/ofertasLaborales/cargarOferta/$', 'cargarPaginaOferta'),
    url(r'^principalEmpleado/ofertasLaborales/cargarPaginaOferta/$', 'principalEmpleado',{"template":"cargaOfertaLaboralEmpleado.html"}),
    url(r'^principalEmpleado/ofertasLaborales/cargarDatosOferta/$', 'cargarDatosOferta'),
    url(r'^principalEmpleado/ofertasLaborales/aplicarOferta/$', 'aplicarOferta'),

    url(r'^principalEmpleado/hojaVida/CargarReferenciasPersonales/$', 'referenciasPersonales',{'accion':'list'}),
    url(r'^principalEmpleado/hojaVida/GuardarReferenciasPersonales/$', 'referenciasPersonales',{'accion':'add'}),


    url(r'^principalEmpleado/curriculo/$', 'print_users'),

    url(r'^principalEmpleado/cambioClave/$', 'cambioClave'),
    url(r'^cerrarSesion/$', 'cerrarSesion'),

)

"""Empleador"""
urlpatterns += patterns('empleador.views',
    url(r'^principalEmpleador/$', 'principalEmpleador',{'template':'inicioEmpleador.html'}),
    url(r'^principalEmpleador/publicacionEmpleo/$', 'principalEmpleador',{'template':'publicacionEmpleo.html'}),
    url(r'^principalEmpleador/publicacionEmpleo/guardar/$', 'guardarPubEmp'),
    url(r'^principalEmpleador/aplicacionesEmpleo/$', 'principalEmpleador',{'template':'aplicacionesEmpleo.html'}),
    url(r'^principalEmpleador/ofertasLaborales/aplicaciones/empleados/$', 'principalEmpleador',{'template':'empleadosAplicacion.html'}),
    url(r'^principalEmpleador/ofertasLaborales/ofertas/$', 'ofertasEmpleador'),
    url(r'^principalEmpleador/ofertasLaborales/aplicaciones/$', 'aplicacionesOfertas'),
    url(r'^principalEmpleador/ofertasLaborales/aplicadas/$', 'empleados'),
    url(r'^principalEmpleador/cambioClave/$', 'cambioClave'),
    url(r'^inicio/loginEmpleador/$', 'login'),
    url(r'^cerrarSesion/$', 'cerrarSesion'),
    url(r'^inicio/registroEmpleador/$', 'frmRegistroEmpleador'),

)

urlpatterns += patterns('',
                        url(r'^admin/', include(admin.site.urls)),
                        )
