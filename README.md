<image src="./images/Captura desde 2023-07-20 19-53-36.png" alt="captura de pantalla" >

# CREADOR DE PARTES DE HORAS EXTRAS  
### EN LAS PRODUCCIONES DE VOZ AUDIOVISUAL

Aplicación en python que guarda en una base de datos sqlite3 las horas extras generadas.  
Se genera una lista con las horas de cada jornada. Al pulsar sobre una jornada de esta lista  
el programa generará un parte en PDF según modelo de la productora de las horas generadas en la semana.  

#### INSTALACIÓN

Clonar el repositorio o descargar el archivo comprimido y descomprimirlo en una carpeta local.  

Instala en tu equipo, si no tienes instalado, la base de datos **sqlite3**.

Instala las dependencias del archivo **requirements.txt**.   

En el archivo **Make_parte_HHEE.py** en la línea 143 escribe tu nombre. En la línea 148 escribe el nombre de tu departamento.

Eso es todo.


#### INSTRUCCIONES

En el archivo **lista_producciones.txt** escribe el nombre de la producción donde generastes las horas.  
Vete añadiendo en una linea diferente si vas generando en diferentes producciones.

Usa el botón **Iniciar** para borrar los campos y que estos vuelvan a su preset.  

El botón **Añadir** Añade a la lista inferior la jornada que establecistes:  

**_Jornada Establecida_** 
_Día_ selecciona en el desplegable el día de la jornada.  
_Entrada_ en HH:MM establece la hora en la que según orden de trabajo inicia la jornada laboral.  
_Salida_ en HH:MM establece la hora de salida según orden de trabajo.  
_Pausa Comida_ establece en MM el tiempo total de descaso dentro de la jornada. Si esta excede de los 30' estos no computarán como tiempo de jornada. 

**_Jornada Realizada_**
_Entrada_ en HH:MM la hora en la que iniciaste la jornada. 
_Salida_ en HH:MM la hora en la que se terminó tu jornada. 

**_Motivos_**
_Desplazamientos_ Selecciona si el motivo de exceso en la jornada fué a causa de los desplazamientos a localización. 
_Retrasos_ Selecciona si el motivo de exceso fué un retraso en la grabación. 

El botón **Borrar** eliminará la jornada seleccionada en la lista inferior de jornadas realizadas.  

Si has seleccionado alguna línea de la lista de jornadas, el botón **Actualizar** te permitirá guardar los cambios realizados en los datos de esa jornada.  

Si has seleccionado alguna línea de la lista de jornadas, el botón **Generar PDF** se activará y generará el parte en un PDF con las jornadas de esa semana.

<image src="./images/Captura desde 2023-07-20 20-16-41.png" alt="PDF generado" >

