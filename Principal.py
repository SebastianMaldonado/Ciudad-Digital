# %%
from abc import ABC, abstractmethod
from Empresas import *

class Cliente:
  def __init__(self, nombre, codigo, cont):
    self.nombre = nombre
    self.codigo = codigo
    self.cont = cont
    self.cv = None
    self.modulo = None

    self.ofertas_lab = []
    self.estudiante = []
    self.institucion = []
    
    #self.cargar_info(self, self.codigo)

  def acceder_modulo (self, tipo):
    if (tipo == 1):
      self.modulo = Administrativo()
    elif (tipo == 2):
      self.modulo = Administrativo()
    elif (tipo == 3):
      self.modulo = Administrativo()
    else:
      self.modulo = Administrativo()

  def cargar_info (self, codigo):
      self.modulo = Administrativo()

      base_datos = open("Archivos/clientes.txt", "r")
      for linea in base_datos:
        datos = linea.split("\t")

        if (datos[0] == codigo):
          ofertas = datos[1].split("%")
          estudiante = datos[2]
          institucion = datos[3]
      base_datos.close()

      for dato in ofertas:   #Por cada oferta que tenga registrada el cliente
        info = dato.split("|")
        base_datos = open("Archivos/ofertas.txt", "r")
        for linea in base_datos:  #Leer código de Empresa para la oferta
          ind = linea.split("|")

          if (dato == ind[0]):
            pass
            

      self.modulo = None



  def aceptar(self):
    pass

  def subir_cv(self):
    pass 
    
class Modulo(ABC):
  @abstractmethod
  def busqueda(self, base_datos, nombre):
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
    self.base_datos = "Archivos/Empresas.txt"
    self.empresa = None
    self.lista_empresas = []

  #-------------------------------- |Acceder a una Empresa| --------------------------------#
  # Función que permite acceder a una empresa guardada en la base de datos
  # La dejará almacenada en los atributos del módulo administrativo para poder acceder a su información
  def acceder_Empresa (self, nombre):
    self.empresa = self.acceder_Empresa(nombre)

  
  #-------------------------------- |Cargar una Empresa| --------------------------------#
  # Función que permite cargar una empresa guardada en la base de datos
  # Si ya está cargada la retorna, en caso contrario la crea y después la retorna
  def cargar_Empresa (self, nombre) -> Empresa:
    archivo = open(self.base_datos, "r")
    for linea in archivo:
      datos = linea.split("|")

      if (datos[0] == nombre):
        empresa = self.empresa_cargada(datos[6])  #Buscar empresa entre los objetos ya cargados

        if (empresa == None):   	#Si NO la encuentra
          empresa = Empresa (datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6])   #Crear nuevo objeto de la clase Empresa
    archivo.close()

    return empresa


  #-------------------------------- |Buscar una Empresa| --------------------------------#
  # Función que permite conocer si una empresa ya fue cargada de la base de Datos
  # Retonará None en caso de no encontrarla
  def empresa_cargada (self, codigo) -> Empresa:
    for empresa in self.lista_empresas:
      if (empresa != None):       # Si la posición NO es vacía
        if (codigo == empresa.codigo):  # Si se encontró la empresa
          return empresa
    return None


  #-------------------------------- |Crear una Empresa| --------------------------------#
  # Carga los datos ingresados y crea un nuevo objeto de la clase Empresa
  # De igual manera actualiza la base de datos para poder acceder a dicha empresa en cualquier momento
  def crearEmpresa (self, nombre, tipo, nr_empleados, list_empleados, list_servicios, ofertas_laborales, codigo):
    # Actualizar Base de Datos
    archivo = open (self.base_datos, "a")
    archivo.write(nombre + "|" + tipo + "|" + nr_empleados + "|" + list_empleados + "|" + list_servicios + "|" + ofertas_laborales + "|" + codigo + "\n")         #Registro en base de datos
    archivo.close()

    # Crear objeto de la clase Empresa
    self.empresa = Empresa (nombre, tipo, nr_empleados, list_empleados, list_servicios, ofertas_laborales, codigo)                                         #Empresa con la que se va a trabajar
    self.lista_empresas.append(self.empresa)


  #-------------------------------- |Liquidar una Empresa| --------------------------------#
  # Liquida o elimina una empresa de la base de datos
  # También eliminará todos los objetos y asociaciones relacionadas con esta empresa:
  #   Productos, servicios, ofertas laborales y contratos con empleados
  def liquidar_Empresa (self, nombre):
    temp = open ("Archivos/temp_administrativo.txt", "w")  #Archivo temporal
    archivo = open (self.base_datos, "r")

    # Eliminación de la Empresa de a base de datos del módulo administrativo
    for linea in archivo:
      datos = linea.split("|")
      if (datos[0] != nombre):
        temp.write(linea)
    archivo.close ()
    temp.close()

    temp = open ("Archivos/temp_administrativo.txt", "r")  
    archivo = open (self.base_datos, "w")
    for linea in temp:
      archivo.write(linea)
    temp.close()
    archivo.close()

    # Eliminar de los archivos temporales del módulo
    empresa_lq = self.empresa_cargada(nombre)
    del empresa_lq

    # Eliminación de productos, servicios y ofertas laborales 
    # Eliminación de contratos con empleados
    pass 
      
# %%
modulo_ad = Administrativo()
modulo_lab = Laboral()
modulo_tur = Turista()
modulo_est = Estudiantil()
modulo_com = Comercio()




cliente = Cliente("Cliente", "2000", "12345") #Crear Cliente
cliente.acceder_modulo(1)                     #Acceder a módulo administrativo

cliente.modulo.crearEmpresa("ElectriCaribe", "tipo", "nr_empleados", "list_empleados", "list_servicios", "ofertas_laborales", "1000")
cliente.modulo.crearEmpresa("Triple A", "tipo", "nr_empleados", "list_empleados", "list_servicios", "ofertas_laborales", "2000")
cliente.modulo.crearEmpresa("Gases del Caribe", "tipo", "nr_empleados", "list_empleados", "list_servicios", "ofertas_laborales", "3000")

cliente.modulo.acceder_Empresa("Triple A")
print(cliente.modulo.empresa.nombre)

cliente.modulo.liquidar_Empresa("ElectriCaribe")
