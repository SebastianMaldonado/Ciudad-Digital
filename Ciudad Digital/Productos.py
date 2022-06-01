from abc import ABC, abstractmethod

'''
|====================================================================|
*                            |Productos|
*                         [Clase Abstracta]
* Descripcion:                                                        
*   
|====================================================================|
'''


class Productos (ABC):

    @abstractmethod
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio


'''
|====================================================================|
*                            |Producto|
*                     [Clase Hija de Productos]
* Descripcion:                                                        
*   
|====================================================================|
'''


class Producto (Productos):
    def __init__(self, Cantidad, Nombre, Empresa, Categoria, Precio):
        self.fabricante = Empresa
        self.cantidad = Cantidad
        super().__init__(Nombre, Categoria, Precio)


'''
|====================================================================|
*                            |Servicio|
*                    [Clase Hija de Productos]
* Descripcion:                                                        
*   
|====================================================================|
'''


class Servicio (Productos):
    def __init__(self, Cupo, Nombre, Empresa, Categoria, Precio):
        self.cupo = Cupo
        self.proveedor = Empresa
        super().__init__(Nombre, Categoria, Precio)
