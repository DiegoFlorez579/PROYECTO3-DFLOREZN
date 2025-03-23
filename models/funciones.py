
#Función "¿Esto es Sano?", que comprueba si el ingrediente tiene menos de 100 calorias o es vegetariano:
def es_sano(numero_calorias: float, vegetariano: bool) -> bool:
    if (numero_calorias < 100) or (vegetariano == True):
        return True
    else:
        return False

#Función "Las Calorías" que retorna el número de calorias de un producto:
def calorias(numero_calorias: list) -> float:
    temp = 0

    for i in numero_calorias:
        temp = temp + i
    
    temp = temp * 0.95

    return round(temp,2)

#Función "Costos" que retorna el costo total de un producto:
def costos(dict_1: dict, dict_2: dict, dict_3: dict) -> int:
    return(dict_1['precio'] + dict_2['precio'] + dict_3['precio'])

#Función "Rentabilidad" que retorna la rentabilidad de un producto dado:
def rentabilidad(precio_venta: int, dict_1: dict, dict_2: dict, dict_3: dict) -> int:
    return(precio_venta - costos(dict_1, dict_2, dict_3))

#Función "El mejor producto" que retorna que producto tiene una mayor rentabilidad:
def mejor_producto(dict_1: dict, dict_2: dict, dict_3: dict, dict_4: dict):
    rentabilidad = [] 
    temp_list = [dict_1, dict_2, dict_3, dict_4]
    for i in temp_list:
        rentabilidad.append(i['rentabilidad'])
    
    rentabilidad.sort(reverse = True)
    for i in temp_list:
        if i['rentabilidad'] == rentabilidad[0]:
            return i['nombre']

