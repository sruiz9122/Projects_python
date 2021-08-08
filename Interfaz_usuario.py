# Paso1. Instalar libreria

# Paso2. Importar libreria y crear una ventana principal y mainloop()
from tkinter import *

main_window = Tk()
main_window.title("Probando interfaz de usuario")

# Paso3. Frames / Marco
main_frame = Frame(main_window,  # Ventana que va a contener el frame
                   bg="#ffffff",  # Background color código html -> RGB red green blue
                   height=1000,  # Tamaño de alto
                   width=1000,  # ancho
                   padx=50,  # Margen en el eje x
                   pady=50,  # Margen en el eje y
                   cursor='arrow')  # Especifica el cursor que le quiero poner al mouse

tittle_label = Label(main_frame,
                     text='Hola interfaces de usuario',
                     font=('Arial', 15),
                     fg='#000000',
                     justify=CENTER,
                     bg='#000000')

main_frame.pack()
""""
imagen = PhotoImage(file='python_img.png')
img_label = Label(main_frame,
                  image=imagen,
                  bg='#FFFFFF')

img_label.pack()
"""

def accion_button():
    global botonText
    if botonText == "Hola":
        botonText = "Click"
    else:
        botonText = "Hola"
    boton.config(text=botonText)

botonText = "Hola"
boton = Button(main_frame,
               text="Hola",
               bg='#00FFFF',
               fg='#FF0000',
               command=accion_button)

boton.pack()

#main_window.mainloop()

ventana = Tk()
ventana.title("Posicionamiento")
ventana.geometry("400x200")
boton = Button(ventana, text="Primer Widget").place(x=10, y=10)
etiqueta = Label(ventana, text="Segundo Widget").place(x=200, y=10)
etiqueta2 = Label(ventana, text="TERCER Widget").place(x=10, y=60)
etiqueta3 = Label(ventana, text="CU4RTO Widget").place(x=200, y=60)
ventana.mainloop()


