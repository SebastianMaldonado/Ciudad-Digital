#%%
from Principal import *

from tkinter import *
from PIL import ImageTk, Image  
import pyautogui

#%%
def iniciar () :
    cliente = Cliente("cliente", 1000, 1)
    abrir_ventana2()

def abrir_ventana2 () :
    width, height = pyautogui.size()
    ventana.withdraw()
    vent2 = Toplevel()

    vent2.geometry(str(int(8*width/10)) + "x" + str(int(8*height/10)))


def abrir_ventana3 () :
    vent2.withdraw()


#%%
#Variables de la interfaz
menu = []
pos_menu = 0
width, height = pyautogui.size()

# Ventana principal (Raíz)
ventana = Tk()
ventana.title ("Ciudad Digital")
ventana.geometry(str(int(8*width/10)) + "x" + str(int(8*height/10)))
ventana.config()

# Primera ventana
portada = Image.open("Window (1).png")
portada = portada.resize((int(8*width/10), int(8*height/10)))
portada = ImageTk.PhotoImage(portada)

menu = Label(image = portada)
menu.config(width = int(8*width/10), height = int(8*height/10))
menu.pack(fill = "x")

boton = Button(command = iniciar)
boton.bind("<Return>", iniciar)
boton.place(x = 0, y = 0)

ventana.mainloop()
# %%
