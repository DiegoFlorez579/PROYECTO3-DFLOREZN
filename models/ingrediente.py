#Importar abc para manejo de clases abstractas:
from abc import ABC, abstractmethod
from models.funciones import es_sano

#Crea la clase abstracta Ingredientes:
class Ingredientes(ABC):
    def __init__(self, precio: int, calorias: float, nombre: str, inventario: int, es_vegetariano: bool) -> None:
        self._precio = precio
        self._calorias = calorias
        self._nombre = nombre
        self._inventario = inventario
        self._es_vegetariano = es_vegetariano

    #Metodos "abastecer" y "es_sano":   
    @abstractmethod
    def abastecer() -> None:
        pass

    def es_sano(self) -> bool:
        return(es_sano(self._calorias, self._es_vegetariano))

    #Getters y setters de todos los atributos:
    @property
    def precio(self) -> int:
        return self._precio

    @precio.setter
    def precio(self, precio:int) -> None:
        self._precio = precio

    @property
    def calorias(self) -> float:
        return self._calorias

    @calorias.setter
    def calorias(self, calorias:float) -> None:
        self._calorias = calorias

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nombre:str) -> None:
        self._nombre = nombre

    @property
    def inventario(self) -> int:
        return self._inventario

    @inventario.setter
    def inventario(self, inventario:int) -> None:
        self._inventario = inventario

    @property
    def es_vegetariano(self) -> bool:
        return self._es_vegetariano

    @es_vegetariano.setter
    def es_vegetariano(self, es_vegetariano:bool) -> None:
        self._es_vegetariano = es_vegetariano

