from models.iproducto import IProducto
from models.funciones import costos, rentabilidad
from models.base import Base
from models.complemento import Complemento

class Malteada(IProducto):
    def __init__(self, id:int, nombre: str, precio_publico: int, ingredientes: list, volumen: float) -> None:
        self._nombre = nombre
        self._precio_publico = precio_publico
        self._ingredientes = ingredientes
        self._volumen = volumen
        self._id = id

    #Getter de id:
    @property
    def id(self) -> int:
        return self._id
    
    #Getters y setters de Malteada:
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nombre:str) -> None:
        self._nombre = nombre
    
    @property
    def precio_publico(self) -> int:
        return self._precio_publico
    
    @precio_publico.setter
    def precio_publico(self, precio_publico: int) -> None:
        self._precio_publico = precio_publico

    @property
    def ingredientes(self) -> list:
        return self._ingredientes
    
    @ingredientes.setter
    def ingredientes(self, ingredientes) -> None:
        self._ingredientes = ingredientes

    @property
    def volumen(self) -> float:
        return self._volumen
    
    @volumen.setter
    def volumen(self, volumen: float) -> None:
        self._volumen = volumen

    #Funciones impuestas por la interfaz:
    def calcular_costo(self) -> int:
        ingredientes_dicts = [{'nombre': i.nombre, 'precio': i.precio} for i in self._ingredientes]
        dict_1, dict_2, dict_3 = ingredientes_dicts[:3]
        return(costos(dict_1, dict_2, dict_3) + 500)

    def calcular_rentabilidad(self):
        ingredientes_dicts = [{'nombre': i.nombre, 'precio': i.precio} for i in self._ingredientes]
        dict_1, dict_2, dict_3 = ingredientes_dicts[:3]
        return(rentabilidad(self._precio_publico, dict_1, dict_2, dict_3) - 500)

    def calcular_calorias(self):
        lista_calorias = []
        for i in self._ingredientes:
            lista_calorias.append(i.calorias)

        temp = 200

        for i in lista_calorias:
            temp = temp + i
    
        return round(temp,2)


    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio_publico,
            'ingredientes': [
                i.to_dict() if isinstance(i, (Base, Complemento)) else str(i) 
                for i in self.ingredientes
            ],
            'volumen': self.volumen
        }