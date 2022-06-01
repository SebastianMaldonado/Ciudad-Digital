from Base_datos import *


class Modulo:
    def discriminar(self, lista, ind, criterio):
        lista_rs = []

        for prod in lista:
            if (ind == 1):       # Cantidad Mínima
                if (criterio >= prod.cantidad):
                    lista_rs.append(prod)
            elif (ind == 2):     # Nombre
                if (criterio == prod.nombre):
                    lista_rs.append(prod)
            elif (ind == 3):     # Cod. Fabricante
                if (criterio == prod.fabricante.cod):
                    lista_rs.append(prod)
            elif (ind == 4):     # Precio Máximo
                if (criterio <= prod.precio):
                    lista_rs.append(prod)
            else:
                lista_rs.append(prod)

        return lista_rs

    #-------------------------------- |Comprar Productos| --------------------------------#
    # Una vez seleccionada una empresa se podrán añadir productos a su catálogo
    # Estos quedarán registrados en el objeto de la empresa
    #   y serán añadidos al archivo

    def comprar_prod(self):
        # prod[1] : [1] si es producto | [2] servicio
        for prod in self.carrito:
            if (prod[1] == 1):  # Si es producto
                prod[2].cantidad -= 1
            else:  # Si es servicio
                prod[2].cupo -= 1
            Base_datos.modificar_db(prod[1], prod[2])
