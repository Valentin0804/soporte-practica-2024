"""Base de Datos SQL - Creación de tablas auxiliares"""

import sqlite3
from practico_04.ejercicio_01 import borrar_tabla, crear_tabla


def crear_tabla_peso():
    """Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
        - IdPersona: Int() (Clave Foranea Persona)
        - Fecha: Date()
        - Peso: Int()
    """
    conexion = sqlite3.connect('mpruebasoporte.db')
    cursor = conexion.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Persona (
            IdPersona INTEGER FORENG KEY AUTOINCREMENT,
            Fecha DATE,
            Peso INTEGER)''')
    
    conexion.commit()
    conexion.close()
    pass # Completar


def borrar_tabla_peso():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    conexion = sqlite3.connect('mpruebasoporte.db')
    cursor = conexion.cursor()

    cursor.execute(''' DROP TABLE IF EXISTS Persona ''')
    pass # Completar


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
