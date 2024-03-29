
def obtener_tamaño_pantalla(root):
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()

    alto_barra_tareas = root.winfo_screenmmheight() - root.winfo_vrootheight()

    return ancho_pantalla, alto_pantalla - alto_barra_tareas


