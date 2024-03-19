from tkinter import *
from model import buscarestudiante,mostrar_estudiante
from tkinter import ttk

def obtener_texto2(entrada3,entrada4,contenedor3,tabla3):
    texto = entrada3.get()
    texto2 = entrada4.get()
    error = Label(contenedor3, text="", bg="white", fg="red")
    error.place(x=670, y=30)

    if texto == "" and texto2 == "":
        error.config(text="Ingresa un apellido paterno y materno")
    else:
        apellidos = texto + " " + texto2
        datos = buscarestudiante(apellidos)
        if datos != "vacio":
            error.config(text="                                                                                                ")
            tabla3.delete(*tabla3.get_children())
            for dato in datos:
                tabla3.insert("", "end", values=dato)
        else:
            error.config(text="No se encontraron resultados               ")
def volver1(tabla3,ventana3):
    tabla3.delete(*tabla3.get_children())
    llenartabla2()
    ventana3.withdraw()
def llenartabla2(tabla3):
    datos = mostrar_estudiante()
    for dato in datos:
        tabla3.insert("", "end", values=dato)
def center_content(tree, column):
    tree.heading(column, anchor='center')
    tree.column(column, anchor='center')

def modificarE(event,tabla3,ventana2,ventana3):
    if tabla3.selection():  # Verificar si hay elementos seleccionados
        selected_item = tabla3.selection()[0]
        # Resto de tu lógica aquí
    else:
        # No hay elementos seleccionados, puedes manejar esto según tu lógica
        pass
    values = tabla3.item(selected_item, "values")
    ventana3.withdraw()
    ventana2.deiconify()

def inicio(ventana3):
    ventana3.withdraw()
    
def IngresarHora(root,ancho,alto):
    ventana3 = Toplevel(root)
    ventana3.title("Agregar Horas")
    ventana3.geometry(f"{ancho}x{alto}")
    ventana3.config(bg="white")
    ventana3.iconbitmap("image/logo-escuela-de-ciencias.ico")

    frame5=Frame(ventana3)
    frame5.pack(fill="both", expand="True")
    frame5.config(bg="white")
    frame5.config(bd=21)
    frame5.config(relief="groove")

    titulo3 = Frame(frame5, width=ancho, height=alto/12, bg="white")
    titulo3.pack()

    label3 = Label(titulo3, text="AGRAGAR HORAS", font=("Arial", 17, "bold italic"), bg="white")
    label3.pack()
    label3.place(x=ancho/2.7, y=2)

    imagen5 = PhotoImage(file="image/flecha.png")
    imagen_redimensionada5 = imagen5.subsample(5, 5)  

    boton8 = Button(titulo3, image=imagen_redimensionada5, width=40, height=20, command=lambda:volver1(tabla3,ventana3), bg="white", borderwidth=0)
    boton8.pack()
    boton8.place(x=10, y=10)  

    # Crear el contenedor1
    contenedor3 = Frame(frame5, width=ancho, height=alto/2, bg="white")
    contenedor3.pack()
    contenedor3.grid_propagate(False)  # Desactiva la propagación de la cuadrícula en el contenedor1

    # Crear la caja de entrada dentro de contenedor1
    apellido1=Label(contenedor3,text="Apellido paterno:",bg="white").place(x=320,y=10)
    apellido2=Label(contenedor3,text="Apellido materno:",bg="white").place(x=470,y=10)
    entrada3 = Entry(contenedor3)
    entrada3.place(x=320,y=30)
    entrada3.config(relief="solid")
    entrada4 = Entry(contenedor3)
    entrada4.place(x=470,y=30)
    entrada4.config(relief="solid")
    # Crear un botón para obtener el texto ingresado
    botonb = Button(contenedor3, text="Buscar", command=lambda:obtener_texto2(entrada3,entrada4,contenedor3,tabla3),bg="black",fg="white")
    botonb.place(x=620,y=30)

    tabla3 = ttk.Treeview(contenedor3, columns=("id","Apellidos", "Nombre(s)", "Semestre"), show="headings")
    tabla3.heading("id", text="id")
    tabla3.heading("Apellidos", text="Apellidos")
    tabla3.heading("Nombre(s)", text="Nombre(s)")
    tabla3.heading("Semestre", text="Semestre")
    tabla3.column("#1",width=20)
    tabla3.place(x=250,y=60)
    center_content(tabla3, "Semestre")
    llenartabla2(tabla3)
    tabla3.bind("<<TreeviewSelect>>", modificarE)
    ventana3.protocol("WM_DELETE_WINDOW", inicio(ventana3))