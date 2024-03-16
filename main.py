from tkinter import *
from functions import obtener_tamaño_pantalla,on_button_click

root = Tk()
root.title("Registro de horas extracurriculares")
root.config(bg="white")
ancho, alto = obtener_tamaño_pantalla(root)

def on_cerrar_ventana():
    root.destroy()

def consulta_estudiante():#Cuando cree otra interfaz se pone ventana.whitdraw() para cerrar la ventana
    ventana.deiconify()

def inicio():
    ventana.withdraw()


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
root.iconbitmap("image/logo-escuela-de-ciencias.ico")

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


ventana.withdraw()
root.protocol("WM_DELETE_WINDOW", on_cerrar_ventana)


root.mainloop()