"""En este archivo se debe importar el archivo:
- ./util.py as util
- ./data/database.py as database
- ../config/test_config.py as test_config
- ../config/db_config/migrations.py as migrations
- ../../main.py as main

Los imports deben hacerse de forma tal que funcionen con el siguiente
comando (estando parados dentro de la carpeta practico_02):
$PATH$/practico_02> python -m source.ejercicio_02
"""

# Completar 
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'data')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'config')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'config/db_config')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import  util
import  database as database
import  test_config as test_config
import  migrations as migrations
import  main

# NO MODIFICAR - INICIO
assert main.name == "main"
assert util.name == "util"
assert database.name == "database"
assert test_config.name == "test_config"
assert migrations.name == "migrations"
# NO MODIFICAR - FIN


# El siguiente ejercicio se encuentra en source/controller/ejercicio_03.py
