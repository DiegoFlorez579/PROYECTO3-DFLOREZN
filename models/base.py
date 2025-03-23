#Importar la clase abstracta ingrediente
from models.ingrediente import Ingredientes

#Crear la clase Base:
class Base(Ingredientes):
    def __init__(self, id: int, precio: int, calorias: float, nombre: str, inventario: int, es_vegetariano: bool, sabor: str) -> None:
        super().__init__(precio, calorias, nombre, inventario, es_vegetariano)
        self._sabor = sabor
        self._id = id

    def abastecer(self) -> None:
        self._inventario += 5

    #Getter de id:
    @property
    def id(self) -> int:
        return self._id

    #Getter y setter de sabor:
    @property
    def sabor(self) -> str:
        return self._sabor

    @sabor.setter
    def sabor(self, sabor:str) -> None:
        self._sabor = sabor
    
    def to_dict(self):
        return {
            'id': self.id,
            'precio': self.precio,
            'calorias': self.calorias,
            'nombre': self.nombre,
            'inventario': self.inventario,
            'es_vegetariano': self.es_vegetariano,
            'sabor': self.sabor
        }