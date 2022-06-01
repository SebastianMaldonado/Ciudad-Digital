# %%
from Modulo import *

# %%
'''
|====================================================================|
*                      |Módulo Administrativo|
* Descripcion:                                                        
*   Módulo encargado de la administración de las empresas
*   Por medio de él es posible crear, cargar, eliminar y acceder a ellas
|====================================================================|
'''


class Administrativo (Modulo):

    def __init__(self):
        self.empresa = None

    #-------------------------------- |Acceder a una Empresa| --------------------------------#
    # Función que permite acceder a una empresa guardada en la base de datos
    # La dejará almacenada en los atributos del módulo administrativo para poder acceder a su información

    def acceder_Empresa(self, codigo):
        lista = Base_datos.cargar_empresa(1, 1, codigo)
        if (lista == None):
            self.empresa = None
        else:
            self.empresa = lista[0]

    #-------------------------------- |Crear una Empresa| --------------------------------#
    # Carga los datos ingresados y crea un nuevo objeto de la clase Empresa
    # De igual manera actualiza la base de datos para poder acceder a dicha empresa en cualquier momento

    def crearEmpresa(self, codigo, nombre, tipo):
        empresa = Empresa(codigo, nombre, tipo)
        Base_datos.añadir_bd(1, empresa)

    #-------------------------------- |Liquidar una Empresa| --------------------------------#
    # Liquida o elimina una empresa de la base de datos
    # También eliminará todos los objetos y asociaciones relacionadas con esta empresa:
    #   Productos, servicios, ofertas laborales y contratos con empleados

    def liquidar_Empresa(self, codigo):
        empresa = Base_datos.cargar_empresa(1, codigo)
        for prod in empresa.productos:  # Eliminar Productos de la Empresa
            Base_datos.eliminar_db(2, prod)

        for serv in empresa.servicios:  # Eliminar Servicios de la Empresa
            Base_datos.eliminar_db(3, serv)

        Base_datos.eliminar_db(1, empresa)

    #-------------------------------- |Añadir Producto| --------------------------------#
    # Una vez seleccionada una empresa se podrán añadir productos a su catálogo
    # Estos quedarán registrados en la lista productos del objeto de la empresa
    #   y serán añadidos al archivo

    def añadir_prod(self, ind, cantidad, nombre, categoria, precio):
        if (ind == 1):
            nuevo = Producto(cantidad, nombre, self.empresa, categoria, precio)
            self.empresa.productos.append(nuevo)
        else:
            nuevo = Servicio(cantidad, nombre, self.empresa, categoria, precio)
            self.empresa.servicios.append(nuevo)

        Base_datos.añadir_bd(ind + 1, nuevo)

    #-------------------------------- |Eliminar Producto| --------------------------------#
    # Una vez seleccionada una empresa se podrán eliminar productos de su catálogo
    # Estos serán eliminados de la lista de productos del objeto de la empresa
    #   y serán eliminados del archivo

    def eliminar_prod(self, ind, nombre):
        eliminado = None

        if (ind == 1):  # Si es un producto
            for prod in self.empresa.productos:
                if (prod.nombre == nombre):
                    eliminado = prod
        else:  # Si es un servicio
            for prod in self.empresa.servicios:
                if (prod.nombre == nombre):
                    eliminado = prod

        if (eliminado == None):
            return

        if (ind == 1):
            try:
                self.empresa.productos.remove(eliminado)
            except:
                print("No se encontró " + eliminado.nombre)
        else:
            try:
                self.empresa.servicios.remove(eliminado)
            except:
                print("No se encontró " + eliminado.nombre)

        Base_datos.eliminar_db(ind + 1, eliminado)


# %%
