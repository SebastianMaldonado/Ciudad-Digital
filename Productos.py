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
    def __init__ (self, Cantidad,Empresa,Nombre,Categoria,Precio):
        self.Fabricante = Empresa
        self.Cantidad = Cantidad
        super().__init__(Nombre,Categoria,Precio)


'''
|====================================================================|
*                            |Servicio|
*                    [Clase Hija de Productos]
* Descripcion:                                                        
*   
|====================================================================|
'''
class Servicio (Productos):
    def __init__ (self, Cupo, Empresa,Nombre,Categoria,Precio):
        self.Cupo = Cupo
        self.Provedor = Empresa 
        super().__init__(Nombre,Categoria,Precio)