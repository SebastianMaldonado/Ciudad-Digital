from abc import ABC, abstractmethod

class Cliente:
  def __init__(self):
    private Codigo = input("Ingrese el Código")
    private Contraseña = input("Ingrese la contraseña")
    with open ("Empresas.txt","r") as database
    
  def aceptar(self):
    pass
  def subir_cv(self):
    pass 
    
class Modulo(ABC):
  @abstractmethod
  def busqueda(self, base_datos, nombre):
    pass
    
class Productos(ABC):
  @abstractmethod
  def __init__(self):
    pass
    
class Laboral(Modulo):
  def __init__(self):
    self.base_datos = open("Laboral.txt", "a")
    
class Turista(Modulo):
  def __init__(self):
    self.base_datos = open("Turista.txt","a")
    
class Estudiantil(Modulo):
  def __init__(self):
    self.base_datos = open("Estudiantil.txt","a")
    
class Comercio(Modulo):
  def __init__(self):
    self.base_datos = open("Comercio.txt","a")
    
class Administrativo (Modulo):

  def __init__ (self):
    self.base_datos = open("Empresas.txt", "b")


  def acceder_Empresa (self, nombre):
    for linea in self.base_datos:
      datos = linea.split("|")

      if (datos[1] == nombre):
        self.empresa = Empresa ()   #Empresa con la que se va a trabajar


  def crearEmpresa (self, nombre, tipo, nr_empleados, list_empleados, list_servicios, ofertas_laborales, codigo):
    self.empresa = Empresa (nombre, tipo, nr_empleados, list_empleados, list_servicios, ofertas_laborales, codigo)                                                 #Empresa con la que se va a trabajar
    self.base_datos.write(nombre + "|" + tipo + "|" + nr_empleados + "|" + list_empleados + "|" + list_servicios + "|" + ofertas_laborales + "|" + codigo)         #Registro en base de datos


  def liquidar_Empresa (self, nombre):
    temp = open ("temp_administrativo.txt", "w")  #Archivo temporal

    #Escritura de todas las empresas menos la que se va a eliminar 
    #en el archivo temporal
    for linea in self.base_datos:
      datos = linea.split()

      if (datos[1] != nombre):
        temp.write(linea)
        
        
class Empresa:

  def __init__ (self, nombre, tipo, nr_empleados, list_empleados, list_servicios, ofertas_laborales, codigo):
    self.nombre = nombre                          
    self.tipo = tipo                              
    self.nr_empleados = nr_empleados              
    self.list_empleados = list_empleados
    self.list_servicios = list_servicios
    self.ofertas_laborales = ofertas_laborales
    self.codigo = codigo

  def vender_prod ():
    pass

  def vender_serv ():
    pass

  def ofertas_lab ():
    pass

  def aceptar_trab ():
    pass

