from Principal import *

import tkinter as tk
import pyautogui

from Principal import inicializar

# Variables

cliente = Cliente("cliente", 1000, 1)


class Portada ():
    def __init__(self, width, height):
        self.width = int(8*width/10)
        self.height = int(8*height/10)

        self.inter_p = 1

        self.ventana = tk.Tk()
        self.ventana.geometry(str(self.width) + "x" + str(self.height))
        self.ventana.title("Digital City")
        self.ventana.iconbitmap("Logo.ico")
        # Ventanas
        bg = tk.PhotoImage(
            file="Window (1).png"
        )
        bg2 = tk.PhotoImage(
            file="Window_3.png"
        )
        bg3 = tk.PhotoImage(
            file="Window_2.png"
        )
        bg4 = tk.PhotoImage(
            file="Window4.png"
        )
        bg5 = tk.PhotoImage(
            file="Admin_Window.png"
        )
        bg6 = tk.PhotoImage(
            file="Window5.png"
        )
        bg7 = tk.PhotoImage(
            file="Window6.png"
        )

        self.vent1 = tk.Label(self.ventana, image=bg,
                              width=self.width, height=self.height)
        self.vent2 = tk.Label(self.ventana, image=bg2,
                              width=self.width, height=self.height)
        self.vent3 = tk.Label(self.ventana, image=bg3,
                              width=self.width, height=self.height)
        self.vent4 = tk.Label(self.ventana, image=bg4,
                              width=self.width, height=self.height)
        self.vent5 = tk.Label(self.ventana, image=bg6,
                              width=self.width, height=self.height)
        self.vent6 = tk.Label(self.ventana, image=bg5,
                              width=self.width, height=self.height)
        self.vent7 = tk.Label(self.ventana, image=bg7,
                              width=self.width, height=self.height)
        self.vent8 = tk.Label(self.ventana, bg="blue",
                              width=self.width, height=self.height)

        self.Portada()
        self.Pant_Mod()
        self.Pant_ModAd1()
        self.Pant_ModAd2()
        self.Pant_ModAd3()
        self.Pant_ModAd4()
        self.Pant_ModAd5()
        self.Modulo()

        self.vent1.pack()
        self.ventana.mainloop()

    #----------------------------|Botones de las Pantallas|----------------------------#

    def Portada(self):
        self.boton1 = tk.Button(
            self.vent1, text="Iniciar", command=self.inicializar, height=3, width=75)
        self.boton1.place(x=500, y=750)

    def Pant_Mod(self):
        self.boton2 = tk.Button(self.vent2, text="Volver",
                                command=self.volver, width=50, height=3)
        self.mod1 = tk.Button(
            self.vent2, text="Modulo Administrativo", command=self.mod1, height=3, width=25)
        self.mod2 = tk.Button(
            self.vent2, text="Modulo Comercial", command=self.mod2, height=3, width=25)
        self.mod3 = tk.Button(
            self.vent2, text="Modulo Estudiantil", command=self.mod3, height=3, width=25)
        self.mod4 = tk.Button(
            self.vent2, text="Modulo Turistico", command=self.mod4, height=3, width=25)

        self.mod1.place(x=500, y=250)
        self.mod2.place(x=800, y=250)
        self.mod3.place(x=500, y=400)
        self.mod4.place(x=800, y=400)
        self.boton2.place(x=550, y=550)

    def Pant_ModAd1(self):  # Pantalla 1 del Modulo Administrativo
        self.mesage = tk.Label(
            self.vent3, text="BIENVENIDO AL MÓDULO ADMINISTRATIVO", height=4,  width=70, bg="#667bf2")
        self.acc_emp = tk.Button(
            self.vent3, text="Acceder Empresa", command=self.pant_acc_emp, height=3, width=25)
        self.cre_emp = tk.Button(
            self.vent3, text="Crear Empresa", command=self.pant_cre_emp, height=3, width=25)
        self.volver_pr = tk.Button(
            self.vent3, text="Volver", command=self.volver2_pr, height=3, width=25)

        self.mesage.place(x=550, y=80)
        self.acc_emp.place(x=700, y=300)
        self.cre_emp.place(x=700, y=400)
        self.volver_pr.place(x=700, y=500)

    def Pant_ModAd2(self):  # Pantalla de Acceder Empresa
        self.mesage = tk.Label(
            self.vent4, text="DIGITE EL CODIGO DE LA EMPRESA QUE QUIERE BUSCAR", height=4,  width=70, bg="#667bf2")
        self.codigo1 = tk.Text(self.vent4, width=10,
                               height=2, font=("Arial", 35))
        self.acc_boton = tk.Button(
            self.vent4, text="Acceder Empresa", command=self.acceder_empresa)
        self.mesage.place(x=550, y=80)
        self.codigo1.place(x=640, y=200)
        self.acc_boton.place(x=720, y=340)

    def Pant_ModAd3(self):  # Pantalla de Crear Empresa
        self.mesage1 = tk.Label(
            self.vent6, text="CREACIÓN DE EMPRESA", height=4,  width=70)
        self.mesage2 = tk.Label(self.vent6, text="Código", height=2,  width=20)
        self.mesage3 = tk.Label(self.vent6, text="Nombre", height=2,  width=20)
        self.mesage4 = tk.Label(self.vent6, text="Tipo", height=2,  width=20)
        self.codigo = tk.Text(self.vent6, width=50, height=5,  bd=3)
        self.nombre = tk.Text(self.vent6, width=50, height=5, bd=3)
        self.tipo = tk.Text(self.vent6, width=50, height=5, bd=3)
        self.crear = tk.Button(
            self.vent6, text="Crear Empresa", command=self.crear_empresa)

        self.mesage1.place(x=550, y=130)
        self.mesage2.place(x=560, y=200)
        self.mesage3.place(x=560, y=360)
        self.mesage4.place(x=560, y=500)
        self.codigo.place(x=550, y=250)
        self.nombre.place(x=550, y=400)
        self.tipo.place(x=550, y=550)
        self.crear.place(x=600, y=650)

    def Pant_ModAd4(self):  # Pantalla 3 del Modulo Administrativo
        self.mesage = tk.Label(self.vent5, text="DIGITE EL CODIGO DE LA EMPRESA QUE QUIERE BUSCAR",
                               height=4,  width=70, bg="#667bf2", font=("Arial", 14))
        self.emp_info = tk.Label(
            self.vent5, height=10, width=70, font=("Arial", 14))
        self.cargar_info_emp(self.emp_info)
        self.ver_prod = tk.Button(
            self.vent5, text="Ver productos", command=self.lista_prods, height=3, width=40)
        self.ver_serv = tk.Button(
            self.vent5, text="Ver servicios", command=self.lista_servs, height=3, width=40)
        self.volver2 = tk.Button(
            self.vent5, text="Volver", command=self.volver2_f, height=3, width=40)

        self.mesage.place(x=400, y=80)
        self.emp_info.place(x=370, y=200)
        self.ver_prod.place(x=620, y=450)
        self.ver_serv.place(x=620, y=500)
        self.volver2.place(x=620, y=550)

    def Pant_ModAd5(self):
        self.emp_pinfo = tk.Label(self.vent7, height=14, width=60)
        self.cargar_info_prod(self.emp_pinfo)
        self.volver3 = tk.Button(
            self.vent7, text="Volver", command=self.volver_emp)

        # Añadir Producto/Servicio
        self.mesage = tk.Label(self.vent7, text="AÑADIR EMPRESA",
                               height=4,  width=70, bg="#667bf2", font=("Arial", 13))
        self.mesage2 = tk.Label(
            self.vent7, text="Cantidad", height=2,  width=20)
        self.mesage3 = tk.Label(
            self.vent7, text="Nombre del producto", height=2,  width=20)
        self.mesage4 = tk.Label(
            self.vent7, text="Categoria", height=2,  width=20)
        self.mesage5 = tk.Label(self.vent7, text="Precio", height=2,  width=20)
        self.mesage6 = tk.Label(
            self.vent7, text="Eliminar producto", height=2,  width=20)
        self.cant_p = tk.Text(self.vent7, width=30, height=10)
        self.nombre_p = tk.Text(self.vent7, width=30, height=10)
        self.cat_p = tk.Text(self.vent7, width=30, height=10)
        self.pr_p = tk.Text(self.vent7, width=30, height=10)
        self.add_prod = tk.Button(
            self.vent7, text="Añadir al Catálogo", command=self.add_producto, height=3, width=25)

        # Eliminar Producto/Servicio
        self.nombre_el = tk.Text(self.vent7, width=30, height=10)
        self.eli_prod = tk.Button(
            self.vent7, text="Eliminar del Catálogo", command=self.eliminar_producto, height=2, width=25)

        self.mesage.place(x=400, y=80)
        self.mesage2.place(x=400, y=200)
        self.mesage3.place(x=700, y=200)
        self.mesage4.place(x=400, y=420)
        self.mesage5.place(x=700, y=420)
        self.mesage6.place(x=1000, y=200)
        self.cant_p.place(x=400, y=240)
        self.nombre_p.place(x=700, y=240)
        self.cat_p.place(x=400, y=460)
        self.pr_p.place(x=700, y=460)
        self.add_prod.place(x=500, y=650)

        self.nombre_el.place(x=1000, y=240)
        self.eli_prod.place(x=1020, y=410)

        self.emp_pinfo.place(x=950, y=460)
        self.volver3.place(x=1000, y=690)

    def cargar_info_prod(self, emp_pinfo):
        if (cliente.modulo != None):
            if (cliente.modulo.empresa == None):
                emp_pinfo.config(text="Empresa no cargada")
            else:
                texto = ""
                if (self.inter_p == 1):  # Mostrar Productos
                    for prod in cliente.modulo.empresa.productos:
                        texto = texto + str(prod.cantidad) + "\t" + prod.fabricante.nombre + "\t" + \
                            prod.nombre + "\t" + prod.categoria + \
                            "\t" + str(prod.precio) + "\n"
                else:  # Mostrar Servicios
                    for prod in cliente.modulo.empresa.servicios:
                        texto = texto + str(prod.cupo) + "\t" + prod.proveedor.nombre + "\t" + \
                            prod.nombre + "\t" + prod.categoria + \
                            "\t" + str(prod.precio) + "\n"

                emp_pinfo.config(text=texto)
        else:
            emp_pinfo.config(text="Modulo no cargado")

    def cargar_info_emp(self, emp_info):
        if (cliente.modulo != None):
            if (cliente.modulo.empresa == None):
                emp_info.config(text="Empresa no cargada")
            else:
                emp = cliente.modulo.empresa
                texto = emp.codigo + "\n" + emp.nombre + "\n" + emp.tipo
                emp_info.config(text=texto)
        else:
            emp_info.config(text="Modulo no cargado")

    def Pant_ModRs(self):
        pass

    #----------------------------|Portada|----------------------------#
    def inicializar(self):
        print("Iniciando")
        self.vent1.pack_forget()
        self.vent2.pack()

    #----------------------------|Modulos|----------------------------#
    def volver(self):
        self.vent1.pack()
        self.vent2.pack_forget()

    def mod1(self):  # Módulo Administrativo
        self.vent2.pack_forget()
        self.vent3.pack()
        cliente.acceder_modulo(1)
        print(cliente.nombre)

    def mod2(self):  # Módulo Comercial
        self.vent2.pack_forget()
        self.vent8.pack()
        cliente.acceder_modulo(2)

    def mod3(self):  # Módulo Estudiantil
        self.vent2.pack_forget()
        self.vent8.pack()
        cliente.acceder_modulo(3)

    def mod4(self):  # Módulo Turístico
        self.vent2.pack_forget()
        self.vent8.pack()
        cliente.acceder_modulo(4)

    #----------------------------|Modulo Administrativo|----------------------------#

    def pant_cre_emp(self):
        self.vent3.pack_forget()
        self.vent6.pack()

    def pant_acc_emp(self):
        self.vent3.pack_forget()
        self.vent4.pack()

    def lista_prods(self):
        self.cargar_info_prod(self.emp_pinfo)
        self.inter_p = 1
        self.vent5.pack_forget()
        self.vent7.pack()

    def lista_servs(self):
        self.cargar_info_prod(self.emp_pinfo)
        self.inter_p = 2
        self.vent5.pack_forget()
        self.vent7.pack()

    def acceder_empresa(self):
        cod = self.codigo1.get("1.0", tk.END)[:-1]
        print("|"+cod+"|")
        cliente.modulo.acceder_Empresa(cod)

        if (cliente.modulo.empresa != None):
            print(cliente.modulo.empresa)
            self.vent4.pack_forget()
            self.vent5.pack()
            self.cargar_info_emp(self.emp_info)
            self.cargar_info_prod(self.emp_pinfo)
        else:
            print("empresa no existente")

    def crear_empresa(self):
        cod = self.codigo.get("1.0", tk.END)[:-1]
        cliente.modulo.acceder_Empresa(cod)

        if (cliente.modulo.empresa == None):
            cliente.modulo.crearEmpresa(cod, self.nombre.get("1.0", tk.END)[
                                        :-1], self.tipo.get("1.0", tk.END)[:-1])
            cliente.modulo.acceder_Empresa(self.codigo.get("1.0", tk.END)[:-1])
            print(cliente.modulo.empresa)
            self.vent6.pack_forget()
            self.vent5.pack()
            self.cargar_info_emp(self.emp_info)
            self.cargar_info_prod(self.emp_pinfo)
        else:
            print("empresa ya existente")

    def add_producto(self):
        if (cliente.modulo != None):
            cliente.modulo.añadir_prod(self.inter_p, self.cant_p.get("1.0", tk.END)[:-1], self.nombre_p.get(
                "1.0", tk.END)[:-1], self.cat_p.get("1.0", tk.END)[:-1], self.pr_p.get("1.0", tk.END)[:-1])
            self.cargar_info_prod(self.emp_pinfo)

    def eliminar_producto(self):
        if (cliente.modulo != None):
            cliente.modulo.eliminar_prod(
                self.inter_p, self.nombre_el.get("1.0", tk.END)[:-1])
            self.cargar_info_prod(self.emp_pinfo)

    def volver2_f(self):
        self.vent5.pack_forget()
        self.vent3.pack()

    def volver2_pr(self):
        self.vent3.pack_forget()
        self.vent2.pack()

    def volver_emp(self):
        self.vent7.pack_forget()
        self.vent5.pack()
    #----------------------------|Resto de Módulos|----------------------------#

    def Modulo(self):
        opciones = ["Sin criterio", "Cantidad Mínima",
                    "Nombre", "Fabricante", "Precio Máximo"]
        self.criterio = tk.StringVar(self.vent8)
        self.criterio.set("Seleccione un criterio de Búsqueda")

        self.crit_sl = tk.OptionMenu(self.vent8, self.criterio, *opciones)
        self.crit_sl.config(width=30, height=10)
        self.crit = tk.Text(self.vent8, width=30, height=10)
        self.buscar = tk.Button(self.vent8, text="Buscar",
                                width=15, height=3, command=self.buscar_lista)
        self.lista = tk.Label(self.vent8, text="Productos")

        self.crit_sl.pack()
        self.crit.pack()
        self.buscar.pack()
        self.lista.pack()

    def buscar_lista(self):
        crit = self.crit.get("1.0", tk.END)[:-1]

        if (self.criterio.get() == "Sin criterio"):
            if (cliente.modulo != None):
                cliente.modulo.buscar_prod(0, "")
                self.actualizar_lista(self.lista)
        elif (self.criterio.get() == "Cantidad Mínima"):
            crit = int(crit)
            if (cliente.modulo != None):
                cliente.modulo.buscar_prod(1, crit)
                self.actualizar_lista(self.lista)
        elif (self.criterio.get() == "Nombre"):
            if (cliente.modulo != None):
                cliente.modulo.buscar_prod(2, crit)
                self.actualizar_lista(self.lista)
        elif (self.criterio.get() == "Fabricante"):
            if (cliente.modulo != None):
                cliente.modulo.buscar_prod(3, crit)
                self.actualizar_lista(self.lista)
        elif (self.criterio.get() == "Precio Máximo"):
            crit = int(crit)
            if (cliente.modulo != None):
                cliente.modulo.buscar_prod(4, crit)
                self.actualizar_lista(self.lista)

    def actualizar_lista(self, lista):
        texto = ""
        for prod in cliente.modulo.lista:
            texto = texto + str(prod.cantidad) + "\t" + prod.fabricante.nombre + "\t" + \
                prod.nombre + "\t" + prod.categoria + \
                "\t" + str(prod.precio) + "\n"

        lista.config(text=texto)


# %%
width, height = pyautogui.size()
portada = Portada(width, height)
# %%
