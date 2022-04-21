from abc import ABC, abstractmethod

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
    cargar_empresa(self)


    def cargar_empresa (self):
        base_datos = open("Archivos/productos.txt", "r")
        for linea in base_datos:
            datos = linea.split("|")
            if (datos[0] == self.codigo):
                producto = Producto()
                self.productos.append(producto)

        base_datos = open("Archivos/servicios.txt", "r")
        for linea in base_datos:
            datos = linea.split("|")
            if (datos[0] == self.codigo):
                servicio = Servicio()
                self.servicios.append(servicio)

        base_datos = open("Archivos/ofertas.txt", "r")
        for linea in base_datos:
            datos = linea.split("|")
            if (datos[0] == self.codigo):
                oferta = ofertas_lab()
                self.ofertas.append(oferta)

    def vender_prod ():
        producto = Producto()
        self.productos.append(producto)

        base_datos = open("Archivos/productos.txt", "a")
        base_datos.write(self.codigo)
        base_datos.close()

    def vender_serv ():
        servicio = Producto()
        self.servicios.append(servicio)

        base_datos = open("Archivos/servicios.txt", "a")
        base_datos.write(self.codigo)
        base_datos.close()

    def ofertas_lab ():
        oferta = ofertas_lab()
        self.ofertas.append(oferta)

        base_datos = open("Archivos/ofertas.txt", "a")
        base_datos.write(self.codigo)
        base_datos.close()

    def aceptar_trab ():
        pass

class Productos (ABC):
    
    @abstractmethod
    def __init__(self, Nombre, Categoria, Precio):
        self.Nombre = Nombre
        self.Categoria = Categoria
        self.Precio = Precio
        
class Producto (Productos):
    def __init__ (self, Cantidad,Empresa,Nombre,Categoria,Precio):
        self.Fabricante = Empresa
        self.Cantidad = Cantidad
        super().__init__(Nombre,Categoria,Precio)

class Servicio (Productos):
    def __init__ (self, Cupo, Empresa,Nombre,Categoria,Precio):
        self.Cupo = Cupo
        self.Provedor = Empresa 
        super().__init__(Nombre,Categoria,Precio)
        

    
