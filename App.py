from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime, timedelta
from tkinter.filedialog import askopenfile

from databaseHoras import Database
data = Database('horasVoz.db')

from diasSemana import dias_semana

from PrintToPdf import printToPdf

pausa_en_jornada = True

# Almacena el numero de la semana
hoy=datetime.now()

### Actualiza los datos en el arbol 
def actualizar_tabla():
    tabla.delete(*tabla.get_children())
    for row in data.listar():
        listRow = list(row)
        tabla.insert('', 'end', text=str(row[0]), values=listRow)

def default():
    produccion_input.current(ultimo)
    fecha_input.set_date(datetime.now())
    HentradaEstablecida_text.set("{:02d}".format(8))
    MentradaEstablecida_text.set("{:02d}".format(0))
    HsalidaEstablecida_text.set(16)
    MsalidaEstablecida_text.set("{:02d}".format(0))
    pausa_text.set(30)
    Hentrada_text.set("{:02d}".format(8))
    Mentrada_text.set("{:02d}".format(0))
    Hsalida_text.set(16)
    Msalida_text.set("{:02d}".format(0))
    HHEE_text.set("{:02d}".format(0))
    desplazamiento_var.set(0)
    retraso_var.set(0)
    update_numero_semana(hoy)
    HHtotal_text.set(0)
    print_btn['state'] = DISABLED

def calculoHorasOrden():
    global pausa_en_jornada
    #horas a minutos
    HoraOrdenEntrada=int(HentradaEstablecida_input.get()) * 60
    MinutosOrdenEntrada=int(MentradaEstablecida_input.get()) + HoraOrdenEntrada
    HoraOrdenSalida=int(HsalidaEstablecida_input.get()) * 60
    MinutosOrdenSalida=int(MsalidaEstablecida_input.get()) + HoraOrdenSalida
    # establecemos el tiempo de la jornada establecida y la pasamos a Horas
    JornadaOrden=(MinutosOrdenSalida-MinutosOrdenEntrada)/60 
    # si la jornada establecida tiene 8h o menos la pausa entra en jornada y es de 30'
    if JornadaOrden <= 8:
        pausa_text.set(30)
        pausa_en_jornada = True
    # si no, la pausa no entra en jornada.
    else:
        pausa_text.set((MinutosOrdenSalida-MinutosOrdenEntrada)-480)
        pausa_en_jornada = False
    # al cambiar la hora de entrada y salida de jornada establecida
    # tambien se actualizan las horas en jornada realizada
    Hentrada_text.set(HentradaEstablecida_text.get())
    Mentrada_text.set(MentradaEstablecida_text.get())
    Hsalida_text.set(HsalidaEstablecida_text.get())
    Msalida_text.set(MsalidaEstablecida_text.get())

def calculoHHEE():
    # Jornada realizada a minutos
    HoraEntrada = int(Hentrada_input.get())*60
    MinutosEntrada = int(Mentrada_input.get()) + HoraEntrada
    HoraSalida = int(Hsalida_input.get())*60
    MinutosSalida = int(Msalida_input.get()) + HoraSalida
    # computo de minutos realizados y restamos 8h (480')
    HHEE_minutos = (MinutosSalida - MinutosEntrada) - 480
    # si la pausa no entra en jornada restamos esos minutos de jornada realizada
    if pausa_en_jornada==False:
        HHEE_minutos -= int(pausa_text.get())
    # Mostramos las horas extras
    HHEE_text.set(HHEE_minutos)   

def add_item():
    # Jornada OT a minutos
    HoraOrdenEntrada=int(HentradaEstablecida_input.get()) * 60
    MinutosOrdenEntrada=int(MentradaEstablecida_input.get()) + HoraOrdenEntrada
    HoraOrdenSalida=int(HsalidaEstablecida_input.get()) * 60
    MinutosOrdenSalida=int(MsalidaEstablecida_input.get()) + HoraOrdenSalida
    # Jornada realizada a minutos
    HoraEntrada = int(Hentrada_input.get())*60
    MinutosEntrada = int(Mentrada_input.get()) + HoraEntrada
    HoraSalida = int(Hsalida_input.get())*60
    MinutosSalida = int(Msalida_input.get()) + HoraSalida
    data.insert(produccion_text.get(), fecha_input.get(), 
                MinutosOrdenEntrada, MinutosOrdenSalida, pausa_text.get(),
                MinutosEntrada, MinutosSalida, HHEE_text.get(), 
                desplazamiento_var.get(), retraso_var.get())
    actualizar_tabla()
    default()

def select_item(event):
    global selected_item
    index = tabla.focus()
    selected_item = tabla.item(index)['values']
    # print(selected_item)
    produccion_text.set(selected_item[1])
    fecha_text.set(selected_item[2])
    HentradaEstablecida_text.set("{:02d}".format(selected_item[3]//60))
    MentradaEstablecida_text.set("{:02d}".format(selected_item[3]%60))
    HsalidaEstablecida_text.set("{:02d}".format(selected_item[4]//60))
    MsalidaEstablecida_text.set("{:02d}".format(selected_item[4]%60))
    pausa_text.set("{:02d}".format(selected_item[5]))
    Hentrada_text.set("{:02d}".format(selected_item[6]//60))
    Mentrada_text.set("{:02d}".format(selected_item[6]%60))
    Hsalida_text.set("{:02d}".format(selected_item[7]//60))
    Msalida_text.set("{:02d}".format(selected_item[7]%60))
    HHEE_text.set(selected_item[8])
    desplazamiento_var.set(selected_item[9])
    retraso_var.set(selected_item[10])
    update_numero_semana(selected_item[2])
    print_btn['state'] = NORMAL
    
    HHtotal_text.set(dias_de_una_semana(selected_item[2]))

def dias_de_una_semana(dia):
    TotalHoras = 0
    dates = dias_semana(dia).returncode
    for i in dates:
        horasE=data.suma_de_horas(i)
        if len(horasE) > 0:
            TotalHoras = TotalHoras + int (horasE[0][0])
    return TotalHoras
    
def remove_item():
    data.delete(selected_item[0])
    actualizar_tabla()
    default()

def update_item():
    # Jornada OT a minutos
    HoraOrdenEntrada=int(HentradaEstablecida_input.get()) * 60
    MinutosOrdenEntrada=int(MentradaEstablecida_input.get()) + HoraOrdenEntrada
    HoraOrdenSalida=int(HsalidaEstablecida_input.get()) * 60
    MinutosOrdenSalida=int(MsalidaEstablecida_input.get()) + HoraOrdenSalida
    # Jornada realizada a minutos
    HoraEntrada = int(Hentrada_input.get())*60
    MinutosEntrada = int(Mentrada_input.get()) + HoraEntrada
    HoraSalida = int(Hsalida_input.get())*60
    MinutosSalida = int(Msalida_input.get()) + HoraSalida
    data.update(selected_item[0], produccion_text.get(), fecha_input.get(), 
                MinutosOrdenEntrada, MinutosOrdenSalida, pausa_text.get(),
                MinutosEntrada, MinutosSalida, HHEE_text.get(), 
                desplazamiento_var.get(), retraso_var.get())
    actualizar_tabla()   

def update_numero_semana(dia):
    # cambia el tipo si el formato de dia 'datetime'
    if type(dia) != datetime:
        dia=dia + " 00:00:00"
        dia = datetime.strptime(dia, '%d/%m/%Y %H:%M:%S')

    semana_text.set(int(dia.strftime("%W"))+1)


def actualiza_semana(event):
    update_numero_semana(fecha_input.get())
    
def importar():
    file = askopenfile(mode ='r+', filetypes =[('Text Files', '*.txt')])
    # print (file.name)
    if file is not None: 
        content = file.readlines()
        for linea in content:
            l = linea.split(",")
            data.insert(l[1], l[0], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9])
    actualizar_tabla()
    file.truncate(0)
    file.close()
                 
def print_to_pdf():
    printToPdf(fecha_text.get())
    print("Generando PDF")
    
def cerrar():
    app.quit()

# Create window object
app = Tk()

app.title('Horas Extras - Voz Audiovisual')
app.geometry('610x450') # ancho por alto
icon = PhotoImage(file = 'icon.png')
app.iconphoto(False, icon)

lista_producciones = open ("lista_producciones.txt", "r")
producciones = []
for c in lista_producciones:
    producciones.append(c[:-1])

# Variable para en Default escribir en la lista desplegable el nombre de la ultima produccion
ultimo = len(producciones) - 1

# Menú

menubar = Menu(app)
app.config(menu = menubar)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Importar", command=importar)
filemenu.add_command(label="Cerrar", command = cerrar)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Acerca de...")

menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)


# Inputs

Label(app, text="Nombre Producción", pady=10, padx=10).grid(row=0, column=0, sticky=E)
produccion_text = StringVar()
produccion_input = ttk.Combobox(app, textvariable=produccion_text, width=60, state="readonly", values=producciones)
produccion_input.grid(row=0, column=1, columnspan=10)
produccion_input.current(ultimo)

ttk.Separator(app, orient=HORIZONTAL).grid(row=2,column=0,columnspan=6, padx=10, ipadx=170) #separador
ttk.Separator(app, orient=HORIZONTAL).grid(row=2,column=6,columnspan=5, padx=10, ipadx=110) #separador

Label(app, text="Jornada Establecida").grid( row=1, column=0)

Label(app, text="Día").grid(row=3, column=0) # Etiqueta fecha ########
fecha_text = StringVar()
fecha_input = DateEntry(app,  
                    relief='flat',
                    width=12,
                    justify=CENTER,
                    state="readonly",
                    date_pattern='dd/MM/yyyy',
                    textvariable=fecha_text
                    )
fecha_input.grid(row=4, column=0)
fecha_input.bind("<<DateEntrySelected>>", actualiza_semana)


Label(app, text="Entrada", width=6).grid(row=3, column=1, columnspan=2) # Etiqueta Entrada por OT ########
HentradaEstablecida_text = StringVar(value=8)
HentradaEstablecida_input = Spinbox(app, textvariable=HentradaEstablecida_text, from_=0, to=23, format="%02.0f", width=2, command=calculoHorasOrden, state="readonly")
HentradaEstablecida_input.grid(row=4, column=1)

MentradaEstablecida_text = StringVar()
MentradaEstablecida_input = Spinbox(app, textvariable=MentradaEstablecida_text, from_=0, to=59, format="%02.0f", width=2, command=calculoHorasOrden, state="readonly")
MentradaEstablecida_input.grid(row=4, column=2)

Label(app, text="Salida", width=6).grid(row=3, column=3, columnspan=2) # Etiqueta Salida por OT ########
HsalidaEstablecida_text = StringVar(value=16)
HsalidaEstablecida_input = Spinbox(app, textvariable=HsalidaEstablecida_text, from_=0, to=23, format="%02.0f", width=2, command=calculoHorasOrden, state="readonly")
HsalidaEstablecida_input.grid(row=4, column=3)

MsalidaEstablecida_text = StringVar()
MsalidaEstablecida_input = Spinbox(app, textvariable=MsalidaEstablecida_text, from_=0, to=59, format="%02.0f", width=2, command=calculoHorasOrden, state="readonly")
MsalidaEstablecida_input.grid(row=4, column=4)

Label(app, text="Pausa Comida (min.)").grid(row=3, column=5) # Etiqueta Pausa de comida ########
pausa_text = StringVar(value=30)
pausa_input = Spinbox(app, textvariable=pausa_text, from_=0, to=240, format="%02.0f", width=3, state="readonly", justify=CENTER)
pausa_input.grid(row=4, column=5, padx=(0,30))

Label(app, text="Jornada Realizada").grid( row=1, column=6, columnspan=4)

Label(app, text="Entrada", width=6).grid(row=3, column=6, columnspan=2) # Etiqueta de Entrada realizada ########
Hentrada_text = StringVar(value=8)
Hentrada_input = Spinbox(app, textvariable=Hentrada_text, from_=0, to=23, format="%02.0f", width=2, command=calculoHHEE, state="readonly")
Hentrada_input.grid(row=4, column=6)

Mentrada_text = StringVar()
Mentrada_input = Spinbox(app, textvariable=Mentrada_text, from_=0, to=59, format="%02.0f", width=2, command=calculoHHEE, state="readonly")
Mentrada_input.grid(row=4, column=7)

Label(app, text="Salida", width=6).grid(row=3, column=8, columnspan=2) # Etiqueta de Salida Realizada ########
Hsalida_text = StringVar(value=16)
Hsalida_input = Spinbox(app, textvariable=Hsalida_text, from_=0, to=23, format="%02.0f", width=2, command=calculoHHEE, state="readonly")
Hsalida_input.grid(row=4, column=8)

Msalida_text = StringVar()
Msalida_input = Spinbox(app, textvariable=Msalida_text, from_=0, to=59, format="%02.0f", width=2, command=calculoHHEE, state="readonly")
Msalida_input.grid(row=4, column=9)

Label(app, text="Horas EE. (min.)").grid(row=3, column=10) # Etiqueta de Horas Extras realizadas ########
HHEE_text = StringVar(value=0)
HHEE_input = Entry(app, textvariable=HHEE_text, state="readonly", justify=CENTER,)
HHEE_input.grid(row=4, column=10)

Label(app, text="Motivos").grid(row=5, column=8, columnspan=2) # Etiqueta de Motivos de las Horas Extra ########
desplazamiento_var = IntVar()
desplazamiento_input = Checkbutton(app, variable=desplazamiento_var, text="Desplazamientos")
desplazamiento_input.grid(row=5, column=10, columnspan=2, sticky=W)

retraso_var = IntVar()
retraso_input = Checkbutton(app, variable=retraso_var, text="Retrasos")
retraso_input.grid(row=6, column=10, columnspan=2, sticky=W)

# Buttons

default_btn = Button(app, text='Iniciar', width=6, command=default)
default_btn.grid(row=7, column=0, )

add_btn= Button(app, text='Añadir', width=6, command=add_item)
add_btn.grid(row=7, column=1, columnspan=2, pady=10)

remove_btn= Button(app, text='Borrar', width=6, command=remove_item)
remove_btn.grid(row=7, column=3, columnspan=2)

update_btn = Button(app, text='Actualizar', command=update_item)
update_btn.grid(row=7, column=5)

print_btn = Button(app, text='Generar PDF', command=print_to_pdf, state=DISABLED)
print_btn.grid(row=6, column=5)
# Suma total Horas semanales

Label(app, text="Sem:").grid(row=7, column=6)
semana_text = StringVar()
semana_input = Entry(app, textvariable=semana_text, width=3, state="readonly", justify=CENTER)
semana_input.grid(row=7, column=7)

Label(app, text="HH. Total").grid(row=7, column=8, columnspan=2)
HHtotal_text = StringVar()
HHtotal_input = Entry(app, textvariable=HHtotal_text, state="readonly", justify=CENTER,)
HHtotal_input.grid(row=7, column=10)

# Tabla

tabla = ttk.Treeview()
tabla.grid(row=8, column=0, columnspan=11, padx=10, sticky=NSEW)
columnas = ['id', 'produccion', 'fecha', 'entradaOrden', 'salidaOrden', 'pausa', 'entrada', 'salida', 'extras', 'desplazamientos', 'retraso']
tabla["columns"]= columnas
tabla["displaycolumns"] = ('id', 'produccion', 'fecha', 'entrada', 'salida', 'extras')
tabla['show'] = 'headings'
tabla.heading("id", text="ID", anchor='c')
tabla.column("id", width=15, anchor='c')
tabla.heading("produccion", text="Producción", anchor='c')
tabla.column("produccion", width=25, anchor='c')
tabla.heading("fecha", text="Fecha", anchor='c')
tabla.column("fecha", width=15, anchor='c')
tabla.heading("entrada", text="Entrada", anchor='c')
tabla.column("entrada", width=15, anchor='c')
tabla.heading("salida", text="Salida", anchor='c')
tabla.column("salida", width=15, anchor='c')
tabla.heading("extras", text="Extras", anchor='c')
tabla.column("extras", width=15, anchor='c')
tabla.bind('<<TreeviewSelect>>', select_item)

update_numero_semana(hoy)
actualizar_tabla()
#Start the program
app.mainloop()