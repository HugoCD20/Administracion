import sqlite3

conexion=sqlite3.connect("horasdb.db")
cursor=conexion.cursor()

def mostrar_estudiante():
    lista=[]
    sql="SELECT * FROM Estudiantes"
    cursor.execute(sql)
    resultado=cursor.fetchall()
    for datos in resultado:
        lista.append((datos[1],datos[2],datos[3]))
    return lista