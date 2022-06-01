# %%
from Base_datos import *
from abc import ABC, abstractmethod

# Importación de Módulos
from Modulo_Administrativo import Administrativo
from Modulo_Estudiantil import Estudiantil
from Modulo_Comercio import Comercial
from Modulo_Turista import Turista

cliente = None


class Cliente:
    def __init__(self, nombre, codigo, cont):
        self.nombre = nombre
        self.codigo = codigo
        self.cont = cont
        self.cv = None
        self.modulo = None

    def acceder_modulo(self, tipo):
        if (tipo == 1):
            self.modulo = Administrativo()
        elif (tipo == 2):
            self.modulo = Comercial()
        elif (tipo == 3):
            self.modulo = Estudiantil()
        elif (tipo == 4):
            self.modulo = Turista()


# %%
def inicializar():
    cliente = Cliente("cliente", 1000, 1)


def selec_mod(mod):
    cliente.acceder_modulo(mod)
