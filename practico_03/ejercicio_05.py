"""Propiedades"""


class Auto:

    def __init__(self, precio: float, marca:str):
        self._precio = precio
        self._marca = marca.capitalize()

    @property
    def precio(self) -> float:
        return round(self._precio, 2)
    
    @precio.setter
    def precio(self, nuevo_precio: float):
        self._precio = nuevo_precio

    @property
    def marca(self) -> str:
        return self._marca
        
    """La clase auto tiene dos propiedades, precio y marca. La marca se define
    obligatoriamente al construir la clase y siempre que se devuelve, se 
    devuelve con la primer letra en mayúscula y no se puede modificar. El precio
    puede modificarse pero cuando se muestra, se redondea a 2 decimales
    
    Restricción: Usar Properties
    
    Referencia: https://docs.python.org/3/library/functions.html#property"""

    # Completar


# NO MODIFICAR - INICIO
auto = Auto("Ford", 12875.456)

assert auto._marca == "Ford"
assert auto._precio == 12875.46
auto._precio = 13874.349
assert auto._precio == 13874.35

try:
    auto._marca = "Chevrolet"
    assert False
except AttributeError:
    assert True
# NO MODIFICAR - FIN


###############################################################################


from dataclasses import dataclass

@dataclass
class Auto:
    """Re-Escribir utilizando DataClasses"""

    _precio : float
   # _marca: str = field(init=False)
    marca: str

    def __post_init__(self):
        self._marca = self.marca.capitalize()
    
    @property
    def precio(self) -> float:
        return round(self._precio, 2)

    @precio.setter
    def precio(self, nuevo_precio: float):
        self._precio = nuevo_precio

    @property
    def marca(self) -> str:
        return self._marca

    # Completar


# NO MODIFICAR - INICIO
auto = Auto("Ford", 12875.456)

assert auto._marca == "Ford"
assert auto._precio == 12875.46
auto._precio = 13874.349
assert auto._precio == 13874.35

try:
    auto._marca = "Chevrolet"
    assert False
except AttributeError:
    assert True
# NO MODIFICAR - FIN
