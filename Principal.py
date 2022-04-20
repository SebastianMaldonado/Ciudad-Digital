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
  def busqueda(self):
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
    
 
