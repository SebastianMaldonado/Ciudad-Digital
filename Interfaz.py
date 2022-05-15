import tkinter as tk
from tkinter import Button, ttk

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
    bg2label = tk.Label(Canva, image=bg2)
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

def Menu3():
    for ele in window.winfo_children():
        ele.destroy()
    Canva2 = tk.Canvas(window)
    Canva2.pack()


window = tk.Tk()
window.title("Digital City")
window.geometry("1123x794")
window.resizable(False, False)
bg = tk.PhotoImage(
    file="C:\\Users\\cberr\\OneDrive\\Documents\\OOP_CODE\\Window (1).png"
)
mainBuImage = tk.PhotoImage(
    file="C:\\Users\\cberr\\OneDrive\\Documents\\OOP_CODE\\MainButton.png"
)
exitBuImage = tk.PhotoImage(
    file="C:\\Users\\cberr\\OneDrive\\Documents\\OOP_CODE\\ExitButton.png"
)
bg2 = tk.PhotoImage(
    file="C:\\Users\\cberr\\OneDrive\\Documents\\OOP_CODE\\Window_2.png"
)
backImage = tk.PhotoImage(
    file="C:\\Users\\cberr\\OneDrive\\Documents\\OOP_CODE\\Back.png"
)
Menu()

window.mainloop()
