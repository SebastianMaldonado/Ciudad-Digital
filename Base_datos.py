import Modulo_Administrativo
from Empresas import *

from Principal import modulo_ad

from tokenize import String

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


    #-------------------------------- |Leer Productos| --------------------------------#
    # Función que permite cargar productos de la base de datos
    # almacenarlos en objetos de la clase Producto
    # y retornar un vector con todos los productos que coincidieran con la búsqueda
    def leer_productos (self, criterio, ind) -> Producto:
        if (ind == 0):  # Si no se recibe ningún criterio de carga
            lista = self.leer_archivo(self.text_prd, None, 0)
        else:           # Si se recibe un criterio
            if (ind == 1):         # Discriminar por nombre
                lista = self.leer_archivo(self.text_prd, criterio, 2, 1)
            elif (ind == 2):       # Discriminar por categoría
                lista = self.leer_archivo(self.text_prd, criterio, 3, 1)
            elif (ind == 3):       # Discriminar por precio  ---------------------------- |Para hacer|
                pass
            elif (ind == 4):       # Discriminar por fabricante
                lista = self.leer_archivo(self.text_prd, criterio, 1, 1)
        
        return lista

    
    
    #-------------------------------- |Leer Servicios| --------------------------------#
    # Función que permite cargar servicios de la base de datos
    # almacenarlos en objetos de la clase Servicio
    # y retornar un vector con todos los servicios que coincidieran con la búsqueda
    def leer_servicios (self, criterio) -> Servicio:
        pass
    

    #-------------------------------- |Leer Ofertas Laborales| --------------------------------#
    # Función que permite cargar las ofertas laborales de la base de datos
    # almacenarlos en objetos de la clase Oferta_laboral
    # y retornar un vector con todos las ofertas laborales que coincidieran con la búsqueda
    def leer_ofertas (self, criterio) -> int:
        pass


    #-------------------------------- |Leer Archivo| --------------------------------#
    # Extraer los objetos solicitados de una base de datos
    # Retorna un vector con los objetos
    # valores de pos [0] para cantidad | [1] empresas | [2] nombre | [3] categoría | [4] precio
    def leer_archivo (archivo, criterio, pos, tipo):
        if (tipo == 1):     # Si se desea leer productos
            lista = Producto.array()

            base_datos = open(archivo, "r")
            for linea in base_datos: 
                datos = linea.split("|")

                # Cargar empresa asociada
                empresa = Modulo_Administrativo.cargar_empresa(modulo_ad, datos[1])

                if (criterio == None):          # Cargar todos los archivos
                    producto = Producto(datos[0], empresa, datos[2], datos[3], datos[4])
                    lista.append(producto)

                elif (datos[pos] == criterio):  # Cargar según criterio de Búsqueda
                    producto = Producto(datos[0], empresa, datos[2], datos[3], datos[4])
                    lista.append(producto)
        elif (tipo == 2):   # Si se desea leer servicios
            lista = Servicio.array()

            base_datos = open(archivo, "r")
            for linea in base_datos: 
                datos = linea.split("|")

                # Cargar empresa asociada
                empresa = Modulo_Administrativo.cargar_empresa(modulo_ad, datos[1])

                if (criterio == None):          # Cargar todos los archivos
                    servicio = Servicio(datos[0], empresa, datos[2], datos[3], datos[4])
                    lista.append(servicio)

                elif (datos[pos] == criterio):  # Cargar según criterio de Búsqueda
                    servicio = Servicio(datos[0], empresa, datos[2], datos[3], datos[4])
                    lista.append(servicio)
        elif (tipo == 3):   # Si se desea leer ofertas laborales ---------------------------------- |Para hacer|
            #lista = Oferta_laboral.array()
            pass
        else:               # Si no se reconoce el tipo de información
            return

        return lista
  
