from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functions import obtener_tamaño_pantalla,on_button_click
from model import mostrar_estudiante, ConsultarHoras,buscarestudiante,AgregarHoras,EliminarH
from model import AgregarEstudiante as nuevo
from model import Modificarhoras as Mhoras
indice=[]
root = Tk()
root.title("Registro de horas extracurriculares")
root.config(bg="white")
ancho, alto = obtener_tamaño_pantalla(root)
root.geometry(f"{ancho}x{alto}")
root.iconbitmap("image/logo-escuela-de-ciencias.ico")

def on_cerrar_ventana():
    root.destroy()
def cerrar_C():
    ventana3.destroy()

def consulta_estudiante():
    indice.append(1)
    ventana3.deiconify()

def ModificarEstudiante():
    indice.append(3)
    ventana3.deiconify()

def inicio():
    root.deiconify()
    ventana.withdraw()
    ventana2.withdraw()
    ventana3.withdraw()
    ventana4.withdraw()
    ventana5.withdraw()
    ventana6.withdraw()
    ventana7.withdraw()
    if usuario:
        usuario.pop(0)
    if indice:
        indice.pop(0)
    if horas:
        horas.pop(0)

def cerrar_exito():
    if indice[0]==2:
        tallerbox.delete(0,END)
        Documentobox.delete(0,END)  
        Duracionbox.delete(0,END)  
        HorasEbox.delete(0,END)  
        infbox.delete(0,END)  
        opcion_seleccionada.set("Selecciona una opción")

    ventana.withdraw()
    ventana5.withdraw()

def volver1():
    tabla3.delete(*tabla3.get_children())
    llenartabla2()
    if indice:
        indice.pop(0)
    ventana3.withdraw()
    ventana2.withdraw()

def volver3():
    root.deiconify()
    tabla3.delete(*tabla3.get_children())
    if indice:
        indice.pop(0)
    llenartabla2()
    ventana3.withdraw()

def volver4():
    if horas:
        horas.pop(0)
    ventana2.deiconify()
    ventana7.withdraw()
    tabla2.delete(*tabla2.get_children())
    on_select(usuario[0])
    
def volver2():
    ventana4.withdraw()
    tabla3.delete(*tabla3.get_children())
    llenartabla2()
    ventana3.deiconify()
    ventana6.withdraw()
    if usuario:
        usuario.pop(0)

def agregahoras():
    indice.append(2)
    ventana3.deiconify()

def regreso1():
    vBandera=1#esta variable es provicional en lo que se hacen las conexiones con la base de datos
    if usuario:
        usuario.pop(0)
    if vBandera==1:
        tabla2.delete(*tabla2.get_children())
        ventana2.withdraw()
        ventana3.deiconify()

def obtener_texto2():
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



def center_content(tree, column):
    tree.heading(column, anchor='center')
    tree.column(column, anchor='center')

def on_select(values):
    ventana3.withdraw()
    ventana2.deiconify()
    nombre=values[1]+" "+values[2]+"                                    "
    apellido1_1=Label(contenedor2,text=nombre,bg="white",font=("Arial", 10, "bold italic")).place(x=100,y=10)
    datos = ConsultarHoras(values[0])
    for dato in datos:
        tabla2.insert("", "end", values=dato)
def modificarH(event):
    if tabla2.selection():  # Verificar si hay elementos seleccionados
        selected_item = tabla2.selection()[0]
        values = tabla2.item(selected_item, "values")
        horas.append(values)
        ventana7.deiconify()
        ventana2.withdraw()
        Llenarhoras(values)
        
    
def modificarE(event):
    if tabla3.selection(): 
        selected_item = tabla3.selection()[0]
        values = tabla3.item(selected_item, "values")
        usuario.append(values)
        if indice[0]==1:
            on_select(values)
        elif indice[0]==2:
            ventana3.withdraw()
            ventana4.deiconify()
        else:
            ventana3.withdraw()
            ventana6.deiconify()
    else:
        pass
    
    

def llenartabla2():
    datos = mostrar_estudiante()
    for dato in datos:
        tabla3.insert("", "end", values=dato)

def calcularhora(opcion,texto3):
    if opcion=="Asistir":
        if texto3>25:
            texto3 *=0.2
            return texto3
        else:
            texto3 *=0.12
            return texto3
    elif opcion=="Impartir":
        if texto3>25:
            texto3 *=0.4
            return texto3
        else:
            texto3 *=0.2
            return texto3

def newhours():
    print(usuario)
    texto = tallerbox.get()
    texto2 = Documentobox.get()
    opcion=opcion_seleccionada.get()
    fallo=True
    label=Label(frame6,fg="red")
    label.place(x=ancho/3,y=520)
    try:
        texto3 = float(Duracionbox.get())
    except:
        fallo=False
    try:
        texto4 = HorasEbox.get()
        if texto4!="":
            texto4 = float(texto4)
    except:
        fallo=False
    texto5 = infbox.get()
    if texto !="" and fallo and texto3!="":
        if texto2=="":
            texto2="VACIO"
        if texto5=="":
            texto5="VACIO"
        if texto4 =="":
            if opcion!="Seleccione una opción":
                texto4=calcularhora(opcion,texto3)
                texto4=round(texto4,2)
                AgregarHoras(usuario[0][0],texto,texto2,texto3,texto4,texto5)
                ventana.deiconify()  
                label.config(text="                                                                                        ") 
            else:
                label.config(text="Selecciona un tipo de taller. asistir/impartir                ")
        else:
            AgregarHoras(usuario[0][0],texto,texto2,texto3,texto4,texto5)
            ventana.deiconify()  
            label.config(text="                                                                                        ")

    else:
        label.config(text="Valores no adecuados                                                                        ")
    
def AgregarEstudiante():
    ventana5.deiconify()

def NuevoEstudiante():
    Apellidop=apellidopbox.get()
    Apellidom=apellidombox.get()
    Nombre=nombrebox.get()
    Semestre=semestrebox.get()
    label8=Label(frame7,fg="red")
    label8.place(x=ancho/2.6,y=650)
    verdadero=True
    try:
        if Semestre !="":
            Semestre=int(Semestre)
    except:
        verdadero=False


    if Apellidop != "" and Apellidom != "" and Nombre != "" and Semestre != "" and verdadero:
        Apellidos= Apellidop+" "+Apellidom
        resultado=nuevo(Apellidos,Nombre,Semestre)
        if resultado=="exito":
            ventana.deiconify()
            label8.config(text="                                                              ")
        else:
            label8.config(text="Ya existe este estudiante            ")
    else:
        label8.config(text="Valores de estudiante no validos        ")
        

def Llenarhoras(values):
    tallerbox2.delete(0,END)  
    tallerbox2.insert(0, values[1])  
    Documentobox2.delete(0,END)  
    Documentobox2.insert(0, values[2])  
    Duracionbox2.delete(0,END)  
    Duracionbox2.insert(0, values[3])
    HorasEbox2.delete(0,END)  
    HorasEbox2.insert(0, values[4])
    infbox2.delete(0,END)  
    infbox2.insert(0, values[5])
    duracion=float(values[3])
    extras=float(values[4])
    if duracion<25:
        auxiliar=extras%0.12
        if auxiliar==0:
            opcion_seleccionada2.set("Asistir")
        else:
            opcion_seleccionada2.set("Impartir")
    else:
        auxiliar=extras%0.2
        if auxiliar==0:
            opcion_seleccionada2.set("Asistir")
        else:
            opcion_seleccionada2.set("Impartir")
def Modificarhoras():
    root.withdraw()
    label=Label(frame9,fg="red")
    label.place(x=ancho/3,y=520)
    verdadero=True
    texto1=tallerbox2.get()
    texto2=Documentobox2.get()
    try:
        texto3=Duracionbox2.get()
        if texto3!="":
            texto3=float(texto3)
    except:
        verdadero=False
    try:
        texto4=HorasEbox2.get()
        if texto4!="":
            texto4=float(texto4)
    except:
        verdadero=False
    texto5=infbox2.get()
    texto6=opcion_seleccionada2.get()
    verifica=float(horas[0][4])
    if verdadero and texto1!="" and texto3!="" and texto2!="" and texto5!="":
        if texto4 == verifica or texto4=="":#en este lado verificamos si hemos modificado las horas si es así ya no se verifica el asistir o impartir
            texto4=calcularhora(texto6,texto3)
            texto4=round(texto4,2)
            resultado = messagebox.askyesno("Confirmación", "¿Estás seguro de modificar la hora?")
            if resultado:
                Mhoras(texto1,texto2,texto3,texto4,texto5,horas[0][0])
                volver4()
                label.config(text="                                                                                                                ")
        else:
            resultado = messagebox.askyesno("Confirmación", "¿Estás seguro de modificar la hora?")
            if resultado:
                Mhoras(texto1,texto2,texto3,texto4,texto5,horas[0][0])
                volver4()
                label.config(text="                                                                                                                     ")
    else:
        label.config(text="Valores invalidos/no pueden haber valores vacios solo el de horas")

def EliminarHora():
    root.withdraw()
    resultado = messagebox.askyesno("Confirmación", "¿Estás seguro de eliminar la hora?")
    if resultado:
        id=horas[0][0]
        EliminarH(id)
        volver4()

miFrame=Frame()
miFrame.pack(fill="both", expand="True")
miFrame.config(bg="white")
miFrame.config(bd=21)
miFrame.config(relief="groove")

label1=Label(miFrame, text="HORAS EXTRACURRICULARES",font=("Arial", 17, "bold italic"),bg="white").place(x=ancho/2.7, y=2)

frame2 = Frame(miFrame, width=ancho/2, height=alto/2.3, bg="white")
frame2.pack(side="right")

frame2.grid_propagate(False)  # Evita que el Frame se ajuste al tamaño de sus widgets

boton1 = Button(frame2, text="Agregar Horas", bg="#0067E0", command=agregahoras, fg="white", width=40, height=5)
boton1.grid(row=0, column=0, pady=(50, 0))  # Ajusta el pady para centrar verticalmente

boton2 = Button(frame2, text="Agregar Estudiante", bg="#0067E0", command=AgregarEstudiante, fg="white", width=40, height=5)
boton2.grid(row=1, column=0, pady=10)

boton3 = Button(frame2, text="Consultar Estudiante", bg="#0067E0", command=consulta_estudiante, fg="white", width=40, height=5)
boton3.grid(row=2, column=0, pady=10)

boton4 = Button(frame2, text="Modificar Estudiante", bg="#0067E0", command=ModificarEstudiante, fg="white", width=40, height=5)
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

imagen4 = PhotoImage(file="image/inicio.png")
imagen_redimensionada4 = imagen4.subsample(25, 25)

boton7 = Button(titulo2, image=imagen_redimensionada4, width=40, height=20, command=inicio, bg="white", borderwidth=0)
boton7.pack()
boton7.place(x=(ancho/10)*8, y=20)  

contenedor2 = Frame(frame4, width=ancho, height=alto/2, bg="white")
contenedor2.pack()
contenedor2.grid_propagate(False)  # Desactiva la propagación de la cuadrícula en el contenedor1


tabla2 = ttk.Treeview(contenedor2, columns=("ID","Taller", "Documento", "Duracion","Horas extra","inf. recuperada"), show="headings")
tabla2.heading("ID", text="ID")
tabla2.heading("Taller", text="Taller")
tabla2.heading("Documento", text="Documento")
tabla2.heading("Duracion", text="duracion")
tabla2.heading("Horas extra", text="Horas extra")
tabla2.heading("inf. recuperada", text="inf. recuperada")
center_content(tabla2, "Taller")
center_content(tabla2, "Documento")
center_content(tabla2, "Duracion")
center_content(tabla2, "Horas extra")
center_content(tabla2, "inf. recuperada")
tabla2.column("#1",width=20)
tabla2.place(x=60,y=60)
tabla2.bind("<<TreeviewSelect>>", modificarH)
#----------------------------tabla de estudiantes---------------------------------------
ventana3 = Toplevel(root)
ventana3.title("Consulta estudiante")
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

label3 = Label(titulo3, text="ESTUDIANTES", font=("Arial", 17, "bold italic"), bg="white")
label3.pack()
label3.place(x=ancho/2.7, y=2)

imagen5 = PhotoImage(file="image/flecha.png")
imagen_redimensionada5 = imagen5.subsample(5, 5)  

boton8 = Button(titulo3, image=imagen_redimensionada5, width=40, height=20, command=volver3, bg="white", borderwidth=0)
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
botonb = Button(contenedor3, text="Buscar", command=obtener_texto2,bg="black",fg="white")
botonb.place(x=620,y=30)

tabla3 = ttk.Treeview(contenedor3, columns=("id","Apellidos", "Nombre(s)", "Semestre"), show="headings")
tabla3.heading("id", text="id")
tabla3.heading("Apellidos", text="Apellidos")
tabla3.heading("Nombre(s)", text="Nombre(s)")
tabla3.heading("Semestre", text="Semestre")
tabla3.column("#1",width=20)
tabla3.place(x=250,y=60)
center_content(tabla3, "Semestre")
center_content(tabla3, "Apellidos")
center_content(tabla3, "Nombre(s)")
llenartabla2()
tabla3.bind("<<TreeviewSelect>>", modificarE)
##---------------------ventana para agregar horas---------------------##
usuario=[]
ventana4 = Toplevel(root)
ventana4.title("Agregar Horas")
ventana4.geometry(f"{ancho}x{alto}")
ventana4.config(bg="white")
ventana4.iconbitmap("image/logo-escuela-de-ciencias.ico")

frame6=Frame(ventana4)
frame6.pack(fill="both", expand="True")
frame6.config(bg="white")
frame6.config(bd=21)
frame6.config(relief="groove")

titulo4 = Frame(frame6, width=ancho, height=alto/12, bg="white")
titulo4.pack()

label4 = Label(titulo4, text="AGREGAR HORAS", font=("Arial", 17, "bold italic"), bg="white")
label4.pack()
label4.place(x=ancho/2.7, y=2)

imagen6 = PhotoImage(file="image/flecha.png")
imagen_redimensionada6 = imagen6.subsample(5, 5)  

boton9 = Button(titulo4, image=imagen_redimensionada6, width=40, height=20, command=volver2, bg="white", borderwidth=0)
boton9.pack()
boton9.place(x=10, y=10)  

imagen7 = PhotoImage(file="image/inicio.png")
imagen_redimensionada7 = imagen7.subsample(25, 25)

boton10 = Button(titulo4, image=imagen_redimensionada7, width=40, height=20, command=inicio, bg="white", borderwidth=0)
boton10.pack()
boton10.place(x=(ancho/10)*8, y=20)  

taller=Label(frame6,text="Taller/Curso:",bg="white",font=("Arial", 9, "bold italic")).place(x=ancho/3,y=100)
tallerbox=Entry(frame6,width=50)
tallerbox.place(x=ancho/3,y=130)
tallerbox.config(relief="solid")

Documento=Label(frame6,text="Documento(Opcional):",bg="white",font=("Arial", 9, "bold italic")).place(x=ancho/3,y=160)
Documentobox=Entry(frame6,width=50)
Documentobox.place(x=ancho/3,y=190)
Documentobox.config(relief="solid")

Duracion=Label(frame6,text="Duracion:",bg="white",font=("Arial", 9, "bold italic")).place(x=ancho/3,y=220)
Duracionbox=Entry(frame6,width=50)
Duracionbox.place(x=ancho/3,y=250)
Duracionbox.config(relief="solid")

HorasE=Label(frame6,text="Horas Extras(opcional):",bg="white",font=("Arial", 9, "bold italic")).place(x=ancho/3,y=280)
HorasEbox=Entry(frame6,width=50)
HorasEbox.place(x=ancho/3,y=320)
HorasEbox.config(relief="solid")

inf=Label(frame6,text="Informacion recuperada(opcional):",bg="white",font=("Arial", 9, "bold italic")).place(x=ancho/3,y=350)
infbox=Entry(frame6,width=50)
infbox.place(x=ancho/3,y=380)
infbox.config(relief="solid")

tipo=Label(frame6,text="Tipo:",bg="white",font=("Arial", 9, "bold italic")).place(x=ancho/3,y=420)
opcion_seleccionada = StringVar(frame6)
opcion_seleccionada.set("Seleccione una opción")
option_menu = OptionMenu(frame6, opcion_seleccionada, "Asistir", "Impartir")
option_menu.place(x=ancho/3,y=450)

botonF = Button(frame6, text="Agregar", command=newhours,bg="black",fg="white")
botonF.place(x=ancho/3,y=480)
#----------------------ventana de exito---------------------------------------
ventana = Toplevel(root)
ventana.title("Agregar Horas")
ventana.geometry(f"{500}x{300}")
ventana.config(bg="white")
ventana.iconbitmap("image/logo-escuela-de-ciencias.ico")

frame3=Frame(ventana)
frame3.pack(fill="both", expand="True")
frame3.config(bg="white")
frame3.config(bd=21)

imagen8 = PhotoImage(file="image/descarga.png")
imagen_redimensionada8 = imagen8.subsample(2, 2)
exito=Label(frame3,image=imagen_redimensionada8)
#exito.place(x=100,y=70)
exito.pack()

registro=Label(frame3,text="Registro Exitoso",font=("Arial", 15, "bold italic"))
#registro.place(x=190,y=90)
registro.pack()

cerrar=Button(frame3,text="Cerrar",command=cerrar_exito,font=("Arial", 11),height=1,width=5,bg="#02ACE2")
cerrar.pack()

#--------------------------ventana para agregar un nuevo estudiante--------------------
ventana5 = Toplevel(root)
ventana5.title("Agregar estudiante")
ventana5.geometry(f"{ancho}x{alto}")
ventana5.config(bg="white")
ventana5.iconbitmap("image/logo-escuela-de-ciencias.ico")

frame7=Frame(ventana5)
frame7.pack(fill="both", expand="True")
frame7.config(bg="white")
frame7.config(bd=21)
frame7.config(relief="groove")

titulo5 = Frame(frame7, width=ancho, height=alto/12, bg="white")
titulo5.pack()

label5 = Label(titulo5, text="AGREGAR ESTUDIANTE", font=("Arial", 17, "bold italic"), bg="white")
label5.pack()
label5.place(x=ancho/2.7, y=2)

imagen9 = PhotoImage(file="image/flecha.png")
imagen_redimensionada9 = imagen9.subsample(5, 5)  

boton11 = Button(titulo5, image=imagen_redimensionada9, width=40, height=20, command=inicio, bg="white", borderwidth=0)
boton11.pack()
boton11.place(x=10, y=10)  

imagen10 = PhotoImage(file="image/inicio.png")
imagen_redimensionada10 = imagen10.subsample(25, 25)

boton12 = Button(titulo5, image=imagen_redimensionada10, width=40, height=20, command=inicio, bg="white", borderwidth=0)
boton12.pack()
boton12.place(x=(ancho/10)*8, y=20)  

imagen11=PhotoImage(file="image/usuario.png")

perfil=Label(frame7,image=imagen11)
perfil.pack()

apellidop=Label(frame7,text="Apellido paterno:",font=("Arial", 12, "italic"))
apellidop.place(x=ancho/2.6,y=350)
apellidopbox=Entry(frame7,width=50,relief=SOLID)
apellidopbox.place(x=ancho/2.6,y=380)

apellidom=Label(frame7,text="Apellido materno:",font=("Arial", 12, "italic"))
apellidom.place(x=ancho/2.6,y=420)
apellidombox=Entry(frame7,width=50,relief=SOLID)
apellidombox.place(x=ancho/2.6,y=450)

nombre=Label(frame7,text="Nombre(s):",font=("Arial", 12, "italic"))
nombre.place(x=ancho/2.6,y=480)
nombrebox=Entry(frame7,width=50,relief=SOLID)
nombrebox.place(x=ancho/2.6,y=520)

semestre=Label(frame7,text="Semestre:",font=("Arial", 12, "italic"))
semestre.place(x=ancho/2.6,y=550)
semestrebox=Entry(frame7,width=50,relief=SOLID)
semestrebox.place(x=ancho/2.6,y=580)

enviar=Button(frame7,text="Enviar",font=("Arial", 12, "italic"),fg="white",bg="black",command=NuevoEstudiante)
enviar.place(x=ancho/2.6,y=620)

#--+--------------------Modificar estudiante--------------------------+--#
ventana6 = Toplevel(root)
ventana6.title("Modificar estudiante")
ventana6.geometry(f"{ancho}x{alto}")
ventana6.config(bg="white")
ventana6.iconbitmap("image/logo-escuela-de-ciencias.ico")

frame8=Frame(ventana6)
frame8.pack(fill="both", expand="True")
frame8.config(bg="white")
frame8.config(bd=21)
frame8.config(relief="groove")

titulo6 = Frame(frame8, width=ancho, height=alto/12, bg="white")
titulo6.pack()

label6 = Label(titulo6, text="MODIFICAR ESTUDIANTE", font=("Arial", 17, "bold italic"), bg="white")
label6.pack()
label6.place(x=ancho/2.7, y=2)

imagen12 = PhotoImage(file="image/flecha.png")
imagen_redimensionada12 = imagen12.subsample(5, 5)  

boton13 = Button(titulo6, image=imagen_redimensionada12, width=40, height=20, command=volver2, bg="white", borderwidth=0)
boton13.pack()
boton13.place(x=10, y=10)  

imagen13 = PhotoImage(file="image/inicio.png")
imagen_redimensionada13 = imagen13.subsample(25, 25)

boton14 = Button(titulo6, image=imagen_redimensionada13, width=40, height=20, command=inicio, bg="white", borderwidth=0)
boton14.pack()
boton14.place(x=(ancho/10)*8, y=20)  

imagen14=PhotoImage(file="image/usuario.png")

perfil2=Label(frame8,image=imagen14)
perfil2.pack()

apellidop2=Label(frame8,text="Apellido paterno:",font=("Arial", 12, "italic"))
apellidop2.place(x=ancho/2.6,y=350)
apellidopbox2=Entry(frame8,width=50,relief=SOLID)
apellidopbox2.place(x=ancho/2.6,y=380)

apellidom2=Label(frame8,text="Apellido materno:",font=("Arial", 12, "italic"))
apellidom2.place(x=ancho/2.6,y=420)
apellidombox2=Entry(frame8,width=50,relief=SOLID)
apellidombox2.place(x=ancho/2.6,y=450)

nombre2=Label(frame8,text="Nombre(s):",font=("Arial", 12, "italic"))
nombre2.place(x=ancho/2.6,y=480)
nombrebox2=Entry(frame8,width=50,relief=SOLID)
nombrebox2.place(x=ancho/2.6,y=520)

semestre2=Label(frame8,text="Semestre:",font=("Arial", 12, "italic"))
semestre2.place(x=ancho/2.6,y=550)
semestrebox2=Entry(frame8,width=50,relief=SOLID)
semestrebox2.place(x=ancho/2.6,y=580)

enviar2=Button(frame8,text="Modificar",font=("Arial", 12, "italic"),fg="white",bg="black")
enviar2.place(x=ancho/2.6,y=620)
eliminar=Button(frame8,text="Eliminar",font=("Arial", 12, "italic"),fg="white",bg="black")
eliminar.place(x=(ancho/2.6)+100,y=620)

##--------------ventana para modificar horas---------------------##
usuario=[]
horas=[]
ventana7 = Toplevel(root)
ventana7.title("Agregar Horas")
ventana7.geometry(f"{ancho}x{alto}")
ventana7.config(bg="white")
ventana7.iconbitmap("image/logo-escuela-de-ciencias.ico")

frame9=Frame(ventana7)
frame9.pack(fill="both", expand="True")
frame9.config(bg="white")
frame9.config(bd=21)
frame9.config(relief="groove")

titulo7 = Frame(frame9, width=ancho, height=alto/12, bg="white")
titulo7.pack()

label7 = Label(titulo7, text="MODIFICAR HORAS", font=("Arial", 17, "bold italic"), bg="white")
label7.pack()
label7.place(x=ancho/2.7, y=2)

imagen15 = PhotoImage(file="image/flecha.png")
imagen_redimensionada15 = imagen15.subsample(5, 5)  
 
boton15 = Button(titulo7, image=imagen_redimensionada15, width=40, height=20, command=volver4, bg="white", borderwidth=0)
boton15.pack()
boton15.place(x=10, y=10)  

imagen16 = PhotoImage(file="image/inicio.png")
imagen_redimensionada16 = imagen16.subsample(25, 25)

boton16 = Button(titulo7, image=imagen_redimensionada16, width=40, height=20, command=inicio, bg="white", borderwidth=0)
boton16.pack()
boton16.place(x=(ancho/10)*8, y=20)  

taller2=Label(frame9,text="Taller/Curso:",bg="white",font=("Arial", 9, "bold italic")).place(x=ancho/3,y=100)
tallerbox2=Entry(frame9,width=50)
tallerbox2.place(x=ancho/3,y=130)
tallerbox2.config(relief="solid")

Documento2=Label(frame9,text="Documento(Opcional):",bg="white",font=("Arial", 9, "bold italic")).place(x=ancho/3,y=160)
Documentobox2=Entry(frame9,width=50)
Documentobox2.place(x=ancho/3,y=190)
Documentobox2.config(relief="solid")

Duracion2=Label(frame9,text="Duracion:",bg="white",font=("Arial", 9, "bold italic")).place(x=ancho/3,y=220)
Duracionbox2=Entry(frame9,width=50)
Duracionbox2.place(x=ancho/3,y=250)
Duracionbox2.config(relief="solid")

HorasE2=Label(frame9,text="Horas Extras(opcional):",bg="white",font=("Arial", 9, "bold italic")).place(x=ancho/3,y=280)
HorasEbox2=Entry(frame9,width=50)
HorasEbox2.place(x=ancho/3,y=320)
HorasEbox2.config(relief="solid")

inf2=Label(frame9,text="Informacion recuperada(opcional):",bg="white",font=("Arial", 9, "bold italic")).place(x=ancho/3,y=350)
infbox2=Entry(frame9,width=50)
infbox2.place(x=ancho/3,y=380)
infbox2.config(relief="solid")

tipo2=Label(frame9,text="Tipo:",bg="white",font=("Arial", 9, "bold italic")).place(x=ancho/3,y=420)
opcion_seleccionada2 = StringVar(frame9)
opcion_seleccionada2.set("Seleccione una opción")
option_menu2 = OptionMenu(frame9, opcion_seleccionada2, "Asistir", "Impartir")
option_menu2.place(x=ancho/3,y=450)

botonF2 = Button(frame9, text="Modificar", command=Modificarhoras,bg="black",fg="white")
botonF2.place(x=ancho/3,y=490)
eliminar = Button(frame9, text="Eliminar", command=EliminarHora,bg="black",fg="white")
eliminar.place(x=(ancho/3)+100,y=490)

ventana.protocol("WM_DELETE_WINDOW", cerrar_exito) 
ventana2.protocol("WM_DELETE_WINDOW", inicio) 
ventana3.protocol("WM_DELETE_WINDOW", inicio) 
ventana4.protocol("WM_DELETE_WINDOW", inicio) 
ventana5.protocol("WM_DELETE_WINDOW", inicio) 
ventana6.protocol("WM_DELETE_WINDOW", inicio) 
ventana7.protocol("WM_DELETE_WINDOW", inicio) 

ventana.withdraw()
ventana2.withdraw()
ventana3.withdraw()
ventana4.withdraw()
ventana5.withdraw()
ventana6.withdraw()
ventana7.withdraw()

root.protocol("WM_DELETE_WINDOW", on_cerrar_ventana)


root.mainloop()