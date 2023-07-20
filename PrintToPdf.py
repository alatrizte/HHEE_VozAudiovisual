from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pdfrw import PdfReader
from pdfrw.toreportlab import makerl
from pdfrw.buildxobj import pagexobj

import datetime
import locale
#locale.setlocale(locale.LC_ALL, 'es_ES')


from diasSemana import dias_semana
from databaseHoras import Database
data = Database('horasVoz.db')

pdfmetrics.registerFont(TTFont('Corbel-Bold', 'Ubuntu-R.ttf'))

class printToPdf:
    def __init__(self, fecha):

        def minutosHoras(minutos):
            HH = minutos // 60
            MM = minutos % 60
            HH_MM = "{:02d}".format(HH) + ":" + "{:02d}".format(MM)
            return HH_MM
        
        dates = dias_semana(fecha).returncode # dias que componen la semana del día selecionado

        # Bucle que recorre los días de la semana y almacena en la lista filas
        filas = [] # Lista para almacenar los datos para cubrir casillas
        for i in dates:
            todo = data.imprimir_dias_semana(i)
            if todo != []:
                filas.append(todo[0])

        # Abrimos el Parte de HH sin cubrir
        input_file = "Parte_HHEE.pdf"

        # Almacenamos la fecha del primer día de trabajo de la semana para incrustas en el nombre de salida del Pdf
        fechaPrimerDia = filas[0][2]
        dataToOutput = fechaPrimerDia[-4:]+fechaPrimerDia[3:5]+fechaPrimerDia[0:2]

        # Generamos el nombre del archivo Pdf a crear
        output_file = "HHEE_" + dataToOutput + ".pdf"

        # Lee la hoja de Pdf
        reader = PdfReader(input_file)

        #print (reader.Root.Pages.Kids[0].MediaBox)
        #print (len(reader.pages))
        page = pagexobj(reader.pages[0])
        sizeX, sizeY = page.BBox[2], page.BBox[3]

        # Compose new pdf
        c = Canvas(output_file)
        
        # Añade pagina y su tamaño importado del Parte de Horas
        c.setPageSize((sizeX, sizeY ))
        c.doForm(makerl(c, page))

        c.saveState()

        c.setFont('Corbel-Bold', 12)
        
        ## Nombre de la prodccion
        x1, y1 = 494.347, 486.068
        texto = filas[0][1]
        c.drawString(x1, y1, texto)
        
        # Bucle con el número de filas a cubrir. 
        # Los valores en x son fijos para cada columna.
        # Los valores en y iran restando dependiendo del número de filas
        sumaTotalHHEE = 0
        y1 = 419.814
        x2, y2 = 490.208, 434.950
        for i in range(len(filas)):
            print(filas[i])
            ## Dia
            x1 =  75.949
            texto = filas[i][2]
            c.drawString(x1, y1, texto)
            ## OT Entrada
            x1 = 172.909
            texto = minutosHoras(filas[i][3])
            c.drawString(x1, y1, texto)
            ## OT Salida
            x1 = 226.693
            texto = minutosHoras(filas[i][4])
            c.drawString(x1, y1, texto)
            ## Comida
            x1 = 279.850
            texto = minutosHoras(int(filas[i][5]))
            c.drawString(x1, y1, texto)
            ## Entrada
            x1 = 333.635
            texto = minutosHoras(filas[i][6])
            c.drawString(x1, y1, texto)
            ## Salida
            x1 = 388.107
            texto = minutosHoras(filas[i][7])
            c.drawString(x1, y1, texto)
            ## HH EE
            sumaTotalHHEE = sumaTotalHHEE + int(filas[i][8])
            x1 = 443.247
            texto = minutosHoras(int(filas[i][8]))
            c.drawString(x1, y1, texto)
            ## Motivos
                # Primer Campo de Motivos
            if filas[i][9] == 1:
                texto = "Desplazamientos"
            elif filas [i][10] == 1:
                texto = "Retraso en grabación"
            else:
                texto = ""
            c.drawString(x2, y2, texto)
                # Segundo campo de Motivos
            if filas[i][9] == 1 and filas[i][10] == 1:
                y2 -= 14.993
                texto = "Retraso en grabación"
                c.drawString(x2, y2, texto)
                y2 += 14.993

            y1 -= 44.98
            y2 -= 44.98
        # Total de Horas Extras
        x1, y1 = 443.247, 199.976
        texto = minutosHoras(sumaTotalHHEE)
        c.drawString(x1, y1, texto)

        c.setFont('Corbel-Bold', 9)
        x = datetime.datetime.today()
        texto = x.strftime("%A, %d de %B de %Y")
        x1, y1 = 639, 120
        c.drawString(x1, y1, texto)
            

        c.restoreState()

        #c.showPage()

        c.save()
        
#printToPdf("9/9/2020")
