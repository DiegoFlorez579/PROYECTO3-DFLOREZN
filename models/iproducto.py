#Importar abc para manejo de clases abstractas:
from abc import ABC, abstractmethod

class IProducto(ABC):

    @abstractmethod
    def calcular_costo():
        pass

    @abstractmethod
    def calcular_rentabilidad():
        pass

    @abstractmethod
    def calcular_calorias():
        pass
