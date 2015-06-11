# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
from models import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.serializers.json import DjangoJSONEncoder
from datetime import date
import time

def cambioClave(request):
    if request.is_ajax():
        if request.method == 'POST':
            print request.POST
            empleado = Empleadores.objects.get(id=request.session["usuario"]["id"])
            empleado.Clave = request.POST["txtClave1"]
            empleado.save()
            return HttpResponse(
                json.dumps({"ok":True}),
                content_type = "application/json; charset=utf8"
            )
    else: raise Http404

def login(request):
    if request.is_ajax():
        if request.method == 'POST':
            try:
                usuario = Empleadores.objects.get(CedulaRuc = str(request.POST['txtCedulaELogin']), Clave = str(request.POST['txtClaveELogin']))
                print usuario.Nombre
                request.session['usuario']={
                    "id": usuario.id
                }
                return HttpResponse(json.dumps({"url":"/encoding/principal/"}),
                                    content_type = "application/json; charset=utf8"
                )
            except Empleadores.DoesNotExist:
                try :
                    cedula = Empleadores.objects.get(CedulaRuc = str(request.POST['txtCedulaELogin']))
                    return HttpResponse(
                        json.dumps({"error":"contraseña incorrecta verifique e intente nuevamente"}),
                        content_type = "application/json; charset=utf8"
                    )
                except Empleadores.DoesNotExist:
                    try:
                        cedula = Empleadores.objects.get(Clave = str(request.POST['txtClaveELogin']))
                        return HttpResponse(
                            json.dumps({"error":"cédula incorrecta verifique e intente nuevamente"}),
                            content_type = "application/json; charset=utf8"
                        )
                    except Empleadores.DoesNotExist:
                        return HttpResponse(
                            json.dumps({"error":"El Usuario no Existe Registrese e intente Nuevamente"}),
                            content_type = "application/json; charset=utf8"
                        )
    else : raise Http404

def principalEmpleador(request, template):
    empleador = Empleadores.objects.get(id=request.session["usuario"]["id"])
    return render_to_response(template, {"nombre":empleador.Nombre, "apellido":empleador.Apellido},context_instance=RequestContext(request))

def convertDate(strDate):
    if len(str(strDate)) == 0:
        return time.strftime("%Y-%m-%d")
    day, month, year = map(int, str(strDate).split("/"))
    return date(year, month, day).strftime("%Y-%m-%d")

@csrf_exempt
def guardarPubEmp(request):
    if request.is_ajax():
        if request.method=='POST':
            numero = '1'
            of = Oferta_Laboral.objects.filter(id_Empleador_id=request.session['usuario']['id'])
            
            if len(of) > 0:
                of = Oferta_Laboral.objects.latest('id').id
                numero = str(int(of)+1)

            print(request.session['usuario']['id'])
            oferta = Oferta_Laboral(
                Num_Oferta = numero,
                Cargo_Solicitado = request.POST['txtCargoSolicitado'],
                Numero_Cargos = int(request.POST['txtNumeroCargos']),
                Tipo_Contrato = request.POST['cmbTipoContrato'],
                Relacion_Laboral = request.POST['cmbRelacionLaboral'],
                Fecha_inicio = convertDate(request.POST['txtFechaInicio']),
                Fecha_fin = convertDate(request.POST['txtFechaFin']),
                Fax = request.POST['txtFax'],
                Contacto = request.POST['txtContacto'],
                Telefono = request.POST['txtTelefono'],
                Celular = request.POST['txtCelular'],
                Correo = request.POST['txtCorreo'],
                Discapacidad = request.POST['rBtnDiscapacidad'],
                id_Empleador_id=request.session['usuario']['id']
            )
            oferta.save()
            perfil = Perfil_Cargo(
                Instruccion = request.POST['cmbInstruccion'],
                Area_Estudio = request.POST['cmbAreaEstudios'],
                Remuneracion = request.POST['cmbRemuneracion'],
                Experiencia_minima = request.POST['txtExperienciaMinima'],
                Experiencia_maxima = request.POST['txtExperienciaMaxima'],
                Conocimientos_cargo = request.POST['txtConocimientosCargo'],
                Actividades_Desem = request.POST['txtActividadesDesem'],
                Capacitacion = request.POST['cmbCapacitacion'],
                Jornadas_Trabajo = request.POST['cmbJornadasTrabajo'],
                Informacion_Adicional = request.POST['txtInforAd'],
                id_Oferta_id = oferta.id
            )
            perfil.save()
            return HttpResponse(
                json.dumps({"ok":True}),
                content_type = "application/json; charset=utf8"
            )
    else: raise Http404

@csrf_exempt
def ofertasEmpleador(request):
    if request.is_ajax():
        ofertas = Oferta_Laboral.objects.filter(id_Empleador_id = request.session['usuario']['id']).order_by('-Fecha_inicio')
        remuneracion = Perfil_Cargo.objects.filter(id_Oferta__in = ofertas)
        remuneracion = remuneracion.values('id','Remuneracion','id_Oferta__Num_Oferta','id_Oferta__Cargo_Solicitado','id_Oferta_id')
        return HttpResponse(
            json.dumps({'ofertas':list(remuneracion)},cls=DjangoJSONEncoder),
            content_type = "application/json; charset=utf8"
        )
    else: raise Http404


def aplicacionesOfertas(request):

    request.session['oferta'] = request.GET['idOferta']
    return HttpResponseRedirect("/principalEmpleador/ofertasLaborales/aplicaciones/empleados/")

@csrf_exempt
def empleados(request):
    if request.is_ajax():
        postulante = Postulante.objects.filter(id_Oferta_id=request.session['oferta'])
        empleados = Empleados.objects.filter(id__in=postulante.values("id_Empleado_id"))
        return HttpResponse(
            json.dumps({'empleados':list(empleados.values('id','Nombre','Apellido'))},cls=DjangoJSONEncoder),
            content_type = "application/json; charset=utf8"
        )
    else: raise Http404

def cargaPagina(request, template):
    return render_to_response(template, context_instance=RequestContext(request))

def cerrarSesion(request):
    del request.session["usuario"]
    del request._cookies
    return HttpResponseRedirect("/")


def frmRegistroEmpleador(request):
    if request.is_ajax():
        if request.method == 'POST':
            empleados = Empleadores.objects.filter(CedulaRuc=request.POST['txtCedulaEmpleador']).exists()
            print(request.POST)
            if not empleados:
                empleador = Empleadores(
                    CedulaRuc = request.POST['txtCedulaEmpleador'],
                    Nombre = request.POST['txtNombres'],
                    Apellido = request.POST['txtApellidos'],
                    Telefono1 = request.POST['txtTelefono1'],
                    Telefono2 = request.POST['txtTelefono2'],
                    Correo = request.POST['txtEmail'],
                    Clave = request.POST['txtClave'],
                    Tipo_Persona = request.POST['txtTipoPersona'],
                    Nombre_Comercial = request.POST['txtNombreComercial'],
                    Tipo_Empresa = request.POST['txtTipoEmpresa'],
                    Pagina_Web = request.POST['txtPaginaWeb']
                )
                empleador.save()

                return HttpResponse(
                    json.dumps({"ok":True}),
                    content_type = "application/json; charset=utf8"
                )
            else:
                return HttpResponse(
                    json.dumps({"error":True}),
                    content_type = "application/json; charset=utf8"
                )
    else: raise Http404