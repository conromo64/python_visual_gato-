##https://youtu.be/nk4UXoUOLQI
from tkinter import *
raiz= Tk()
raiz.resizable(0,0)
raiz.title("Calculadora simple")
##raiz.iconbitmap("patos155.ico")
raiz.geometry("400x300")
raiz.config(bg="SkyBlue1")
str_resultado=StringVar()
str_inicial=StringVar()
#creamos una funcion para sumar
def sumar():
    dato1=float(texto1.get())
    dato2=float(texto2.get())
    resultado=dato1+dato2
    cadena=str(resultado)
    str_resultado.set(cadena)

#creamos una funcion para sumar
def restar():
    dato1=float(texto1.get())
    dato2=float(texto2.get())
    resultado=dato1-dato2
    cadena=str(resultado)
    str_resultado.set(cadena)

#creamos una funcion para sumar
def multiplicar():
    dato1=float(texto1.get())
    dato2=float(texto2.get())
    resultado=dato1*dato2
    cadena=str(resultado)
    str_resultado.set(cadena)

##creamos una funcion para sumar
def dividir():
    dato1=float(texto1.get())
    dato2=float(texto2.get())
    resultado=dato1/dato2
    cadena=str(resultado)
    str_resultado.set(cadena)

str_inicial.set("0")
etiqueta1=Label(raiz, bg="SkyBlue1", text="Dato 1 ",font='Helvetica 18 bold')
etiqueta1.place(x=20, y =20)
etiqueta2=Label(raiz, bg="SkyBlue1", text="Dato 2 ",font='Helvetica 18 bold')
etiqueta2.place(x=20, y=60)
etiqueta3=Label(raiz, bg="SkyBlue1", text="Resultado  ",font='Helvetica 18 bold' )
etiqueta3.place(x=20, y=100)
texto1=Entry(raiz,textvariable=str_inicial,font='Helvetica 18 bold',width=10)
texto1.place(x=200, y=20)
texto2=Entry(raiz,font='Helvetica 18 bold',width=10)
texto2.place(x=200, y=60)
texto3=Entry(raiz,textvariable=str_resultado,font='Helvetica 18 bold',width=10,state = DISABLED)
texto3.place(x=200, y=100)
boton1=Button(raiz,text="+",command=sumar,font='Helvetica 18 bold',width=3).place(x=20,y=150)
boton2=Button(raiz,text="-",command=restar,font='Helvetica 18 bold',width=3).place(x=100,y=150)
boton3=Button(raiz,text="*",command=multiplicar,font='Helvetica 18 bold',width=3).place(x=180,y=150)
boton4=Button(raiz,text="/",command=dividir,font='Helvetica 18 bold',width=3).place(x=260,y=150)





raiz.mainloop()


