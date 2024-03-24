import sqlite3

conexion=sqlite3.connect("horasdb.db")
cursor=conexion.cursor()

def mostrar_estudiante():
    lista=[]
    sql="SELECT * FROM Estudiantes"
    cursor.execute(sql)
    resultado=cursor.fetchall()
    for datos in resultado:
        lista.append(datos)
    return lista

def ConsultarHoras(id):
    list=[]
    sql=f"SELECT * FROM Registro where id_estudiante='{id}'"
    cursor.execute(sql)
    resultado=cursor.fetchall()
    for dato in resultado:
        list.append((dato[2],dato[3],dato[4],dato[5],dato[6]))
    return list

def buscarestudiante(apellidos):
    sql=f"SELECT * FROM Estudiantes where Apellidos='{apellidos}'"
    cursor.execute(sql)
    resultado=cursor.fetchall()
    if resultado:
        return resultado
    else:
        no="vacio"
        return no

def AgregarHoras(id,taller,documento,duracion,horas,inf):
    sql=f"INSERT INTO Registro(id_estudiante,Taller,Documento,Duracion,Hrs_extras,inf_recuperada)VALUES({id},'{taller}','{documento}',{duracion},{horas},'{inf}')"
    cursor.execute(sql)
    conexion.commit()
