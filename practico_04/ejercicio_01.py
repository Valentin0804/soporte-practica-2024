"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3

def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """
    conexion = sqlite3.connect('mpruebasoporte.db')
    cursor = conexion.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Persona (
            IdPersona INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre TEXT(30),
            FechaNacimiento DATE,
            DNI INTEGER,
            Altura INTEGER
        )
    ''')
    
    conexion.commit()
    conexion.close()
    pass # Completar


def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    conexion = sqlite3.connect('pruebasoporte.db')
    cursor = conexion.cursor()
    
    cursor.execute('''
        DROP TABLE IF EXISTS Persona
    ''')
    
    conexion.commit()
    conexion.close()
    pass # Completar


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
