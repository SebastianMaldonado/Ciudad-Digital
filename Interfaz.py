from email.mime import image
from tkinter import *
ventana = Tk()
ventana.geometry("1123x794")
Background = PhotoImage(file="C:\\Users\\cberr\\Downloads\\Window (1).png")
frame2 = Frame(ventana, bg="red")
frame2.place(x=550, y=198)
canvas1 = Canvas(ventana, width=1123, height=794)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=Background,
                     anchor="nw")
getStarted = Button(ventana, text="", bg="blue")
getStarted.place(x=450, y=750)
ventana.mainloop()
