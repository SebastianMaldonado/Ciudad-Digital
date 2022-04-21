from abc import ABC, abstractmethod
from Empresas import *

class Cliente:
  def __init__(self, codigo, cont ):
    codigo = codigo
    cont = cont
    
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
    
class Administrativo ():

  def __init__ (self):
    self.base_datos = "Empresas.txt"


  def acceder_Empresa (self, nombre):
    archivo = open(self.base_datos, "r")
    for linea in archivo:
      datos = linea.split("|")

      if (datos[1] == nombre):
        self.empresa = Empresa ()   #Empresa con la que se va a trabajar
    archivo.close()

  def crearEmpresa (self, nombre, tipo, nr_empleados, list_empleados, list_servicios, ofertas_laborales, codigo):
    archivo = open (self.base_datos, "a")
    archivo.write(nombre + "|" + tipo + "|" + nr_empleados + "|" + list_empleados + "|" + list_servicios + "|" + ofertas_laborales + "|" + codigo)         #Registro en base de datos
    archivo.close()

    self.empresa = Empresa (nombre, tipo, nr_empleados, list_empleados, list_servicios, ofertas_laborales, codigo)                                         #Empresa con la que se va a trabajar

  def liquidar_Empresa (self, nombre):
    temp = open ("temp_administrativo.txt", "a")  #Archivo temporal
    archivo = open (self.base_datos, "r")

    #Escritura de todas las empresas menos la que se va a eliminar 
    #en el archivo temporal
    for linea in archivo:
      datos = linea.split()

      if (datos[1] != nombre):
        temp.write(linea)
        

modulo1 = Administrativo()
modulo1.crearEmpresa("nombre", "tipo", "nr_empleados", "list_empleados", "list_servicios", "ofertas_laborales", "1000")


