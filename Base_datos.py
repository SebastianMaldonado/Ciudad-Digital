#%%
from xmlrpc.client import boolean
from Empresas import Empresa
from Productos import *
from tokenize import String

#%%
'''
|====================================================================|
*                          |Base de Datos|
* Descripcion:                                                        
*   
|====================================================================|
'''
class Base_datos:
    def __init__ (self):
        self.txt_prd = "Archivos/productos.txt"
        self.txt_srv = "Archivos/servicios.txt"
        self.txt_ofr = "Archivos/ofertaslaborales.txt"


    #-------------------------------- |Cargar Empresas| --------------------------------#
    # criterio: Ingresar criterio de búsqueda
    # ind: (0) sin criterio | (1) por código | (2) por nombre | (3) por categoría
    def cargar_empresa (self, ind, criterio) -> Empresa:
        lista = []

        archivo = open("Archivos/Empresas.txt", "r")
        for linea in archivo:
            datos = linea.split("|")

            if (ind == 0):
                lista.append(Empresa(datos[0], datos[1], datos[2]))
            elif (datos[ind - 1] == criterio):
                lista.append(Empresa(datos[0], datos[1], datos[2]))
        archivo.close()
        return lista


    #-------------------------------- |Cargar Servicios| --------------------------------#
    # Devuelve una lista con los servicios buscados
    # ind : (0) sin criterio | (1) cupos mínimos | (2) nombre | (3) cod. proveedor | (4) categoría | (5) precio máximo
    def buscar_servicios (self, ind, criterio) -> Servicio:
        lista = []
        empresas = self.cargar_empresa(3, "")

        for emp in empresas:
            for serv in emp.productos:
                if (ind == 0):      #Sin criterio de búsqueda
                    lista.append(serv)
                elif (ind == 1):    #Por cantidad mínima
                    if (serv.cupo >= criterio):
                        lista.append(serv)
                elif (ind == 2):    #Por nombre
                    if (serv.nombre == criterio):
                        lista.append(serv)
                elif (ind == 3):    #Por empresa
                    if (serv.proveedor.codigo == criterio):
                        lista.append(serv)
                elif (ind == 4):    #Por precio máximo
                    if (serv.precio <= criterio):
                        lista.append(serv)
        
        return lista
    

    #-------------------------------- |Cargar Productos| --------------------------------#
    # Devuelve una lista con los productos buscados
    # ind : (0) sin criterio | (1) cantidad mínima | (2) nombre | (3) cod. fabricante | (4) categoría | (5) precio máximo
    def buscar_productos (self, ind, criterio) -> Producto:
        lista = []
        empresas = self.cargar_empresa(0, "")

        for emp in empresas:
            for prod in emp.productos:
                if (ind == 0):      #Sin criterio de búsqueda
                    lista.append(prod)
                elif (ind == 1):    #Por cantidad mínima
                    if (prod.cupo >= criterio):
                        lista.append(prod)
                elif (ind == 2):    #Por nombre
                    if (prod.nombre == criterio):
                        lista.append(prod)
                elif (ind == 3):    #Por empresa
                    if (prod.proveedor.codigo == criterio):
                        lista.append(prod)
                elif (ind == 4):    #Por categoría
                    if (prod.categoria == criterio):
                        lista.append(prod)
                elif (ind == 5):    #Por precio máximo
                    if (prod.precio <= criterio):
                        lista.append(prod)
        
        return lista


    #-------------------------------- |Añadir a la Base de Datos| --------------------------------#
    def añadir_bd (self, ind, obj):
        if (ind == 1):      # Añadir nueva Empresa
            archivo = open ("Archivos/Empresas.txt", "a")
            archivo.write(str(obj.codigo) + "|" + obj.nombre + "|" + obj.tipo + "|\n")
            archivo.close()
        elif (ind == 2):    # Añadir nuevo Producto
            archivo = open ("Archivos/Productos.txt", "a")
            archivo.write(str(obj.cantidad) + "|" + obj.nombre + "|" + str(obj.fabricante.codigo) + "|" + obj.categoria + "|" + str(obj.precio) + "|\n")
            archivo.close()
        elif (ind == 3):    # Añadir nuevo Servicio
            archivo = open ("Archivos/Servicios.txt", "a")
            archivo.write(str(obj.cupo) + "|" + obj.nombre + "|" + str(obj.proveedor.codigo) + "|" + obj.categoria + "|" + str(obj.precio) + "|\n")
            archivo.close()


    #-------------------------------- |Eliminar de la Base de Datos| --------------------------------#
    def eliminar_db (self, ind, obj):
        if (ind == 1):      #Eliminar Empresa
            base_datos = "Archivos/Empresas.txt"
        elif (ind == 2):    #Eliminar Producto
            base_datos = "Archivos/Productos.txt"
        elif (ind == 3):    #Eliminar Servicio
            base_datos = "Archivos/Servicios.txt"
        
        temp = open ("Archivos/temp_administrativo.txt", "w")  #Archivo temporal
        archivo = open (base_datos, "r")

        # Eliminación de la Empresa de a base de datos del módulo administrativo
        for linea in archivo:
            datos = linea.split("|")
            if (datos[1] != obj.nombre):
                temp.write(linea)
        archivo.close ()
        temp.close()

        temp = open ("Archivos/temp_administrativo.txt", "r")  
        archivo = open (base_datos, "w")

        for linea in temp:
            archivo.write(linea)
        temp.close()
        archivo.close()


    #-------------------------------- |Modificar la Base de Datos| --------------------------------#
    def modificar_db (self, ind, obj):
        if (ind == 1):      #Modificar Empresa
            base_datos = "Archivos/Empresas.txt"
        if (ind == 2):      #Modificar Producto
            base_datos = "Archivos/Productos.txt"
        elif (ind == 2):    #Modificar Servicio
            base_datos = "Archivos/Servicios.txt"
        
        temp = open ("Archivos/temp_administrativo.txt", "w")  #Archivo temporal
        archivo = open (base_datos, "r")

        # Eliminación de la Empresa de a base de datos del módulo administrativo
        for linea in archivo:
            datos = linea.split("|")
            if (datos[1] != obj.nombre):
                temp.write(linea)
            else:
                if (ind == 1):
                    temp.write (str(obj.codigo) + "|" + obj.nombre + "|" + obj.tipo + "|\n")
                elif (ind == 2):
                    temp.write (str(obj.cantidad) + "|" + obj.nombre + "|" + str(obj.fabricante.codigo) + "|" + obj.categoria + "|" + str(obj.precio) + "|\n")
                elif (ind == 3):
                    temp.write (str(obj.cupo) + "|" + obj.nombre + "|" + str(obj.proveedor.codigo) + "|" + obj.categoria + "|" + str(obj.precio) + "|\n")
        archivo.close ()
        temp.close()

        temp = open ("Archivos/temp_administrativo.txt", "r")  
        archivo = open (base_datos, "w")

        for linea in temp:
            archivo.write(linea)
        temp.close()
        archivo.close()


#%%
base = Base_datos()
lista = base.buscar_productos(4, "Telefonia")
  
for prod in lista:
    print(prod.nombre)
    print("   "+prod.fabricante.nombre)

empresa = Empresa (1242, "Olimpica", "Tienda")
prod = Producto (100, "Ron Medellin", empresa, "Licores", 20000)
serv = Servicio (1, "Farmacia", empresa, "Salud", 100000)
base.añadir_bd (1, empresa)
base.añadir_bd (2, prod)
base.añadir_bd (3, serv)
base.eliminar_db (3, serv)
prod.cantidad = 1
base.modificar_db (2, prod)
# %%

