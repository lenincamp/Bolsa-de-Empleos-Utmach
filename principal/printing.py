# -*- coding: utf-8 -*-
from encodings.utf_8 import decode
from reportlab.lib.pagesizes import letter, A4, cm
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import Spacer, SimpleDocTemplate, Table, TableStyle
from unicodedata import normalize

from reportlab.lib import colors
from reportlab.lib.colors import Color
from principal.models import *

class MyPrint:
    def __init__(self, buffer, pagesize):
        self.buffer = buffer
        if pagesize == 'A4':
            self.pagesize = A4
        elif pagesize == 'Letter':
            self.pagesize = letter
        self.width, self.height = self.pagesize

    def print_users(self, idEmp):
        buffer = self.buffer
        doc = SimpleDocTemplate(buffer,
                                rightMargin=72,
                                leftMargin=72,
                                topMargin=72,
                                bottomMargin=72,
                                pagesize=self.pagesize)

        # Our container for 'Flowable' objects
        elements = []

        # A large collection of style sheets pre-made for us
        styles = getSampleStyleSheet()

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        titulo = styles['Heading4']
        titulo.alignment = TA_CENTER
        titulo.backColor = colors.cornflowerblue
        titulo.textColor = colors.white
        elements.append(Paragraph('Datos Personales', titulo))
        elements.append(Spacer(0,12))

        emp = Empleados.objects.get(id=idEmp)
        dir = Direccion.objects.get(id_usuario=idEmp, empleado=True)
        ciudad = Ciudad.objects.get(id=dir.id_ciudad_id)
        provincia = Provincias.objects.get(id=ciudad.idProvincia_id)

        t = Table([
            ['Cédula de Identidad:', emp.CedulaRuc],
            ['Nombres',emp.Nombre],
            ['Apellidos: ', emp.Apellido],
            ['Correo Electrónico: ', emp.Correo],
            ['Teléfono(s): ', emp.Telefono1 + ' - ' + emp.Telefono2],
            ['Ciudad / Provincia: ', ciudad.NombreC + ' / ' + provincia.NombreP]
        ])
        t.setStyle([
            ('TEXTCOLOR',(0,0),(0,-1),colors.cornflowerblue),
            ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),

        ])

        t.hAlign = 'RIGHT'
        elements.append(t)


        elements.append(Paragraph('Instrucción Formal', titulo))
        instruccion = Instruccion_Formal.objects.filter(id_Empleado_id = idEmp)

        styles = getSampleStyleSheet()
        styleN = styles["Normal"]
        styleN.alignment = TA_CENTER

        styleBH = styles["Normal"]
        styleBH.alignment = TA_CENTER

        # Headers
        hNivelInstruccion = Paragraph('''<b>Instrucción</b>''', styleBH)
        hInstitucion = Paragraph('''<b>Institución</b>''', styleBH)
        hTituloObtenido = Paragraph('''<b>Título</b>''', styleBH)
        cont = 0
        for ins in instruccion:
            NivelInstruccion = Paragraph(ins.Nivel_Instruccion, styleN)
            Institucion = Paragraph(ins.Institucion, styleN)
            TituloObtenido = Paragraph(ins.Titulo_Obtenido, styleN)
            if cont == 0:
                data= [[hNivelInstruccion, hInstitucion,hTituloObtenido],
                   [NivelInstruccion, Institucion, TituloObtenido]]
            else:
                data= [[NivelInstruccion, Institucion, TituloObtenido]]

            cont = 1
            t = Table(data)

            t.setStyle(TableStyle([
                ('INNERGRID', (0,0), (-1,-1), .75, colors.cornflowerblue),
                ('BOX', (0,0), (-1,-1), .75, colors.cornflowerblue),
                ]))

            t.hAlign = 'CENTER'
            elements.append(t)
        ##########################################

        elements.append(Paragraph('Vocación / Subactividades', titulo))

        # Headers
        hOficio = Paragraph('''<b>Oficio</b>''', styleBH)
        hDescripcion = Paragraph('''<b>Descripción</b>''', styleBH)
        cont = 0
        subactividades = SubActividades.objects.select_related('Oficios__Nombre').all().filter(id_Empleado_id=idEmp).order_by('id_oficio__Nombre')
        subactividades = subactividades.values('Descripcion','id_oficio__Nombre')
        for sub in subactividades:
            oficio = Paragraph(sub["Descripcion"], styleN)
            descripcion = Paragraph(sub["id_oficio__Nombre"], styleN)
            if cont == 0:
                data= [[hOficio, hDescripcion],
                       [oficio, descripcion]]
            else:
                data= [[oficio, descripcion]]

            cont = 1
            t = Table(data)

            t.setStyle(TableStyle([
                ('INNERGRID', (0,0), (-1,-1), .75, colors.cornflowerblue),
                ('BOX', (0,0), (-1,-1), .75, colors.cornflowerblue),
                ]))

            t.hAlign = 'CENTER'
            elements.append(t)
        ##########################################################3
        elements.append(Paragraph('Experiencia', titulo))
        # Headers
        hInstitucion = Paragraph('''<b>Institución</b>''', styleBH)
        hPuesto = Paragraph('''<b>Puesto</b>''', styleBH)
        hActividades = Paragraph('''<b>Actividades</b>''', styleBH)
        hDesde = Paragraph('''<b>Desde</b>''', styleBH)
        hHasta = Paragraph('''<b>Hasta</b>''', styleBH)
        cont = 0
        experiencia = Experiencia.objects.filter(Empleado_id = idEmp)
        for exp in experiencia:
            institucion = Paragraph(exp.Institucion, styleN)
            puesto = Paragraph(exp.Puesto, styleN)
            actividades = Paragraph(exp.Actividades, styleN)
            desde = Paragraph(exp.Fecha_Desde.strftime("%d-%m-%Y"), styleN)
            hasta = Paragraph(exp.Fecha_Hasta.strftime("%d-%m-%Y"), styleN)
            if cont == 0:
                data= [[hInstitucion, hPuesto, hActividades, hDesde, hHasta],
                       [institucion, puesto, actividades, desde, hasta]]
            else:
                data= [[institucion, puesto, actividades, desde, hasta]]

            cont = 1
            t = Table(data)

            t.setStyle(TableStyle([
                ('INNERGRID', (0,0), (-1,-1), .75, colors.cornflowerblue),
                ('BOX', (0,0), (-1,-1), .75, colors.cornflowerblue),
                ]))

            t.hAlign = 'CENTER'
            elements.append(t)

        ##########################################################
        elements.append(Paragraph('Idiomas', titulo))

        # Headers
        hIdioma = Paragraph('''<b>Idioma</b>''', styleBH)
        hNivelHablado = Paragraph('''<b>Nivel Hablado</b>''', styleBH)
        hNivelEscrito = Paragraph('''<b>Nivel Escrito</b>''', styleBH)
        cont = 0
        idiomas = Idiomas.objects.filter(id_Empleado_id = idEmp)
        for id in idiomas:
            idioma = Paragraph(id.Idioma, styleN)
            nivelHablado = Paragraph(id.Nivel_hablado, styleN)
            nivelEscrito = Paragraph(id.Nivel_escrito, styleN)
            if cont == 0:
                data= [[hIdioma, hNivelHablado, hNivelEscrito],
                       [idioma, nivelHablado, nivelEscrito]]
            else:
                data= [[idioma, nivelHablado, nivelEscrito]]

            cont = 1
            t = Table(data)

            t.setStyle(TableStyle([
                ('INNERGRID', (0,0), (-1,-1), .75, colors.cornflowerblue),
                ('BOX', (0,0), (-1,-1), .75, colors.cornflowerblue),
                ]))

            t.hAlign = 'CENTER'
            elements.append(t)


        ##########################################################
        elements.append(Paragraph('Capacitación', titulo))

        # Headers
        hTipoEvento = Paragraph('''<b>Tipo de Evento</b>''', styleBH)
        hTipoCertificado = Paragraph('''<b>Tipo de Certificado</b>''', styleBH)
        hNombreEvento = Paragraph('''<b>Nombre del Evento</b>''', styleBH)
        hAreaEstudios = Paragraph('''<b>Area de Estudios</b>''', styleBH)
        hHoras = Paragraph('''<b>Horas</b>''', styleBH)
        cont = 0
        capacitaciones = Capacitaciones.objects.filter(id_Empleado_id = idEmp)
        for cap in capacitaciones:
            tipEvento = Paragraph(cap.Tipo_Evento, styleN)
            tipCertificado = Paragraph(cap.Tipo_Certificado, styleN)
            nomEvento = Paragraph(cap.Nombre_Evento, styleN)
            areaEstudios = Paragraph(cap.Area_Estudios, styleN)
            horas = Paragraph(cap.Horas, styleN)
            if cont == 0:
                data= [[hTipoEvento, hTipoCertificado, hNombreEvento, hAreaEstudios, hHoras],
                       [tipEvento, tipCertificado, nomEvento, areaEstudios, horas]]
            else:
                data= [[tipEvento, tipCertificado, nomEvento, areaEstudios, horas]]

            cont = 1
            t = Table(data)

            t.setStyle(TableStyle([
                ('INNERGRID', (0,0), (-1,-1), .75, colors.cornflowerblue),
                ('BOX', (0,0), (-1,-1), .75, colors.cornflowerblue),
                ('VALIGN',(0,0),(-1,-1),'CENTER'),


                ]))

            t.hAlign = 'CENTER'
            t.vAlign = 'CENTER'
            elements.append(t)

        ##########################################################
        elements.append(Paragraph('Referencias Personales', titulo))

        # Headers
        hNombres = Paragraph('''<b>Nombres</b>''', styleBH)
        hApellidos = Paragraph('''<b>Apellidos</b>''', styleBH)
        hTelefono = Paragraph('''<b>Teléfono</b>''', styleBH)
        cont = 0
        referencias = Referencias_Personales.objects.filter(id_Empleado_id = idEmp)
        for ref in referencias:
            nombres = Paragraph(ref.Nombres, styleN)
            apellidos = Paragraph(ref.Apellidos, styleN)
            telefono = Paragraph(ref.Telefono, styleN)
            if cont == 0:
                data= [[hNombres, hApellidos, hTelefono],
                       [nombres, apellidos, telefono]]
            else:
                data= [[nombres, apellidos, telefono]]


            t = Table(data)

            t.setStyle(TableStyle([
                ('INNERGRID', (0,0), (-1,-1), .75, colors.cornflowerblue),
                ('BOX', (0,0), (-1,-1), .75, colors.cornflowerblue),
                ]))

            t.hAlign = 'CENTER'
            if ref.Nombres != '' and ref.Apellidos != '' and cont == 0:
                elements.append(t)
                cont = 1



        doc.build(elements)

        # Get the value of the BytesIO buffer and write it to the response.
        pdf = buffer.getvalue()
        buffer.close()
        return pdf