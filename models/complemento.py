#Importar la clase abstracta ingrediente
from models.ingrediente import Ingredientes

#Crear la clase Complemento:
class Complemento(Ingredientes):
    def __init__(self, id: int, precio: int, calorias: float, nombre: str, inventario: int, es_vegetariano: bool) -> None:
        super().__init__(precio, calorias, nombre, inventario, es_vegetariano)
        self._id = id

    #Getter de id:
    @property
    def id(self) -> int:
        return self._id
    
    def abastecer(self) -> None:
        self._inventario += 10

    def renovar_inventario(self) -> None:
        self._inventario = 0

    def to_dict(self):
        return {
            'id': self.id,
            'precio': self.precio,
            'calorias': self.calorias,
            'nombre': self.nombre,
            'inventario': self.inventario,
            'es_vegetariano': self.es_vegetariano
        }