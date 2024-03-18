from tkinter import *
from tkinter import ttk
from functions import obtener_tamaño_pantalla,on_button_click
from model import mostrar_estudiante
root = Tk()
root.title("Registro de horas extracurriculares")
root.config(bg="white")
ancho, alto = obtener_tamaño_pantalla(root)

def on_cerrar_ventana():
    root.destroy()
def cerrar_C():
    ventana.destroy()

def consulta_estudiante():
    vBandera=1
    ventana.deiconify()

def inicio():
    ventana.withdraw()
    ventana2.withdraw()
def regreso1():
    vBandera=1#esta variable es provicional en lo que se hacen las conexiones con la base de datos
    if vBandera==1:
        ventana2.withdraw()
        ventana.deiconify()
def obtener_texto():
    texto = entrada.get()
    print("El texto ingresado es:", texto)
def center_content(tree, column):
    tree.heading(column, anchor='center')
    tree.column(column, anchor='center')

root.geometry(f"{ancho}x{alto}")
root.iconbitmap("image/logo-escuela-de-ciencias.ico")

miFrame=Frame()
miFrame.pack(fill="both", expand="True")
miFrame.config(bg="white")
miFrame.config(bd=21)
miFrame.config(relief="groove")

label1=Label(miFrame, text="HORAS EXTRACURRICULARES",font=("Arial", 17, "bold italic"),bg="white").place(x=ancho/2.7, y=2)

frame2 = Frame(miFrame, width=ancho/2, height=alto/2.3, bg="white")
frame2.pack(side="right")

frame2.grid_propagate(False)  # Evita que el Frame se ajuste al tamaño de sus widgets

boton1 = Button(frame2, text="Agregar Horas", bg="#0067E0", command=on_button_click, fg="white", width=40, height=5)
boton1.grid(row=0, column=0, pady=(50, 0))  # Ajusta el pady para centrar verticalmente

boton2 = Button(frame2, text="Agregar Estudiante", bg="#0067E0", command=on_button_click, fg="white", width=40, height=5)
boton2.grid(row=1, column=0, pady=10)

boton3 = Button(frame2, text="Consultar Estudiante", bg="#0067E0", command=consulta_estudiante, fg="white", width=40, height=5)
boton3.grid(row=2, column=0, pady=10)

boton4 = Button(frame2, text="Modificar Estudiante", bg="#0067E0", command=on_button_click, fg="white", width=40, height=5)
boton4.grid(row=3, column=0, pady=10)

boton5 = Button(frame2, text="Salir", bg="#AA1A1A", command=on_cerrar_ventana, fg="white", width=30, height=4)
boton5.grid(row=4, column=0, pady=(0, 50))  # Ajusta el pady para centrar verticalmente

# Alinear los botones horizontalmente al centro
frame2.grid_columnconfigure(0, weight=1)

frame4 = Frame(miFrame, width=ancho/2, height=alto/2.3, bg="white")
frame4.pack(side="left")
frame4.grid_propagate(False)  

# Cargar la imagen
imagen = PhotoImage(file="image/verdadero.png")

# Redimensionar la imagen
imagen_redimensionada = imagen.subsample(3, 3)  # Redimensionar a la mitad

# Crear el widget Label para mostrar la imagen
label_imagen = Label(frame4, image=imagen_redimensionada, bg="white")
label_imagen.pack(expand=True, fill=BOTH)
label_imagen.bind("<Configure>", lambda e: label_imagen.config(width=e.width, height=e.height))

# Centrar la imagen dentro del Frame
frame4.grid_rowconfigure(0, weight=1)
frame4.grid_columnconfigure(0, weight=1)
label_imagen.grid(row=0, column=0, sticky=NSEW)

ventana = Toplevel(root)
ventana.title("Consultar Estudiante")
ventana.geometry(f"{ancho}x{alto}")
ventana.config(bg="white")
ventana.iconbitmap("image/logo-escuela-de-ciencias.ico")

frame3=Frame(ventana)
frame3.pack(fill="both", expand="True")
frame3.config(bg="white")
frame3.config(bd=21)
frame3.config(relief="groove")

titulo1 = Frame(frame3, width=ancho, height=alto/12, bg="white")
titulo1.pack()

label1 = Label(titulo1, text="CONSULTAR ESTUDIANTE", font=("Arial", 17, "bold italic"), bg="white")
label1.pack()
label1.place(x=ancho/2.7, y=2)

imagen2 = PhotoImage(file="image/flecha.png")
imagen_redimensionada2 = imagen2.subsample(5, 5)  # Redimensionar a la mitad

boton6 = Button(titulo1, image=imagen_redimensionada2, width=40, height=20, command=inicio, bg="white", borderwidth=0)
boton6.pack()
boton6.place(x=10, y=10)  

# Crear el contenedor1
contenedor1 = Frame(frame3, width=ancho, height=alto/2, bg="white")
contenedor1.pack()
contenedor1.grid_propagate(False)  # Desactiva la propagación de la cuadrícula en el contenedor1

# Crear la caja de entrada dentro de contenedor1
apellido1=Label(contenedor1,text="Apellido paterno:",bg="white").place(x=320,y=10)
apellido2=Label(contenedor1,text="Apellido materno:",bg="white").place(x=470,y=10)
entrada = Entry(contenedor1)
entrada.place(x=320,y=30)
entrada.config(relief="solid")
entrada2 = Entry(contenedor1)
entrada2.place(x=470,y=30)
entrada2.config(relief="solid")
# Crear un botón para obtener el texto ingresado
botonb = Button(contenedor1, text="Buscar", command=obtener_texto,bg="black",fg="white")
botonb.place(x=620,y=30)

tabla = ttk.Treeview(contenedor1, columns=("Apellidos", "Nombre(s)", "Semestre",""), show="headings")
tabla.heading("Apellidos", text="Apellidos")
tabla.heading("Nombre(s)", text="Nombre(s)")
tabla.heading("Semestre", text="Semestre")
tabla.heading("", text="")
tabla.place(x=250,y=60)
center_content(tabla, "Semestre")
datos = mostrar_estudiante()
    
    # Insertar datos en la tabla
for dato in datos:
    print(dato)
    tabla.insert("", "end", values=dato)

ventana2 = Toplevel(root)
ventana2.title("Consultar horas")
ventana2.geometry(f"{ancho}x{alto}")
ventana2.config(bg="white")
ventana2.iconbitmap("image/logo-escuela-de-ciencias.ico")

frame4=Frame(ventana2)
frame4.pack(fill="both", expand="True")
frame4.config(bg="white")
frame4.config(bd=21)
frame4.config(relief="groove")

titulo2 = Frame(frame4, width=ancho, height=alto/12, bg="white")
titulo2.pack()

label2 = Label(titulo2, text="CONSULTAR HORAS", font=("Arial", 17, "bold italic"), bg="white")
label2.pack()
label2.place(x=ancho/2.7, y=2)

imagen3 = PhotoImage(file="image/flecha.png")
imagen_redimensionada3 = imagen3.subsample(5, 5)  # Redimensionar a la mitad

boton7 = Button(titulo2, image=imagen_redimensionada3, width=40, height=20, command=regreso1, bg="white", borderwidth=0)
boton7.pack()
boton7.place(x=10, y=10)  

# Crear el contenedor1
contenedor2 = Frame(frame4, width=ancho, height=alto/2, bg="white")
contenedor2.pack()
contenedor2.grid_propagate(False)  # Desactiva la propagación de la cuadrícula en el contenedor1

# Crear la caja de entrada dentro de contenedor1
apellido1_1=Label(contenedor2,text="Apellido paterno:",bg="white").place(x=320,y=10)
apellido2_2=Label(contenedor2,text="Apellido materno:",bg="white").place(x=470,y=10)
entrada3 = Entry(contenedor2)
entrada3.place(x=320,y=30)
entrada3.config(relief="solid")
entrada4 = Entry(contenedor2)
entrada4.place(x=470,y=30)
entrada4.config(relief="solid")
# Crear un botón para obtener el texto ingresado
botonb2 = Button(contenedor2, text="Buscar", command=obtener_texto,bg="black",fg="white")
botonb2.place(x=620,y=30)

tabla2 = ttk.Treeview(contenedor2, columns=("Taller", "Documento", "Duracion","Horas extra","inf. recuperada",""), show="headings")
tabla2.heading("Taller", text="Taller")
tabla2.heading("Documento", text="Documento")
tabla2.heading("Duracion", text="duracion")
tabla2.heading("Horas extra", text="Horas extra")
tabla2.heading("inf. recuperada", text="inf. recuperada")
tabla2.heading("", text="")
tabla2.place(x=60,y=60)

ventana.protocol("WM_DELETE_WINDOW", inicio)
ventana2.protocol("WM_DELETE_WINDOW", inicio)

ventana.withdraw()
ventana2.withdraw()
root.protocol("WM_DELETE_WINDOW", on_cerrar_ventana)


root.mainloop()