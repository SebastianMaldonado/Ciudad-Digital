import tkinter as tk
from tkinter import END, Button, ttk
from turtle import width
from typing import Text
from tkinter import *


def Menu():
    for ele in window.winfo_children():
        ele.destroy()
    bglabel = tk.Label(window, image=bg)
    bglabel.pack()
    mainbutton = tk.Button(
        window,
        image=mainBuImage,
        command=Menu2,
        bg="#44089B",
        bd=1,
        relief="flat",
        overrelief="raised",
        borderwidth=2,
    )
    mainbutton.place(x=290, y=718)
    ExitButton = tk.Button(
        window,
        image=exitBuImage,
        command=window.destroy,
        bg="#44089B",
        bd=1,
        relief="flat",
        overrelief="raised",
        borderwidth=2,
    )
    ExitButton.place(x=570, y=718)


def Menu2():
    for ele in window.winfo_children():
        ele.destroy()
    Canva = tk.Canvas(window)
    Canva.pack()
    Input_box = tk.Entry(Canva)
    Canva.create_window(200, 140, window=Input_box)
    bg2label = tk.Label(Canva, width=1123, height=748, bg="#3046c3")
    bg2label.pack()
    returnButton = tk.Button(
        Canva,
        image=backImage,
        bd=1,
        height=50,
        width=130,
        relief="flat",
        overrelief="raised",
        bg="#FFCBB4",
        command=Menu,
    )
    returnButton.place(x=10, y=730)
    LoginButton = tk.Button(
        Canva,
        image=LoginImage,
        bd=1,
        height=80,
        width=130,
        relief="flat",
        overrelief="raised",
        bg="#FFCBB4",
        command=Menu3
    )
    LoginButton.place(x=490, y=420)
    Input_box.pack()


def Menu3():
    for ele in window.winfo_children():
        ele.destroy()
    Canva2 = tk.Label(window)
    Canva2.pack()
    bg3label = tk.Label(Canva2, image=bg3)
    bg3label.pack()
    returnButton = tk.Button(
        Canva2,
        image=backImage,
        bd=1,
        height=50,
        width=130,
        relief="flat",
        overrelief="raised",
        bg="#FFCBB4",
        command=Menu,
    )
    returnButton.place(x=10, y=730)
    LaboralButton = tk.Button(
        Canva2,
        image=LaboralImage,
        bd=1,
        relief="flat",
        overrelief="raised",
        bg="#FFCBB4",
        command=Menu4,
    )
    LaboralButton.place(x=300, y=300)
    ComercioButton = tk.Button(
        Canva2,
        image=ComercioImage,
        bd=1,
        relief="flat",
        overrelief="raised",
        bg="#FFCBB4",
        command=Menu5,
    )
    ComercioButton.place(x=600, y=300)

    TurismoButton = tk.Button(
        Canva2,
        image=TuristaImage,
        bd=1,
        relief="flat",
        overrelief="raised",
        bg="#FFCBB4",
        command=Menu6,
    )
    TurismoButton.place(x=300, y=450)

    EstudiantilButton = tk.Button(
        Canva2,
        image=EstuImage,
        bd=1,
        relief="flat",
        overrelief="raised",
        bg="#FFCBB4",
        command=Menu7,
    )
    EstudiantilButton.place(x=600, y=450)

    AdminButton = tk.Button(
        Canva2,
        image=AdminImage,
        bd=1,
        relief="flat",
        overrelief="raised",
        bg="#FFCBB4",
        command=Menu8,
    )
    AdminButton.place(x=450, y=600)


def Menu4():
    for ele in window.winfo_children():
        ele.destroy()
    Canva3 = tk.Label(window)
    Canva3.pack()
    bg4label = tk.Label(Canva3)
    bg4label.pack()
    returnButton = tk.Button(
        Canva3,
        image=backImage,
        bd=1,
        height=50,
        width=130,
        relief="flat",
        overrelief="raised",
        bg="#FFCBB4",
        command=Menu3,
    )
    returnButton.place(x=10, y=730)


def Menu5():
    for ele in window.winfo_children():
        ele.destroy()
    Canva4 = tk.Label(window)
    Canva4.pack()
    bg5label = tk.Label(Canva4)
    bg5label.pack()
    returnButton = tk.Button(
        Canva4,
        image=backImage,
        bd=1,
        height=50,
        width=130,
        relief="flat",
        overrelief="raised",
        bg="#FFCBB4",
        command=Menu3,
    )
    returnButton.place(x=10, y=730)


def Menu6():
    for ele in window.winfo_children():
        ele.destroy()
    Canva5 = tk.Label(window)
    Canva5.pack()
    bg6label = tk.Label(Canva5)
    bg6label.pack()
    returnButton = tk.Button(
        Canva5,
        image=backImage,
        bd=1,
        height=50,
        width=130,
        relief="flat",
        overrelief="raised",
        bg="#FFCBB4",
        command=Menu3,
    )
    returnButton.place(x=10, y=730)


def Menu7():
    for ele in window.winfo_children():
        ele.destroy()
    Canva6 = tk.Label(window)
    Canva6.pack()
    bg7label = tk.Label(Canva6)
    bg7label.pack()
    returnButton = tk.Button(
        Canva6,
        image=backImage,
        bd=1,
        height=50,
        width=130,
        relief="flat",
        overrelief="raised",
        bg="#FFCBB4",
        command=Menu3,
    )
    returnButton.place(x=10, y=730)


def Menu8():
    for ele in window.winfo_children():
        ele.destroy()
    Canva7 = tk.Label(window)
    Canva7.pack()
    bg8label = tk.Label(Canva7, image=Adminbg4)
    bg8label.pack()
    returnButton = tk.Button(
        Canva7,
        image=backImage,
        bd=1,
        height=50,
        width=130,
        relief="flat",
        overrelief="raised",
        bg="#FFCBB4",
        command=Menu3,
    )
    returnButton.place(x=10, y=730)
    global swFinanciera, swInmobiliaria, swSuministroG
    global swSuministroA, swSuministroE, ID

    swFinanciera = tk.BooleanVar()
    FinancieraButton = ttk.Checkbutton(
        Canva7, text="Financiera", variable=swFinanciera)
    FinancieraButton.place(x=300, y=150)

    swInmobiliaria = tk.BooleanVar()
    InmobiliariaButton = ttk.Checkbutton(
        Canva7, text="Inmobiliaria", variable=swInmobiliaria
    )
    InmobiliariaButton.place(x=300, y=200)

    swSuministroG = tk.BooleanVar()
    SuministrosGButton = ttk.Checkbutton(
        Canva7, text="Servicio de gas", variable=swSuministroG
    )
    SuministrosGButton.place(x=300, y=250)

    swSuministroA = tk.BooleanVar()
    SuministroAButton = ttk.Checkbutton(
        Canva7, text="Servicio de agua", variable=swSuministroA
    )
    SuministroAButton.place(x=600, y=150)

    swSuministroE = tk.BooleanVar()
    SuministrosEButton = ttk.Checkbutton(
        Canva7, text="Suministro Electricidad", variable=swSuministroE
    )
    SuministrosEButton.place(x=600, y=200)

    InfoButton = tk.Button(Canva7, image=BuscarImage, command=getInfo, bg="#FFCBB4", bd=1,
                           relief="flat", overrelief="raised")
    InfoButton.place( x =540, y =565)

def getInfo():
    # This lists are used to get the selections from the user
    Tipoempresa = []
    switchasignment(Tipoempresa=Tipoempresa)
    

def switchasignment(Tipoempresa: list[str]):
    if (swFinanciera.get()):
        Tipoempresa.append("Financiera")
    if (swInmobiliaria.get()):
        Tipoempresa.append("Inmobiliaria")
    if (swSuministroG.get()):
        Tipoempresa.append("Servicio de gas")
    if (swSuministroA.get()):
        Tipoempresa.append("Suministro de agua")
    if (swSuministroE.get()):
        Tipoempresa.append("Suministro de electricidad")


window = tk.Tk()
window.title("Digital City")
window.geometry("1123x794")
window.resizable(False, False)
bg = tk.PhotoImage(
    file="C:\\Users\\cberr\\OneDrive\\Documents\\OOP_CODE\\Window (1).png"
)
bg2 = tk.PhotoImage(
    file="C:\\Users\\cberr\\OneDrive\\Documents\\OOP_CODE\\Window_2.png"
)
bg3 = tk.PhotoImage(
    file="C:\\Users\\cberr\\OneDrive\\Documents\\OOP_CODE\\Window_3 (2).png"
)
Adminbg4 = tk.PhotoImage(
    file="C:\\Users\\cberr\\OneDrive\\Documents\\OOP_CODE\\Admin_window.png"
)
mainBuImage = tk.PhotoImage(
    file="C:\\Users\\cberr\\OneDrive\\Documents\\OOP_CODE\\MainButton.png"
)
exitBuImage = tk.PhotoImage(
    file="C:\\Users\\cberr\\OneDrive\\Documents\\OOP_CODE\\ExitButton.png"
)
backImage = tk.PhotoImage(
    file="C:\\Users\\cberr\\OneDrive\\Documents\\OOP_CODE\\Back.png"
)
LoginImage = tk.PhotoImage(
    file="C:\\Users\\cberr\\OneDrive\\Documents\\OOP_CODE\\Login.png"
)
AdminImage = tk.PhotoImage(
    file="C:\\Users\\cberr\\OneDrive\\Documents\\OOP_CODE\\Administrativo.png"
)
TuristaImage = tk.PhotoImage(
    file="C:\\Users\\cberr\\OneDrive\\Documents\\OOP_CODE\\Turista.png"
)
EstuImage = tk.PhotoImage(
    file="C:\\Users\\cberr\\OneDrive\\Documents\\OOP_CODE\\Estudiantil.png"
)
ComercioImage = tk.PhotoImage(
    file="C:\\Users\\cberr\\OneDrive\\Documents\\OOP_CODE\\Comercio.png"
)
LaboralImage = tk.PhotoImage(
    file="C:\\Users\\cberr\\OneDrive\\Documents\\OOP_CODE\\Laboral.png"
)
BuscarImage = tk.PhotoImage(
    file="C:\\Users\\cberr\\OneDrive\\Documents\\OOP_CODE\\Buscar.png"
)
Menu()

window.mainloop()
