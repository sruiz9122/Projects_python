from tkinter import *

def saludo():
    print("Hola a todos")

def minimizar():
    ventana.iconify()

ventana = Tk()
ventana.title("Ejercicio número 1")
ventana.geometry("400x200")
etiqueta1 = Label(ventana, text="Desde aqupi saludamos").place(x=30, y=50)
etiqueta2 = Label(ventana, text="Desde aqui minimizamos").place(x=30, y=100)
boton1 = Button(ventana, text="Click para saludar", command=saludo).place(x=200, y=50)
boton2 = Button(ventana, text="Click para minimizar", command=minimizar).place(x=200, y=100)
ventana.mainloop()