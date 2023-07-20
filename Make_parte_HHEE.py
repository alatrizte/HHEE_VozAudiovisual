##### reportLab Libreríasd #####

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Corbel-Bold', 'corbelb.ttf'))

class ParteHHEE_Pdf:
    def __init__(self):
        c = canvas.Canvas("Parte_HHEE.pdf")
        c.setPageSize(landscape(A4))
        c.setLineWidth(2.6)
        x1, x2 = 60.600, 720.689
        c.rect(x1, 519.879, x2, 18.545)
        c.rect(x1, 480.968, x2, 32.036)
        c.rect(x1, 219.948, x2, 255.738)
        c.rect(x1, 178.302, x2, 36.363)
        c.rect(x1, 56.851, x2, 47.060)
        x1, y1 = 61.925, 446.176
        x2 = 779.964
        for i in range(5):
            c.line(x1, y1, x2, y1)
            y1 -= 44.98
        x1, y1 = 162.012, 474.361
        y2 = 221.273
        c.line(x1, y1, x1, y2)
        x1 += 107.57
        c.line(x1, y1, x1, y2)
        x1 += 53.785
        c.line(x1, y1, x1, y2)
        x1 += 107.57
        c.line(x1, y1, x1, y2)
        x1 = 488.896
        c.line(x1, y1, x1, y2)
        x1, y1 = 430.935, 213.340
        y2 = 179.627
        c.line(x1, y1, x1, y2)
        x1, y1 = 269.582, 102.586
        y2 = 58.176
        c.line(x1, y1, x1, y2)

        c.setLineWidth(0.75)
        c.line(60.603, 496.596, 781.286, 496.596)
        x1, y1 = 215.797, 511.679
        y2 = 482.293
        c.line(x1, y1, x1, y2)
        c.line(377.151, 496.596, 377.151, 482.293)
        c.line(488.896, 496.596, 488.896, 482.293)
        x1, x2 = 162.012, 269.582
        y1 = 460.058
        c.line(x1, y1, x2, y1)
        x1, x2 = 323.366, 430.935
        c.line(x1, y1, x2, y1)
        x1, x2 = 488.896, 779.964
        y1 = 431.183
        for i in range(5):
            c.line(x1, y1, x2, y1)
            y1 -= 44.981
        y1 = 416.189
        for i in range(5):
            c.line(x1, y1, x2, y1)
            y1 -= 44.981
        x1 = 61.925
        y1 = 196.303
        c.line(x1, y1, x2, y1)
        y1 = 86.330
        c.line(x1, y1, x2, y1)
        y1 = 72.839
        c.line(x1, y1, x2, y1)
        x1, y1 = 215.797, 460.058
        y2 = 221.273
        c.line(x1, y1, x1, y2)
        x1 = 377.151
        c.line(x1, y1, x1, y2)

        c.setFontSize(10)
        x1, y1 = 325.111, 525.134
        texto = "Parte de Horas Extras VOZ AUDIOVISUAL"
        c.drawString(x1, y1, texto)
        x1, y1 = 67.494, 500.394
        texto = "NOMBRE Y APELLIDOS"
        c.drawString(x1, y1, texto)
        y1 = 486.091
        texto = "DEPARTAMENTO"
        c.drawString(x1, y1, texto)
        x1 = 382.458
        texto = "PRODUCCION"
        c.drawString(x1, y1, texto)
        x1, y1 = 169.423, 463.388
        texto = "Jornada Establecida"
        c.drawString(x1, y1, texto)
        x1 = 336.271
        texto = "Jornada Realizada"
        c.drawString(x1, y1, texto)
        x1, y1 = 171.304, 449.099
        texto = "Entrada"
        c.drawString(x1, y1, texto)
        x1 = 332.666
        c.drawString(x1, y1, texto)
        x1 = 229.295
        texto = "Salida"
        c.drawString(x1, y1, texto)
        x1 = 391.015
        c.drawString(x1, y1, texto)
        x1, y1 = 67.494, 457.186
        texto = "Día"
        c.drawString(x1, y1, texto)
        x1 = 279.156
        texto = "Comida"
        c.drawString(x1, y1, texto)
        x1 = 438.474
        texto = "HH. Extra"
        c.drawString(x1, y1, texto)
        x1 = 491.020
        texto = "Motivo"
        c.drawString(x1, y1, texto)
        x1, y1 = 63.123, 200.703
        texto = "Total Horas Extras"
        c.drawString(x1, y1, texto)
        y1 = 183.936
        texto = "Total Horas Nocturnas"
        c.drawString(x1, y1, texto)
        y1 = 106.384
        texto = "OBSERVACIONES"
        c.drawString(x1, y1, texto)
        y1 = 90.189
        texto = "UNIDAD"
        c.drawString(x1, y1, texto)
        y1 = 75.784
        texto = "TAREAS ESPECIALES"
        c.drawString(x1, y1, texto)
        y1 = 61.707
        texto = "OTRAS"
        c.drawString(x1, y1, texto)
        x1, y1 = 682.513, 155.045
        texto = "Firmado trabajador"
        c.drawString(x1, y1, texto)

        c.setFont('Corbel-Bold', 12)
        x1, y1 = 223.508, 500.394
        texto = "Aquí tu Nombre"        ## Escribe aquí tu nombre.
        c.drawString(x1, y1, texto)
        x1, y1 = 674.356, 143.765
        c.drawString(x1, y1, texto)
        x1, y1 = 223.508, 486.091
        texto = "Aquí tu departamento" ## Escribe aquí tu departamento.
        c.drawString(x1, y1, texto)

        c.save()

ParteHHEE_Pdf()
