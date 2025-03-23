from models.funciones import mejor_producto
from models.base import Base
from models.complemento import Complemento


class Heladeria():
    def __init__(self, nombre: str, menu_diario: dict) -> None:
      self.__nombre = nombre
      self.__menu_diario = menu_diario  

    #Getters y setters de Heladeria:
    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre:str) -> None:
        self.__nombre = nombre
    
    @property
    def menu_diario(self) -> dict:
        return self.__menu_diario

    @menu_diario.setter
    def menu_diario(self, menu_diario:dict) -> None:
        self.__menu_diario = menu_diario

    def mejor_producto(self, menu_dia) -> str:
        productos_dicts = [{'nombre': i.nombre, 'rentabilidad': i.calcular_rentabilidad()} for i in menu_dia]
        dict_1, dict_2, dict_3, dict_4 = productos_dicts[:4]
        return(mejor_producto(dict_1, dict_2, dict_3, dict_4))

    def buscar_producto_por_id(self, producto_id):
        for productos in self.menu_diario.values():
            for producto in productos:
                if producto.id == producto_id:
                    return producto
        return None  
    

    def buscar_producto_por_nombre(self, nombre):
        for productos in self.menu_diario.values():
            for producto in productos:
                if producto.nombre.lower() == nombre.lower():
                    return producto
        return None

    def buscar_calorias_por_id(self, producto_id):
        producto = self.buscar_producto_por_id(producto_id)
        return producto.calcular_calorias() if producto else None

    def consultar_rentabilidad_por_id(self, producto_id):
        producto = self.buscar_producto_por_id(producto_id)
        return producto.calcular_rentabilidad() if producto else None
    
    def consultar_costo_produccion_por_id(self, producto_id):
        producto = self.buscar_producto_por_id(producto_id)
        return producto.calcular_costo() if producto else None
    
    def vender_producto(self, producto_id):
        producto = self.buscar_producto_por_id(producto_id)
        if producto:
            for ingrediente in producto.ingredientes:
                if isinstance(ingrediente, Base):
                    if ingrediente.inventario >= 0.2:
                        ingrediente.inventario -= 0.2
                    else:
                        return f"No hay suficiente inventario para la base del producto {producto.nombre}"
                elif isinstance(ingrediente, Complemento):
                    if ingrediente.inventario >= 1:
                        ingrediente.inventario -= 1
                    else:
                        return f"No hay suficiente inventario para el complemento del producto {producto.nombre}"
            return f"Venta exitosa de {producto.nombre}"
        return "Producto no encontrado"

    def consultar_todos_los_ingredientes(self):
        ingredientes_unicos = set()
        for productos in self.menu_diario.values():
            for producto in productos:
                ingredientes_unicos.update(producto.ingredientes)
        return list(ingredientes_unicos)
    
    def buscar_ingrediente_por_id(self, ingrediente_id):
        for ingrediente in self.consultar_todos_los_ingredientes():
            if ingrediente.id == ingrediente_id:
                return ingrediente
        return None
    
    def buscar_ingrediente_por_nombre(self, nombre):
        for ingrediente in self.consultar_todos_los_ingredientes():
            if ingrediente.nombre.lower() == nombre.lower():
                return ingrediente
        return None
    
    def verificar_si_ingrediente_es_sano(self, ingrediente_id):
        ingrediente = self.buscar_ingrediente_por_id(ingrediente_id)
        return ingrediente.es_sano() if ingrediente else None
    
    def reabastecer_producto(self, producto_id):
        producto = self.buscar_producto_por_id(producto_id)
        if producto:
            for ingrediente in producto.ingredientes:
                ingrediente.abastecer()
            return f"Inventario de {producto.nombre} reabastecido"
        return "Producto no encontrado"
    
    def renovar_inventario_producto(self, producto_id, cantidad):
        producto = self.buscar_producto_por_id(producto_id)
        if producto:
            for ingrediente in producto.ingredientes:
                ingrediente.inventario += cantidad
            return f"Inventario de {producto.nombre} renovado en {cantidad} unidades"
        return "Producto no encontrado"
