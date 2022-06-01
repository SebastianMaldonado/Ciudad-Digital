# %%
from Productos import *

# %%
'''
|====================================================================|
*                            |Empresa|
* Descripcion:                                                        
*   
|====================================================================|
'''


class Empresa:

    def __init__(self, codigo, nombre, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo

        self.productos = self.cargar_productos(3, codigo)
        self.servicios = self.cargar_servicios(3, codigo)

    def __repr__(self) -> str:
        return self.nombre

    #-------------------------------- |Cargar Productos| --------------------------------#
    # criterio: Ingresar criterio de búsqueda
    # ind: (0) sin criterio | (1) cantidad | (2) nombre | (3) cod. empresa | (4) categoría | (5) precio

    def cargar_productos(self, ind, criterio) -> Producto:
        lista = []

        archivo = open("Archivos/Productos.txt", "r")
        for linea in archivo:
            datos = linea.split("|")

            if (ind == 0):
                lista.append(
                    Producto(int(datos[0]), datos[1], self, datos[3], int(datos[4])))
            elif (datos[ind - 1] == str(criterio)):
                lista.append(
                    Producto(int(datos[0]), datos[1], self, datos[3], int(datos[4])))
        archivo.close()
        return lista

    #-------------------------------- |Cargar Servicios| --------------------------------#
    # criterio: Ingresar criterio de búsqueda
    # ind: (0) sin criterio | (1) cantidad | (2) nombre | (3) cod. empresa | (4) categoría | (5) precio

    def cargar_servicios(self, ind, criterio) -> Servicio:
        lista = []

        archivo = open("Archivos/Servicios.txt", "r")
        for linea in archivo:
            datos = linea.split("|")

            if (ind == 0):
                lista.append(
                    Servicio(int(datos[0]), datos[1], self, datos[3], int(datos[4])))
            elif (datos[ind - 1] == str(criterio)):
                lista.append(
                    Servicio(int(datos[0]), datos[1], self, datos[3], int(datos[4])))
        archivo.close()
        return lista


# %%
