from models.base import Base
from models.complemento import Complemento
from models.copa import Copa
from models.malteada import Malteada
from models.heladeria import Heladeria


#Creacion de ingredientes

#Bases:
base_1 = Base(1, 3000, 150, "Helado de Vainilla", 20, True, "Vainilla")
base_2 = Base(2, 3200, 180, "Helado de Cafe", 15, True, "Cafe")
base_3 = Base(3, 2800, 140, "Leche chocolatada", 25, True, "Chocolate")
base_4 = Base(4, 2900, 130, "Jugo de maracuya con leche", 18, True, "Maracuya")
base_5 = Base(5, 3100, 160, "Helado de Fresa", 22, True, "Fresa")
base_6 = Base(6, 3300, 190, "Helado de Arequipe", 20, False, "Arequipe")
base_7 = Base(7, 3000, 170, "Helado de Chocolate", 24, False, "Chocolate")
base_8 = Base(8, 2800, 140, "Batido de Mango", 19, True, "Mango")

#Complementos:
complemento_1 = Complemento(9, 1500, 100, "Bocadillo", 10, True)
complemento_2 = Complemento(10, 1200, 80, "Queso rallado", 12, False)
complemento_3 = Complemento(11, 1000, 90, "Galleta de mantequilla", 20, True)
complemento_4 = Complemento(12, 1300, 110, "Crema chantilly", 15, False)
complemento_5 = Complemento(13, 2000, 120, "Arequipe", 8, False)
complemento_6 = Complemento(14, 1100, 70, "Chispas de chocolate", 14, True)
complemento_7 = Complemento(15, 1400, 95, "Leche condensada", 10, False)
complemento_8 = Complemento(16, 1250, 85, "Coco rallado", 12, True)
complemento_9 = Complemento(17, 1350, 105, "Mani triturado", 14, True)
complemento_10 = Complemento(18, 1150, 75, "Sirope de Fresa", 16, True)
complemento_11 = Complemento(19, 1400, 110, "Caramelo liquido", 10, False)
complemento_12 = Complemento(20, 1300, 120, "Nueces picadas", 11, True)

#Creacion de copas y malteadas para cada dia:
menu_semanal = {
    "Lunes": [
        Copa(1, "Sabana Tropical", 9500, [base_1, complemento_1, complemento_2], "Copa mediana"),
        Copa(2, "Aroma de Cafe", 9900, [base_2, complemento_3, complemento_4], "Copa grande"),
        Malteada(3, "Chocolate Santafereño", 10500, [base_3, complemento_5, complemento_6], 16),
        Malteada(4, "Maracuya Cremoso", 10200, [base_4, complemento_7, complemento_8], 12)
    ],
    "Martes": [
        Copa(5, "Fresa Delicia", 9700, [base_5, complemento_9, complemento_10], "Copa mediana"),
        Copa(6, "Dulce Tentacion", 10100, [base_6, complemento_11, complemento_12], "Copa grande"),
        Malteada(7, "Mango Extremo", 10700, [base_8, complemento_5, complemento_7], 14),
        Malteada(8, "Chocolate y Nuez", 10300, [base_7, complemento_3, complemento_12], 16)
    ],
    "Miercoles": [
        Copa(9, "Coco Caramelo", 9800, [base_1, complemento_2, complemento_11], "Copa grande"),
        Copa(10, "Arequipe Sensacion", 10200, [base_6, complemento_6, complemento_9], "Copa mediana"),
        Malteada(11, "Maracuya Exotico", 10500, [base_4, complemento_1, complemento_12], 14),
        Malteada(12, "Cafe Cremoso", 10800, [base_2, complemento_5, complemento_10], 16)
    ],
    "Jueves": [
        Copa(13, "Choco Tentacion", 10300, [base_7, complemento_8, complemento_10], "Copa grande"),
        Copa(14, "Dulce Mango", 10000, [base_8, complemento_3, complemento_7], "Copa mediana"),
        Malteada(15, "Leche y Coco", 10700, [base_3, complemento_1, complemento_12], 14),
        Malteada(16, "Fresa Cremosa", 10400, [base_5, complemento_6, complemento_11], 12)
    ],
    "Viernes": [
        Copa(17, "Arequipe Caramelo", 10600, [base_6, complemento_9, complemento_11], "Copa grande"),
        Copa(18, "Mango Tentacion", 10250, [base_8, complemento_5, complemento_10], "Copa mediana"),
        Malteada(19, "Cafe Intenso", 10900, [base_2, complemento_3, complemento_6], 16),
        Malteada(20, "Fresa Dulce", 10550, [base_5, complemento_4, complemento_12], 14)
    ],
    "Sabado": [
        Copa(21, "Vainilla Exquisita", 10800, [base_1, complemento_6, complemento_10], "Copa grande"),
        Copa(22, "Doble Chocolate", 11000, [base_7, complemento_3, complemento_5], "Copa mediana"),
        Malteada(23, "Frutos Secos", 11200, [base_6, complemento_9, complemento_11], 14),
        Malteada(24, "Cafe Arequipe", 11400, [base_2, complemento_5, complemento_12], 16)
    ],
    "Domingo": [
        Copa(25, "Frutos Rojos", 10700, [base_5, complemento_8, complemento_12], "Copa mediana"),
        Copa(26, "Dulce Maracuya", 10900, [base_4, complemento_1, complemento_9], "Copa grande"),
        Malteada(27, "Tropical Mix", 11500, [base_8, complemento_3, complemento_6], 14),
        Malteada(28, "Arequipe Fest", 11800, [base_6, complemento_7, complemento_10], 16)
    ]
}

Heladeria_principal = Heladeria('Principal', menu_semanal)
