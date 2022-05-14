from Productos import *


'''
|====================================================================|
*                            |Empresa|
* Descripcion:                                                        
*   
|====================================================================|
'''
class Empresa:

  def __init__ (self, nombre, tipo, nr_empleados, list_empleados, list_servicios, ofertas_laborales, codigo):
    self.nombre = nombre                          
    self.tipo = tipo                              
    self.nr_empleados = nr_empleados              
    self.list_empleados = list_empleados
    self.list_servicios = list_servicios
    self.ofertas_laborales = ofertas_laborales
    self.codigo = codigo

    self.productos = []
    self.servicios = []
    self.ofertas = []


    #-------------------------------- |Cargar datos| --------------------------------#
    # Método por medio del cual la empresa carga y almacena todos los objetos
    # de las bases de datos relacionados con ella
    def cargar_empresa (self):
        # Cargar Productos
        base_datos = open("Archivos/productos.txt", "r")
        for linea in base_datos:
            datos = linea.split("|")
            if (datos[0] == self.codigo):
                producto = Producto()
                self.productos.append(producto)

        # Cargar Servicios
        base_datos = open("Archivos/servicios.txt", "r")
        for linea in base_datos:
            datos = linea.split("|")
            if (datos[0] == self.codigo):
                servicio = Servicio()
                self.servicios.append(servicio)
        
        # Cargar Ofertas Laborales
        base_datos = open("Archivos/ofertas.txt", "r")
        for linea in base_datos:
            datos = linea.split("|")
            if (datos[0] == self.codigo):
                oferta = ofertas_lab()
                self.ofertas.append(oferta)


    #-------------------------------- |Vender Producto| --------------------------------#
    # 
    def vender_prod ():
        producto = Producto()
        self.productos.append(producto)

        base_datos = open("Archivos/productos.txt", "a")
        base_datos.write(self.codigo)
        base_datos.close()


    #-------------------------------- |Vender Servicio| --------------------------------#
    # 
        servicio = Producto()
        self.servicios.append(servicio)

        base_datos = open("Archivos/servicios.txt", "a")
        base_datos.write(self.codigo)
        base_datos.close()


    #-------------------------------- |Mostrar Ofertas laborales| --------------------------------#
    # 
    def ofertas_lab ():
        oferta = ofertas_lab()
        self.ofertas.append(oferta)

        base_datos = open("Archivos/ofertas.txt", "a")
        base_datos.write(self.codigo)
        base_datos.close()

    def aceptar_trab ():
        pass



        

    
