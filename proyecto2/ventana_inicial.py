## Importamos todos los elementos de la libreria TKINTER
from tkinter import *


#Creamos un objeto de la clase Tk provista por la libreria tkinter
raiz= Tk()

#variable
nombre=StringVar()
#Modificamos algunas de las propíedades del objeto creado mediante el iso de los metodos asociados a la clase
raiz.title("Hola")
raiz.resizable(1,1)
raiz.iconbitmap("patos155.ico")
raiz.geometry("1200x500")
raiz.config(bg="SkyBlue1")

#Creamos un marco dentro de la ventana raiz
marco=Frame()
#empacamos (metemos) el marco dentro de la ventana raiz
marco.pack()
#Modoficamos las propiedades del marco
marco.pack(side="left", anchor="s")
marco.pack(fill="y", expand="true")
marco.pack(fill="both", expand="true")
marco.config(bg="blue")
marco.config(height="400", width="1000")
marco.config(bd=35)
marco.config(relief="groove")
marco.config(cursor="hand2")
marco.config(cursor="pirate")


#Etiquetas
etiqueta1=Label(marco, text="Hola mundo 3 ")
etiqueta1.place(x=400, y =20)
Label(marco, text="Adios mundo ",fg="red", bg="black", font=("Informal Roman",45)).place(x=400, y=250)
imagen=PhotoImage(file="patos155.png")
Label(marco,image=imagen).place(x=10,y=10)

#Campo detexto

texto1=Entry(marco)
texto1.place(x=500, y=20)

texto2=Entry(marco,textvariable=nombre)
texto2.place(x=800, y=20)

#creamos una funcion para asignar el texto1 a texto2>
def asignar1a2():
	nombre.set(texto1.get())



boton=Button(marco,text="Saludar", command=asignar1a2).place(x=650,y=15)


raiz.mainloop()
