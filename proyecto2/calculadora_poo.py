from tkinter import *
class Calculadora:
    ## definicion de las propiedades de la clase y asignación de valores por omisión
    def __init__(self,n1,mem,opant):
        self.n1=n1
        self.mem=mem
        self.opant=opant

    ## Definición de metodos de asignación para las propiedades de la clase
    def setn1(self,n1):
        self.n1=n1
    def setn2(self,n2):
        self.n2=n2
    def setmem(self,mem):
        self.mem=mem
    def setopant(self,opant):
        self.opant=opant
    def suma(self):
        return (self.n1+self.n2)

    ##definción del metodo que ejecuta la operación y guarda la operación y resultado a la memoria
    def ejecuta(self):
        result=0
        if (self.opant=="+"):
            result=self.mem+self.n1
        elif (self.opant=="-"):
            result=self.mem-self.n1
        elif (self.opant=="*"):
            result=self.mem*self.n1
        elif (self.opant=="/"):
            result=self.mem/self.n1
        else:
            result=self.n1
        self.mem=result
        res=str(result)
        return result


## Crea un objeto de la clase claculadora
r=Calculadora(0,0,"#")

## Crea un objeto de la clase Tkinter para la ventana
raiz= Tk()
## Crea la variable para la asignación del resultado y dato
str_resultado=StringVar()
str_dato=StringVar()
##Configura el aspecto de nuestra ventana
raiz.resizable(1,0)
raiz.title("Calculadora simple")
raiz.resizable(1,1)
#raiz.iconbitmap("patos155.ico")
raiz.geometry("400x300")
raiz.config(bg="SkyBlue1")



#creamos una funcion para sumar
def sumar():
    r.setn1(float(texto1.get()))
    str_resultado.set(r.ejecuta())
    r.setopant("+")
    str_dato.set("0")


#creamos una funcion para restar
def restar():
    r.setn1(float(texto1.get()))
    str_resultado.set(r.ejecuta())
    r.setopant("-")
    str_dato.set("")

#creamos una funcion para multiplicar
def multiplicar():
    r.setn1(float(texto1.get()))
    str_resultado.set(r.ejecuta())
    r.setopant("*")
    str_dato.set("0")

#creamos una funcion para dividir
def dividir():
    r.setn1(float(texto1.get()))
    str_resultado.set(r.ejecuta())
    r.setopant("/")
    str_dato.set("0")

#creamos una funcion para igual
def igual():
    r.setn1(float(texto1.get()))
    str_resultado.set(r.ejecuta())
    r.setmem(0)
    r.setopant("#")
    str_dato.set("0")

def cero():
    if (str_dato.get()!="0"):
        str_dato.set(str_dato.get()+"0")

def uno():
    if (str_dato.get()=="0"):
        str_dato.set("1")
    else:
        str_dato.set(str_dato.get()+"1")


## Creamos los objetos para mostrar información y leer datos de nuestro usuario
etiqueta1=Label(raiz, bg="SkyBlue1", text="Dato ",font='Helvetica 18 bold')
etiqueta1.place(x=20, y =20)
str_dato.set("0")
texto1=Entry(raiz,textvariable=str_dato,font='Helvetica 18 bold',width=10)
texto1.place(x=200, y=20)
str_resultado.set("0")
etiqueta3=Label(raiz, bg="SkyBlue1", text="Resultado  ",font='Helvetica 18 bold' )
etiqueta3.place(x=20, y=60)

texto3=Entry(raiz,textvariable=str_resultado,font='Helvetica 18 bold',width=10,state = DISABLED)
texto3.place(x=200, y=60)

## Creamos los botones de nuestra calculadora
boton1=Button(raiz,text="+",command=sumar,font='Helvetica 18 bold',width=3).place(x=20,y=150)
boton2=Button(raiz,text="-",command=restar,font='Helvetica 18 bold',width=3).place(x=100,y=150)
boton3=Button(raiz,text="*",command=multiplicar,font='Helvetica 18 bold',width=3).place(x=180,y=150)
boton4=Button(raiz,text="/",command=dividir,font='Helvetica 18 bold',width=3).place(x=260,y=150)
boton5=Button(raiz,text="=",command=igual,font='Helvetica 18 bold',width=3).place(x=340,y=150)

boton6=Button(raiz,text="0",command=cero,font='Helvetica 18 bold',width=3).place(x=20,y=210)
boton7=Button(raiz,text="1",command=uno,font='Helvetica 18 bold',width=3).place(x=100,y=210)

##Ciclo de ejecución
raiz.mainloop()
