from Base_datos import *

'''
|====================================================================|
*                      |Módulo Administrativo|
* Descripcion:                                                        
*   Módulo encargado de la administración de las empresas
*   Por medio de él es posible crear, cargar, eliminar y acceder a ellas
|====================================================================|
'''
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