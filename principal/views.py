# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
from principal.models import *
from empleador.models import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.serializers.json import DjangoJSONEncoder
from datetime import date
import time
from django.db.models import Q
from principal.printing import MyPrint
from io import BytesIO

def print_users(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="HOJA_VIDA.pdf"'

    buffer = BytesIO()

    report = MyPrint(buffer, 'Letter')
    pdf = report.print_users(request.GET['emp'])

    response.write(pdf)
    return response


@csrf_exempt
def CmbProvincias(request):
    if request.is_ajax():
        if request.method == 'POST':
            provincias = Provincias.objects.all().order_by('NombreP')
            data = []
            for provincia in provincias:
                data.append({
                    'idProvincia' : provincia.id,
                    'NombreP'     : provincia.NombreP
                })
            return HttpResponse(
                json.dumps(data),
                content_type = "application/json; charset=utf8"
            )
    else: raise Http404

@csrf_exempt
def CmbCiudades(request):
    if request.is_ajax():
        if request.method == 'POST':
            ciudades = Ciudad.objects.filter(idProvincia=request.POST['idP']).order_by('NombreC')
            data = []
            for ciudad in ciudades:
                data.append({
                    'idCiudad' : ciudad.id,
                    'NombreC'     : ciudad.NombreC
                })
            return HttpResponse(
                json.dumps(data),
                content_type = "application/json; charset=utf8"
            )
    else: raise Http404

def frmRegistro(request):
    if request.is_ajax():
        if request.method == 'POST':
            ciudad = Ciudad.objects.get(id=int(request.POST['cmbCiudad']))
            empleados = Empleados.objects.filter(CedulaRuc=request.POST['txtCedula']).exists()
            if not empleados:
                arregloFecha = str(request.POST['txtFechaNacimiento']).split('/')
                fecha = arregloFecha[2]+"-"+arregloFecha[1]+"-"+arregloFecha[0]
                empleado = Empleados(
                    CedulaRuc = request.POST['txtCedula'],
                    Nombre = request.POST['txtNombres'],
                    Apellido = request.POST['txtApellidos'],
                    Telefono1 = request.POST['txtTelefono1'],
                    Telefono2 = request.POST['txtTelefono2'],
                    Correo = request.POST['txtEmail'],
                    Clave = request.POST['txtClave'],
                    Fecha_Nacimiento = fecha
                )
                empleado.save()
                direccion = Direccion(
                    Calle_Principal = request.POST['txtCallePrincipal'],
                    Calle_Secundaria = request.POST['txtCalleSecundaria'],
                    Referencia = request.POST['txtReferencia'],
                    Sector = request.POST['cmbSector'],
                    Numero = request.POST['txtNumero'],
                    id_ciudad = ciudad,
                    id_usuario = empleado.id,
                    empleado = True
                )
                direccion.save()
                emp = Empleados.objects.get(id=empleado.id)
                especiales = Especiales(id_Empleado=emp);
                especiales.save()
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

def guardarDatosEmpleado(request):
    if request.is_ajax():
        if request.method == 'POST':
            empleado = Empleados.objects.get(id=request.session["usuario"]["id"])
            empleado.CedulaRuc = request.POST['txtCedula']
            empleado.Nombre = request.POST['txtNombres']
            empleado.Apellido = request.POST['txtApellidos']
            empleado.Telefono1 = request.POST['txtTelefono1']
            empleado.Telefono2 = request.POST['txtTelefono2']
            empleado.Correo = request.POST['txtEmail']
            arregloFecha = str(request.POST['txtFechaNacimiento']).split('/')
            fecha = arregloFecha[2]+"-"+arregloFecha[1]+"-"+arregloFecha[0]
            empleado.Fecha_Nacimiento = fecha
            empleado.Etnia = request.POST['cmbEtnia']
            empleado.Estado_Civil = request.POST['cmbEstadoCivil']
            empleado.Estado_Laboral = request.POST['cmbEstadoLaboral']
            empleado.Sexo = request.POST['cmbSexo']
            empleado.Tipo_Sangre = request.POST['cmbTipoSangre']
            empleado.save()

            ciudad = Ciudad.objects.get(id=int(request.POST['cmbCiudad']))
            direccion = Direccion.objects.get(id_usuario = empleado.id, empleado=True)
            direccion.Calle_Principal = request.POST['txtCallePrincipal']
            direccion.Calle_Secundaria = request.POST['txtCalleSecundaria']
            direccion.Referencia = request.POST['txtReferencia']
            direccion.Sector = request.POST['cmbSector']
            direccion.Numero = request.POST['txtNumero']
            direccion.id_ciudad = ciudad
            direccion.save()

            especial = Especiales.objects.get(id_Empleado=empleado.id)
            especial.Discapacidad = json.loads(request.POST['rBtnDiscapacidad'])
            especial.Enf_Catastrofica = json.loads(request.POST['rBtnEnfermedadCatastrofica'])
            especial.Fam_enf_Severa = json.loads(request.POST['rBtnCargoFamiliarDiscapacidad'])
            especial.Fam_enf_Catastrofica = json.loads(request.POST['rBtnCargoFamiliarCatastrofica'])
            especial.save()
            return HttpResponse(
                json.dumps({"ok":True}),
                content_type = "application/json; charset=utf8"
            )
    else: raise Http404

def login(request):
    if request.is_ajax():
        if request.method == 'POST':
            try:
                usuario = Empleados.objects.get(CedulaRuc = str(request.POST['txtCedulaLogin']), Clave = str(request.POST['txtClaveLogin']))
                direccion = Direccion.objects.get(id_usuario= usuario.id, empleado=True)

                request.session['usuario']={
                    "id": usuario.id,
                    "ciudad": direccion.id_ciudad_id
                }
                return HttpResponse(json.dumps({"url":"/encoding/principal/"}),
                                    content_type = "application/json; charset=utf8"
                )
            except Empleados.DoesNotExist:
                try :
                    cedula = Empleados.objects.get(CedulaRuc = str(request.POST['txtCedulaLogin']))
                    return HttpResponse(
                        json.dumps({"error":"contraseña incorrecta verifique e intente nuevamente"}),
                        content_type = "application/json; charset=utf8"
                    )
                except Empleados.DoesNotExist:
                    try:
                        cedula = Empleados.objects.get(Clave = str(request.POST['txtClaveLogin']))
                        return HttpResponse(
                            json.dumps({"error":"cédula incorrecta verifique e intente nuevamente"}),
                            content_type = "application/json; charset=utf8"
                        )
                    except Empleados.DoesNotExist:
                        return HttpResponse(
                            json.dumps({"error":"El Usuario no Existe Registrese e intente Nuevamente"}),
                            content_type = "application/json; charset=utf8"
                        )
    else : raise Http404

def principalEmpleado(request, template):
    empleado = Empleados.objects.get(id=request.session["usuario"]["id"])
    return render_to_response(template, {"nombre":empleado.Nombre, "apellido":empleado.Apellido, "idEmp":request.session["usuario"]["id"]},context_instance=RequestContext(request))

def cerrarSesion(request):
    del request.session["usuario"]
    del request._cookies
    return HttpResponseRedirect("/")

def cambioClave(request):
    if request.is_ajax():
        if request.method == 'POST':
            print request.POST
            empleado = Empleados.objects.get(id=request.session["usuario"]["id"])
            empleado.Clave = request.POST["txtClave1"]
            empleado.save()
            return HttpResponse(
                json.dumps({"ok":True}),
                content_type = "application/json; charset=utf8"
            )
    else: raise Http404

@csrf_exempt
def informacionPersonal(request):
    if request.is_ajax():
        if request.method == "POST":
            datosEmpleado = Empleados.objects.get(id=request.session["usuario"]["id"]).__dict__
            direccion = Direccion.objects.get(id_usuario = request.session["usuario"]["id"], empleado=True).__dict__
            datosEmpleado['Fecha_Nacimiento']=datosEmpleado['Fecha_Nacimiento'].strftime('%m/%d/%Y')
            del datosEmpleado['_state']
            del direccion['_state']

            ciudad = Ciudad.objects.get(id=direccion["id_ciudad_id"])

            especiales = Especiales.objects.get(id_Empleado=request.session["usuario"]["id"]).__dict__
            del especiales['_state']

            return HttpResponse(
                json.dumps({
                    "datosEmpleado":datosEmpleado,
                    "direccion":direccion,
                    "idProvincia":ciudad.idProvincia_id,
                    "datosEspeciales":especiales
                }), content_type="application/json; charset=utf8"
            )
    else: raise Http404

def cargaPagina(request, template):
    return render_to_response(template, context_instance=RequestContext(request))

@csrf_exempt
def cargarPreferenciasLaborales(request):
    if request.is_ajax():
        if request.method == "POST":
            try:
                detallePreferencia = Detalle_Pref_Empl.objects.get(id_Empleado=request.session["usuario"]["id"])
                preferenciasLaborales = Preferencias_laborales.objects.get(id=detallePreferencia.id_Preferencias_id)
                ciudad = Ciudad.objects.get(id=detallePreferencia.ciudad_id)

                preferencias = preferenciasLaborales.__dict__
                detPref = detallePreferencia.__dict__

                del preferencias['_state']
                del detPref['_state']
                return HttpResponse(
                    json.dumps({
                        "preferencias":preferencias,
                        "detallePreferencia": detPref,
                        "idProvincia":ciudad.idProvincia_id,
                        "primeraVez":False
                    }), content_type="application/json; charset=utf8"
                )


            except Detalle_Pref_Empl.DoesNotExist:
                preferencias = Preferencias_laborales(
                    Sector_Publico=False,
                    Sector_Privado=False,
                    Aspiracion_Salarial=370,
                    Lugar_Residencia=False
                )
                preferencias.save()

                empleado = Empleados.objects.get(id=request.session["usuario"]["id"])
                preferencias = Preferencias_laborales.objects.get(id=preferencias.id)
                ciudad = Ciudad.objects.get(id=request.session["usuario"]["ciudad"])

                detallePreferencia = Detalle_Pref_Empl(
                    id_Empleado = empleado,
                    id_Preferencias = preferencias,
                    ciudad = ciudad
                )
                detallePreferencia.save()
                detallePreferencia = Detalle_Pref_Empl.objects.get(id=detallePreferencia.id).__dict__
                del detallePreferencia['_state']

                preferencias = Preferencias_laborales.objects.get(id=preferencias.id).__dict__
                del preferencias['_state']

                ciudad = Ciudad.objects.get(id=request.session["usuario"]["ciudad"]).__dict__
                del ciudad['_state']
                return HttpResponse(
                    json.dumps({
                        "preferencias":preferencias,
                        "detallePreferencia":detallePreferencia,
                        "idProvincia":ciudad["idProvincia"],
                        "primeraVez":True
                    }), content_type="application/json; charset=utf8"
                )
    else: raise Http404

@csrf_exempt
def guardarPreferenciasLaborales(request):
    if request.is_ajax():
        if request.method == 'POST':
            detPreferencia = Detalle_Pref_Empl.objects.get(id_Empleado=request.session["usuario"]["id"])
            detPreferencia.ciudad_id = request.POST['cmbCiudad']
            detPreferencia.save()

            prefLaborales = Preferencias_laborales.objects.get(id=detPreferencia.id_Preferencias_id)
            prefLaborales.Sector_Publico = request.POST['rBtnSectorPublico']
            prefLaborales.Sector_Privado = request.POST['rBtnSectorPrivado']
            prefLaborales.Aspiracion_Salarial = request.POST['cmbAspiracionSalarial']
            prefLaborales.Lugar_Residencia = json.loads(request.GET['chBtnMismoLugarResidencia'])
            prefLaborales.save()

            return HttpResponse(
                json.dumps({"ok":True}),
                content_type = "application/json; charset=utf8"
            )
    else: raise Http404

@csrf_exempt
def cargarCiudad(request):
    if request.is_ajax():
        if request.method=='POST':
            ciudad = Ciudad.objects.get(id=request.session["usuario"]["ciudad"])
            return HttpResponse(
                json.dumps({"idCiudad":ciudad.id,"idProvincia":ciudad.idProvincia_id}),
                content_type = "application/json; charset=utf8"
                )
    else:raise Http404

@csrf_exempt
def idiomas(request, accion):
    if request.is_ajax():
        if request.method == 'POST':
            if accion == 'list':
                idiomas = Idiomas.objects.filter(id_Empleado=request.session['usuario']['id']).order_by('Idioma')
                idiomas = list(idiomas.values('Idioma','Nivel_hablado','Nivel_escrito','id'))

                return HttpResponse(
                    json.dumps({"Result":"OK","Records":idiomas}),
                    content_type = "application/json; charset=utf8"
                )

            elif accion == 'add':
                empleado = Empleados.objects.get(id=request.session['usuario']['id'])
                idiomas = Idiomas(
                    Idioma = str(request.POST['Idioma'].encode('utf8')),
                    Nivel_hablado = str(request.POST['Nivel_hablado'].encode('utf8')),
                    Nivel_escrito = str(request.POST['Nivel_escrito'].encode('utf8')),
                    id_Empleado = empleado
                )
                idiomas.save()
                idiomas = idiomas.__dict__
                del idiomas["_state"]
                del idiomas['_id_Empleado_cache']
                return HttpResponse(
                    json.dumps({'Result': "OK", "Record":idiomas}),
                    content_type = "application/json; charset=utf8"
                )
            elif accion == 'edit':
                idiomas = Idiomas.objects.get(id= request.POST['id'])
                idiomas.Idioma = request.POST['Idioma'],
                idiomas.Nivel_hablado = request.POST['Nivel_hablado'],
                idiomas.Nivel_escrito = request.POST['Nivel_escrito'],
                idiomas.id_Empleado_id = request.session['usuario']['id']
                idiomas.save()
                return HttpResponse(
                    json.dumps({'Result': "OK"}),
                    content_type = "application/json; charset=utf8"
                )
            elif accion == 'del':
                idiomas = Idiomas.objects.get(id=request.POST['id'])
                idiomas.delete()
                return HttpResponse(
                    json.dumps({'Result': "OK"}),
                    content_type = "application/json; charset=utf8"
                )
    else: raise Http404

@csrf_exempt
def oficios(request, accion):
    if request.is_ajax():
        if request.method == 'POST':
            if accion == 'list':

                subactividades = SubActividades.objects.select_related('Oficios__Nombre').all().filter(id_Empleado=request.session['usuario']['id']).order_by('id_oficio__Nombre')
                subactividades = list(subactividades.values('id','Descripcion','id_oficio__Nombre'))

                return HttpResponse(
                    json.dumps({"Result":"OK","Records":subactividades}),
                    content_type = "application/json; charset=utf8"
                )

            elif accion == 'add':

                empleado = Empleados.objects.get(id=request.session['usuario']['id'])

                oficio  = Oficios.objects.filter(Nombre__exact=request.POST['id_oficio__Nombre']).values('id')
                oficio = Oficios.objects.get(id=oficio[0]['id'])

                subactividad = SubActividades(
                    Descripcion = request.POST['Descripcion'],
                    id_oficio = oficio,
                    id_Empleado = empleado
                )
                subactividad.save()

                #'id','id_oficio__Nombre', 'Descripcion'
                d={
                    'id':subactividad.id,
                    'id_oficio__Nombre':request.POST['id_oficio__Nombre'],
                    'Descripcion': request.POST['Descripcion']
                }

                return HttpResponse(
                    json.dumps({'Result': "OK", "Record":d}),
                    content_type = "application/json; charset=utf8"
                )
            elif accion == 'edit':
                subactividad = SubActividades.objects.get(id=request.POST['id'])
                oficio  = Oficios.objects.filter(Nombre__exact=request.POST['id_oficio__Nombre']).values('id')
                subactividad.Descripcion = request.POST["Descripcion"]
                subactividad.id_oficio_id = oficio[0]['id']
                subactividad.save()
                return HttpResponse(
                    json.dumps({'Result': "OK"}),
                    content_type = "application/json; charset=utf8"
                )
            elif accion == 'del':
                subactividad = SubActividades.objects.get(id=request.POST['id'])
                subactividad.delete()
                return HttpResponse(
                    json.dumps({'Result': "OK"}),
                    content_type = "application/json; charset=utf8"
                )
    else: raise Http404

@csrf_exempt
def cmbOficiosSub(request):
    if request.is_ajax():
        if request.method == 'POST':
            data = []
            oficios = Oficios.objects.all().order_by('Nombre')
            for item in oficios:
                d = {
                    "Value":item.Nombre,
                    "DisplayText":item.Nombre
                }
                data.append(d)

            return HttpResponse(
                json.dumps({"Result":"OK","Options":data}),
                content_type = "application/json; charset=utf8"
            )
    else: raise Http404

@csrf_exempt
def logros(request, accion):
    if request.is_ajax():
        if request.method == 'POST':
            if accion == 'list':
                logros = Logros.objects.filter(id_Empleado = request.session['usuario']['id']).order_by('Tipo_Logro').values('id','Tipo_Logro','Descripcion')
                return HttpResponse(
                    json.dumps({"Result":"OK","Records":list(logros)}),
                    content_type = "application/json; charset=utf8"
                )

            elif accion == 'add':

                empleado = Empleados.objects.get(id=request.session['usuario']['id'])
                logros = Logros(
                    Tipo_Logro=request.POST['Tipo_Logro'],
                    Descripcion = request.POST['Descripcion'],
                    id_Empleado = empleado
                )

                logros.save()
                logros = logros.__dict__
                del logros['_state']
                del logros['_id_Empleado_cache']
                print logros
                return HttpResponse(
                    json.dumps({'Result': "OK", "Record":logros}),
                    content_type = "application/json; charset=utf8"
                )
            elif accion == 'edit':
                logros = Logros.objects.get(id=request.POST['id'])
                logros.Tipo_Logro = request.POST['Tipo_Logro']
                logros.Descripcion = request.POST['Descripcion']
                logros.save()
                return HttpResponse(
                    json.dumps({'Result': "OK"}),
                    content_type = "application/json; charset=utf8"
                )
            elif accion == 'del':
                logros = Logros.objects.get(id=request.POST['id'])
                logros.delete()
                return HttpResponse(
                    json.dumps({'Result': "OK"}),
                    content_type = "application/json; charset=utf8"
                )
    else: raise Http404

@csrf_exempt
def cmbAreaTrabajo(request):

    data = []
    areas = AreaTrabajo.objects.all().order_by('Nombre')
    for item in areas:
        d = {
            "Value":item.Nombre,
            "DisplayText":item.Nombre
        }
        data.append(d)

    return HttpResponse(
        json.dumps({"Result":"OK","Options":data}),
        content_type = "application/json; charset=utf8"
    )

def convertDate(strDate):
    if len(str(strDate)) == 0:
        return time.strftime("%Y-%m-%d")

    day, month, year = map(int, str(strDate).split("/"))
    return date(year, month, day).strftime("%Y-%m-%d")


@csrf_exempt
def experiencia(request, accion):
    if request.is_ajax():
        if request.method == 'POST':
            if accion == 'list':
                exp = Experiencia.objects.select_related('Area_Trabajo__Nombre').all().filter(Empleado=request.session['usuario']['id']).order_by('Institucion')
                exp = list(exp.values('id','Institucion','Puesto','Fecha_Desde','Fecha_Hasta','Actividades','Area_Trabajo__Nombre'))
                return HttpResponse(
                    json.dumps({"Result":"OK","Records":exp}, cls=DjangoJSONEncoder),
                    content_type = "application/json; charset=utf8"
                )

            elif accion == 'add':
                area = AreaTrabajo.objects.get(Nombre=request.POST['Area_Trabajo__Nombre'])

                exp = Experiencia(
                    Institucion = request.POST['Institucion'],
                    Puesto = request.POST['Puesto'],
                    Fecha_Desde = convertDate(request.POST['Fecha_Desde']),
                    Fecha_Hasta = convertDate(request.POST['Fecha_Hasta']),
                    Actividades = request.POST['Actividades'],
                    Empleado_id = request.session['usuario']['id'],
                    Area_Trabajo = area
                )
                exp.save()

                d = {
                    'id': exp.id,
                    'Institucion' : request.POST['Institucion'],
                    'Puesto' : request.POST['Puesto'],
                    'Fecha_Desde' : convertDate(request.POST['Fecha_Desde']),
                    'Fecha_Hasta' : convertDate(request.POST['Fecha_Hasta']),
                    'Actividades' : request.POST['Actividades'],
                    'Area_Trabajo__Nombre' : area.Nombre
                }
                return HttpResponse(
                    json.dumps({'Result': "OK", "Record":d}, cls=DjangoJSONEncoder),
                    content_type = "application/json; charset=utf8"
                )
            elif accion == 'edit':

                area = AreaTrabajo.objects.get(Nombre=request.POST['Area_Trabajo__Nombre'])
                exp = Experiencia.objects.get(id=request.POST['id'])
                exp.Institucion = request.POST['Institucion']
                exp.Puesto = request.POST['Puesto']
                exp.Fecha_Desde = convertDate(request.POST['Fecha_Desde'])
                exp.Fecha_Hasta = convertDate(request.POST['Fecha_Hasta'])
                exp.Actividades = request.POST['Actividades']
                exp.Area_Trabajo = area
                exp.save()

                return HttpResponse(
                    json.dumps({'Result': "OK"}),
                    content_type = "application/json; charset=utf8"
                )
            elif accion == 'del':
                exp = Experiencia.objects.get(id=request.POST['id'])
                exp.delete()
                return HttpResponse(
                    json.dumps({'Result': "OK"}),
                    content_type = "application/json; charset=utf8"
                )
    else: raise Http404


@csrf_exempt
def capacitaciones(request, accion):
    if request.is_ajax():
        if request.method == 'POST':
            if accion == 'list':
                capacitaciones = Capacitaciones.objects.filter(id_Empleado_id = request.session['usuario']['id']).order_by('Institucion')
                return HttpResponse(
                    json.dumps({"Result":"OK","Records":list(capacitaciones.values())}, cls=DjangoJSONEncoder),
                    content_type = "application/json; charset=utf8"
                )

            elif accion == 'add':
                capacitaciones = Capacitaciones(
                    Institucion = request.POST['Institucion'],
                    Tipo_Evento = request.POST['Tipo_Evento'],
                    Area_Estudios = request.POST['Area_Estudios'],
                    Nombre_Evento = request.POST['Nombre_Evento'],
                    Tipo_Certificado = request.POST['Tipo_Certificado'],
                    Fecha_Desde = convertDate(request.POST['Fecha_Desde']),
                    Fecha_Hasta = convertDate(request.POST['Fecha_Hasta']),
                    Dias = request.POST['Dias'],
                    Horas = request.POST['Horas'],
                    id_Empleado_id = request.session['usuario']['id']
                )
                capacitaciones.save()

                d = {
                    'id': capacitaciones.id,
                    'Institucion' : request.POST['Institucion'],
                    'Area_Estudios' : request.POST['Area_Estudios'],
                    'Nombre_Evento' : request.POST['Nombre_Evento'],
                    'Tipo_Certificado' : request.POST['Tipo_Certificado'],
                    'Fecha_Desde' : convertDate(request.POST['Fecha_Desde']),
                    'Fecha_Hasta' : convertDate(request.POST['Fecha_Hasta']),
                    'Dias' : request.POST['Dias'],
                    'Horas' : request.POST['Horas']
                }

                return HttpResponse(
                    json.dumps({'Result': "OK", "Record":d}, cls=DjangoJSONEncoder),
                    content_type = "application/json; charset=utf8"
                )
            elif accion == 'edit':


                capacitaciones = Capacitaciones.objects.get(id=request.POST['id'])
                capacitaciones.Institucion = request.POST['Institucion']
                capacitaciones.Tipo_Evento = request.POST['Tipo_Evento']
                capacitaciones.Area_Estudios = request.POST['Area_Estudios']
                capacitaciones.Nombre_Evento = request.POST['Nombre_Evento']
                capacitaciones.Tipo_Certificado = request.POST['Tipo_Certificado']
                capacitaciones.Fecha_Desde = convertDate(request.POST['Fecha_Desde'])
                capacitaciones.Fecha_Hasta = convertDate(request.POST['Fecha_Hasta'])
                capacitaciones.Dias = request.POST['Dias']
                capacitaciones.Horas = request.POST['Horas']
                capacitaciones.save()

                return HttpResponse(
                    json.dumps({'Result': "OK"}),
                    content_type = "application/json; charset=utf8"
                )
            elif accion == 'del':
                capacitaciones = Capacitaciones.objects.get(id=request.POST['id'])
                capacitaciones.delete()
                return HttpResponse(
                    json.dumps({'Result': "OK"}),
                    content_type = "application/json; charset=utf8"
                )
    else: raise Http404


@csrf_exempt
def instruccionFormal(request, accion):
    if request.is_ajax():
        if request.method == 'POST':
            if accion == 'list':
                instruccion = Instruccion_Formal.objects.filter(id_Empleado_id = request.session['usuario']['id']).order_by('Institucion')
                return HttpResponse(
                    json.dumps({"Result":"OK","Records":list(instruccion.values())}),
                    content_type = "application/json; charset=utf8"
                )

            elif accion == 'add':
                instruccion = Instruccion_Formal(
                    Nivel_Instruccion = request.POST['Nivel_Instruccion'],
                    Institucion = request.POST['Institucion'],
                    Titulo_Obtenido = request.POST['Titulo_Obtenido'],
                    Registro_Senescyt = request.POST['Registro_Senescyt'],
                    id_Empleado_id = request.session['usuario']['id']
                )
                instruccion.save()
                instruccion = instruccion.__dict__
                del instruccion['_state']

                print(instruccion)
                return HttpResponse(
                    json.dumps({'Result': "OK", "Record":instruccion}),
                    content_type = "application/json; charset=utf8"
                )
            elif accion == 'edit':

                instruccion = Instruccion_Formal.objects.get(id=request.POST['id'])
                instruccion.Nivel_Instruccion = request.POST['Nivel_Instruccion']
                instruccion.Institucion = request.POST['Institucion']
                instruccion.Titulo_Obtenido = request.POST['Titulo_Obtenido']
                instruccion.Registro_Senescyt = request.POST['Registro_Senescyt']
                instruccion.save()
                return HttpResponse(
                    json.dumps({'Result': "OK"}),
                    content_type = "application/json; charset=utf8"
                )
            elif accion == 'del':
                instruccion = Instruccion_Formal.objects.get(id=request.POST['id'])
                instruccion.delete()
                return HttpResponse(
                    json.dumps({'Result': "OK"}),
                    content_type = "application/json; charset=utf8"
                )
    else: raise Http404

@csrf_exempt
def referenciasPersonales(request, accion):
    if request.is_ajax():
        if request.method == "POST":
            if accion == 'list':

                referencias = Referencias_Personales.objects.filter(id_Empleado=request.session['usuario']['id']).order_by('id')
                if len(referencias) == 0:
                    for i in range(0,3):
                        referencias = Referencias_Personales.objects.create(
                            Nombres='',
                            Apellidos='',
                            Telefono='',
                            Correo='',
                            id_Empleado_id=request.session['usuario']['id']
                        )
                        referencias.save()

                    return HttpResponse(
                        json.dumps({
                            "primeraVez":True
                        }), content_type="application/json; charset=utf8"
                    )
                else:
                    referencias = referencias.values('id','Nombres','Apellidos','Telefono','Correo')
                    return HttpResponse(
                        json.dumps({
                            "referencias":list(referencias),
                            "primeraVez":False
                        }), content_type="application/json; charset=utf8"
                    )

            elif accion == 'add':
                print(request.POST)

                referencias = Referencias_Personales.objects.filter(id_Empleado=request.session['usuario']['id']).order_by('id')
                print(referencias)
                cont = 0
                for de in referencias:
                    ref = Referencias_Personales.objects.get(id=de.id)
                    ref.Nombres = request.POST['txtNombres'+str(cont)]
                    ref.Apellidos = request.POST['txtApellidos'+str(cont)]
                    ref.Telefono = request.POST['txtTelefono'+str(cont)]
                    ref.Correo = request.POST['txtEmail'+str(cont)]
                    ref.save()
                    cont+=1

                return HttpResponse(
                    json.dumps({"ok":True}),
                    content_type = "application/json; charset=utf8"
                )
    else: raise Http404

@csrf_exempt
def ofertasPag(request):
    if request.is_ajax():
        perfil = Perfil_Cargo.objects.select_related().all().order_by('-id_Oferta__Fecha_inicio')
        perfil = perfil.values('id','Remuneracion','id_Oferta__Num_Oferta','id_Oferta__Cargo_Solicitado','id_Oferta_id')

        return HttpResponse(
            json.dumps({'ofertas':list(perfil)},cls=DjangoJSONEncoder),
            content_type = "application/json; charset=utf8"
        )
    else: raise Http404

@csrf_exempt
def ofertasFiltro(request):
    if request.is_ajax():
        perfil = Perfil_Cargo.objects.select_related().all().filter(
            Q(id_Oferta__Num_Oferta=request.POST['txtNumOferta'])|
            Q(id_Oferta__Cargo_Solicitado=request.POST['txtCargoSolicitado'])|
            Q(id_Oferta__Fecha_inicio=convertDate(request.POST['txtFechaDesde']))|
            Q(id_Oferta__Fecha_fin=convertDate(request.POST['txtFechaHasta']))|
            Q(id_Oferta__Discapacidad=request.POST['rBtnDiscapacidad'])|
            Q(Area_Estudio=request.POST['cmbAreaLaboral'])|
            Q(Remuneracion=request.POST['cmbRemuneracion'])
        ).order_by('-id_Oferta__Fecha_inicio')
        perfil = perfil.values('id','Remuneracion','id_Oferta__Num_Oferta','id_Oferta__Cargo_Solicitado','id_Oferta_id')
        print perfil
        return HttpResponse(
            json.dumps({'ofertas':list(perfil)},cls=DjangoJSONEncoder),
            content_type = "application/json; charset=utf8"
        )
    else: raise Http404


def cargarPaginaOferta(request):
    if request.method=='GET':
        request.session['oferta']= request.GET['idOferta']
        return HttpResponseRedirect("/principalEmpleado/ofertasLaborales/cargarPaginaOferta/")
    else: raise Http404

@csrf_exempt
def cargarDatosOferta(request):
    if request.is_ajax():

        perfil = Perfil_Cargo.objects.filter(id_Oferta=request.session['oferta']).values()
        ofertas = Oferta_Laboral.objects.filter(id=request.session['oferta']).values()
        print(list(perfil))
        return HttpResponse(
            json.dumps({'ofertas':list(ofertas), 'perfil':list(perfil)},cls=DjangoJSONEncoder),
            content_type = "application/json; charset=utf8"
        )
    else: raise Http404

@csrf_exempt
def aplicarOferta(request):
    if request.is_ajax():
        post = Postulante.objects.filter(id_Empleado = request.session['usuario']['id'],id_Oferta_id = request.session['oferta']).exists()
        if post :
            return HttpResponse(json.dumps({"error":True}),
                                content_type = "application/json; charset=utf8")
        postulante = Postulante(
            id_Empleado_id = request.session['usuario']['id'],
            id_Oferta_id = request.session['oferta'],
            fecha_postulacion = convertDate('')
        )
        postulante.save()
        return HttpResponse(json.dumps({"ok":True}),
                             content_type = "application/json; charset=utf8")
    else:raise Http404