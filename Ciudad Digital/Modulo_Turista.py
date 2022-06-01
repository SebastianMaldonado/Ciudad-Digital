from Modulo import *

'''
|====================================================================|
*                      |Módulo Comercial|
* Descripcion:                                                        
*   Módulo encargado de la administración y búsqueda de productos
*   Por medio de él es comprar productos comerciales y servicios
|====================================================================|
'''


class Turista (Modulo):
    lista = []
    carrito = []

    #-------------------------------- |Buscar Producto| --------------------------------#
    # Una vez seleccionada una empresa se podrán añadir productos a su catálogo
    # Estos quedarán registrados en el objeto de la empresa
    #   y serán añadidos al archivo
    # ind : (0) sin criterio | (1) cantidad mínima | (2) nombre | (3) Fabricante | (4) precio máximo
    def buscar_prod(self, ind, criterio):
        base = Base_datos()
        temp = base.buscar_productos(4, "Turista")
        self.lista = self.discriminar(temp, ind, criterio)

    #-------------------------------- |Buscar Producto| --------------------------------#
    # Agregar a la lista de objetos a comprar
    # cada que se agrege un objeto se añadirá como lista,
    # posición [1] si es producto o servicio y posición [2] el objeto a comprar

    def añadir_carro(self, ind, obj):
        self.carrito.append([ind, obj])
