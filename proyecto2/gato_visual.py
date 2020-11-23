##https://youtu.be/nk4UXoUOLQI
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
## Para ventana nueva
import tkinter as tk
from time import sleep
##Conexion a Base de Datos
import pymysql


## Crea la ventana principal
raiz= Tk()
raiz.resizable(1,1)
raiz.title("Gato")
raiz.iconbitmap("patos155.ico")
raiz.geometry("500x400")
raiz.config(bg="SkyBlue1")
ganador="x"
turno =StringVar()
a_insertar="hola"
j1=StringVar()
j2=StringVar()
v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()
v5=StringVar()
v6=StringVar()
v7=StringVar()
v8=StringVar()
v9=StringVar()
str_jugada=StringVar()
str_contG=StringVar()
str_contB=StringVar()
str_ident=StringVar()
str_nombre=StringVar()
str_puntos=StringVar()

str_contG.set("0")
str_contB.set("0")
str_ident.set("0")
str_nombre.set("")
str_puntos.set("0")

cont_jugada=0
v1.set("1")
v2.set("2")
v3.set("3")
v4.set("4")
v5.set("5")
v6.set("6")
v7.set("7")
v8.set("8")
v9.set("9")
turno.set("G")

imggato = PhotoImage(file="gato.png")
imgbenito = PhotoImage(file="benito.png")
imgblanco = PhotoImage(file="blanco.png")
fondo = PhotoImage(file="fondo.png")

def lista_usuarios():
    ## Combo de Usuarios
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='test')
    cursor = conn.cursor()
    cursor.execute('select Nom_usuario from usuarios')
    tcs = []

    for row in cursor:
        tcs.append(row)
    cursor.close()
    conn.close()
    return  tcs


def nuevo_usuario():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='test')
    cursor1 = conn.cursor()
    sql = "insert into usuarios (nom_usuario) values (%s)"
    datos = str(str_nombre.get())
    cursor1.execute(sql,datos)
    conn.commit()
    cursor1.close()
    conn.close()
    lista = lista_usuarios()
    tc['values'] = lista
    bn['values'] = lista

    ##cadena='insert into usuarios (nom_usuario) values("'+datos+'")'
    ##messagebox.showinfo(message=cadena)

def marcador_usuario():
    global ganador
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='test')
    cursor1 = conn.cursor()
    datos = ganador
    sql = 'update usuarios set puntos=puntos+1 where nom_usuario="'+datos+'"'
    cursor1.execute(sql)
    conn.commit()
    cursor1.close()
    conn.close()
    messagebox.showinfo(message=sql)

def abrir_ventana():
    global  a_insertar
    raiz.withdraw
    ventana = tk.Toplevel(raiz)
    ventana.geometry('500x300')
    ventana.configure(background='SkyBlue1')

    ## Etiquetas
    et1 = Label(ventana, bg='SkyBlue1', text="Identificador: ", font='Helvetica 18 bold')
    et1.place(x=10, y=10)
    et2 = Label(ventana, bg='SkyBlue1', text="        Nombre: ", font='Helvetica 18 bold')
    et2.place(x=10, y=50)
    et3 = Label(ventana, bg='SkyBlue1', text="         Puntos: ", font='Helvetica 18 bold')
    et3.place(x=10, y=90)
    ##et.pack(padx=5, pady=5, ipadx=5, ipady=5)

    ##Cajas de Texto
    ident = Entry(ventana, textvariable=str_ident, font='Helvetica 18 bold', width=5)
    ident.place(x=200, y=10)
    nombre_u = Entry(ventana, textvariable=str_nombre, font='Helvetica 18 bold', width=20)
    nombre_u.place(x=200, y=50)
    puntos = Entry(ventana, textvariable=str_puntos, font='Helvetica 18 bold', width=5, state=DISABLED)
    puntos.place(x=200, y=90)

    ## Botones
    agrega = Button(ventana, cursor="circle", bg="blue", text="Agraga", font='Helvetica 12 bold', fg="white", command=nuevo_usuario, width=10, height=2)
    agrega.place(x=150, y=150)




def nuevo():
    boton1.config(state=NORMAL)
    boton2.config(state=NORMAL)
    boton3.config(state=NORMAL)
    boton4.config(state=NORMAL)
    boton5.config(state=NORMAL)
    boton6.config(state=NORMAL)
    boton7.config(state=NORMAL)
    boton8.config(state=NORMAL)
    boton9.config(state=NORMAL)

    boton1.config(bg="white")
    boton2.config(bg="white")
    boton3.config(bg="white")
    boton4.config(bg="white")
    boton5.config(bg="white")
    boton6.config(bg="white")
    boton7.config(bg="white")
    boton8.config(bg="white")
    boton9.config(bg="white")

    boton1.config(image=imgblanco)
    boton2.config(image=imgblanco)
    boton3.config(image=imgblanco)
    boton4.config(image=imgblanco)
    boton5.config(image=imgblanco)
    boton6.config(image=imgblanco)
    boton7.config(image=imgblanco)
    boton8.config(image=imgblanco)
    boton9.config(image=imgblanco)
    v1.set("1")
    v2.set("2")
    v3.set("3")
    v4.set("4")
    v5.set("5")
    v6.set("6")
    v7.set("7")
    v8.set("8")
    v9.set("9")
    turno.set("G")
    reinicia.config(state=DISABLED)
    partida.config(state=DISABLED)

def partida():
    str_contG.set("0")
    str_contB.set("0")
    tc.config(state=NORMAL)
    bn.config(state=NORMAL)
    nuevo()

def cierra():
    boton1.config(state=DISABLED)
    boton2.config(state=DISABLED)
    boton3.config(state=DISABLED)
    boton4.config(state=DISABLED)
    boton5.config(state=DISABLED)
    boton6.config(state=DISABLED)
    boton7.config(state=DISABLED)
    boton8.config(state=DISABLED)
    boton9.config(state=DISABLED)

def celebra_gato():
    vec_img = [PhotoImage(file="./dongato/0.gif")]
    vec_img.append(PhotoImage(file="./dongato/1.gif"))
    vec_img.append(PhotoImage(file="./dongato/2.gif"))
    vec_img.append(PhotoImage(file="./dongato/3.gif"))
    vec_img.append(PhotoImage(file="./dongato/4.gif"))
    vec_img.append(PhotoImage(file="./dongato/5.gif"))
    vec_img.append(PhotoImage(file="./dongato/6.gif"))
    vec_img.append(PhotoImage(file="./dongato/7.gif"))
    vec_img.append(PhotoImage(file="./dongato/8.gif"))
    vec_img.append(PhotoImage(file="./dongato/9.gif"))
    vec_img.append(PhotoImage(file="./dongato/10.gif"))
    vec_img.append(PhotoImage(file="./dongato/11.gif"))
    vec_img.append(PhotoImage(file="./dongato/12.gif"))
    vec_img.append(PhotoImage(file="./dongato/13.gif"))
    vec_img.append(PhotoImage(file="./dongato/14.gif"))
    vec_img.append(PhotoImage(file="./dongato/15.gif"))
    vec_img.append(PhotoImage(file="./dongato/16.gif"))
    vec_img.append(PhotoImage(file="./dongato/17.gif"))
    vec_img.append(PhotoImage(file="./dongato/18.gif"))
    vec_img.append(PhotoImage(file="./dongato/19.gif"))
    vec_img.append(PhotoImage(file="./dongato/20.gif"))
    vec_img.append(PhotoImage(file="./dongato/21.gif"))
    vec_img.append(PhotoImage(file="./dongato/22.gif"))

    for i in range(0,22):
        imagen.config(image=vec_img[i])
        raiz.update()
        sleep(.2)
    imagen.config(image=fondo)
    raiz.update()

def celebra_benito():
    vec_img = [PhotoImage(file="./benito/b0.gif")]
    vec_img.append(PhotoImage(file="./benito/b1.gif"))
    vec_img.append(PhotoImage(file="./benito/b2.gif"))
    vec_img.append(PhotoImage(file="./benito/b3.gif"))
    vec_img.append(PhotoImage(file="./benito/b4.gif"))
    vec_img.append(PhotoImage(file="./benito/b5.gif"))
    vec_img.append(PhotoImage(file="./benito/b6.gif"))
    vec_img.append(PhotoImage(file="./benito/b7.gif"))
    vec_img.append(PhotoImage(file="./benito/b8.gif"))
    vec_img.append(PhotoImage(file="./benito/b9.gif"))
    vec_img.append(PhotoImage(file="./benito/b10.gif"))
    vec_img.append(PhotoImage(file="./benito/b11.gif"))

    for i in range(0,11):
        imagen.config(image=vec_img[i])
        raiz.update()
        sleep(.2)
    imagen.config(image=fondo)
    raiz.update()

def valida():
    global cont_jugada
    global ganador
    mensaje=""
    if (v1.get() == v2.get() and v1.get()== v3.get()):
        if v1.get()=="G":
            mensaje="G"
        else:
            mensaje = "B"

    if (v4.get() == v5.get() and v4.get()== v6.get()):
        if v4.get()=="G":
            mensaje="G"
        else:
            mensaje = "B"

    if (v7.get() == v8.get() and v7.get()== v9.get()):
        if v7.get()=="G":
            mensaje="G"
        else:
            mensaje = "B"

    if (v1.get() == v4.get() and v1.get()== v7.get()):
        if v1.get()=="G":
            mensaje="G"
        else:
            mensaje = "B"
    if (v2.get() == v5.get() and v2.get()== v8.get()):
        if v2.get()=="G":
            mensaje="G"
        else:
            mensaje = "B"

    if (v3.get() == v6.get() and v3.get()== v9.get()):
        if v3.get()=="G":
            mensaje="G"
        else:
            mensaje = "B"

    if (v1.get() == v5.get() and v1.get()== v9.get()):
        if v1.get()=="G":
            mensaje="G"
        else:
            mensaje = "B"

    if (v3.get() == v5.get() and v3.get()== v7.get()):
        if v3.get()=="G":
            mensaje="G"
        else:
            mensaje = "B"

    if mensaje!="":
        if mensaje=="G":
            mensaje = "el ganador es "+tc.get()
            aux=int(str_contG.get())
            aux=aux+1
            str_contG.set(str(aux))
            celebra_gato()
            ganador=tc.get()
            marcador_usuario()

        else:
            mensaje = "el ganador es " + bn.get()
            aux = int(str_contB.get())
            aux = aux + 1
            str_contB.set(str(aux))
            celebra_benito()
            ganador = bn.get()
            marcador_usuario()
        messagebox.showinfo(message=mensaje)
        cierra()
        reinicia.config(state=NORMAL)
        partida.config(state=NORMAL)
        cont_jugada = 0




    cont_jugada=cont_jugada+1
    ##str_contB.set(str(cont_jugada))
    if cont_jugada==9:
        messagebox.showinfo(message="Empate")
        ##cierra()
        reinicia.config(state=NORMAL)
        partida.config(state=NORMAL)
        cont_jugada=0

#creamos una funcion para sumar
def eb1():
    if turno.get()=="G":
        boton1.config(image=imggato)
        boton1.config(state=DISABLED)
        boton1.config(bg="blue")
        v1.set(turno.get())
        turno.set("B")
    else:
        boton1.config(image=imgbenito)
        boton1.config(state=DISABLED)
        boton1.config(bg="red")
        v1.set(turno.get())
        turno.set("G")
    siguiente["text"] = turno.get()
    valida()

def eb2():
    if turno.get()=="G":
        boton2.config(image=imggato)
        boton2.config(state=DISABLED)
        boton2.config(bg="blue")
        v2.set(turno.get())
        turno.set("B")
    else:
        boton2.config(image=imgbenito)
        boton2.config(state=DISABLED)
        boton2.config(bg="red")
        v2.set(turno.get())
        turno.set("G")
    siguiente["text"] = turno.get()
    valida()

def eb3():
    if turno.get()=="G":
        boton3.config(image=imggato)
        boton3.config(state=DISABLED)
        boton3.config(bg="blue")
        v3.set(turno.get())
        turno.set("B")
    else:
        boton3.config(image=imgbenito)
        boton3.config(state=DISABLED)
        boton3.config(bg="red")
        v3.set(turno.get())
        turno.set("G")
    siguiente["text"] = turno.get()
    valida()

def eb4():
    if turno.get()=="G":
        boton4.config(image=imggato)
        boton4.config(state=DISABLED)
        boton4.config(bg="blue")
        v4.set(turno.get())
        turno.set("B")
    else:
        boton4.config(image=imgbenito)
        boton4.config(state=DISABLED)
        boton4.config(bg="red")
        v4.set(turno.get())
        turno.set("G")
    siguiente["text"] = turno.get()
    valida()

def eb5():
    if turno.get()=="G":
        boton5.config(image=imggato)
        boton5.config(state=DISABLED)
        boton5.config(bg="blue")
        v5.set(turno.get())
        turno.set("B")
    else:
        boton5.config(image=imgbenito)
        boton5.config(state=DISABLED)
        boton5.config(bg="red")
        v5.set(turno.get())
        turno.set("G")
    siguiente["text"] = turno.get()
    valida()

def eb6():
    if turno.get()=="G":
        boton6.config(image=imggato)
        boton6.config(state=DISABLED)
        boton6.config(bg="blue")
        v6.set(turno.get())
        turno.set("B")
    else:
        boton6.config(image=imgbenito)
        boton6.config(state=DISABLED)
        boton6.config(bg="red")
        v6.set(turno.get())
        turno.set("G")
    siguiente["text"] = turno.get()
    valida()

def eb7():
    if turno.get()=="G":
        boton7.config(image=imggato)
        boton7.config(state=DISABLED)
        boton7.config(bg="blue")
        v7.set(turno.get())
        turno.set("B")
    else:
        boton7.config(image=imgbenito)
        boton7.config(state=DISABLED)
        boton7.config(bg="red")
        v7.set(turno.get())
        turno.set("G")
    siguiente["text"] = turno.get()
    valida()

def eb8():
    if turno.get()=="G":
        boton8.config(image=imggato)
        boton8.config(state=DISABLED)
        boton8.config(bg="blue")
        v8.set(turno.get())
        turno.set("B")
    else:
        boton8.config(image=imgbenito)
        boton8.config(state=DISABLED)
        boton8.config(bg="red")
        v8.set(turno.get())
        turno.set("G")
    siguiente["text"] = turno.get()
    valida()

def eb9():
    if turno.get()=="G":
        boton9.config(image=imggato)
        boton9.config(state=DISABLED)
        boton9.config(bg="blue")
        v9.set(turno.get())
        turno.set("B")
    else:
        boton9.config(image=imgbenito)
        boton9.config(state=DISABLED)
        boton9.config(bg="red")
        v9.set(turno.get())
        turno.set("G")
    siguiente["text"] = turno.get()
    valida()


def man_usuarios():
    abrir_ventana()

## Nombre del primer usuario
def nombre1(event):
    tc.config(state=DISABLED)

## Nombre del primer usuario
def nombre2(event):
    bn.config(state=DISABLED)



##-------------------------- Procedimiento Principal------------------------------------------------

## Combo de Usuarios
tc=ttk.Combobox(raiz, font='Helvetica 12 bold', width=10)
tc.place(x=295, y = 120)
bn=ttk.Combobox(raiz, font='Helvetica 12 bold', width=10)
bn.place(x=295, y = 160)
lista=lista_usuarios()
tc['values']=lista
bn['values']=lista
tc.bind("<<ComboboxSelected>>",nombre1)
bn.bind("<<ComboboxSelected>>",nombre2)

et_sig=Label(raiz, bg="SkyBlue1", text="Turno: ", font='Helvetica 18 bold')
et_sig.place(x=295, y = 80)
siguiente=Label(raiz, bg="white", text="G", font='Helvetica 18 bold')
siguiente.place(x=420, y = 80)

## e_contG=Label(raiz, bg="SkyBlue1",text="Benito: ", textvariable=j1, font='Helvetica 18 bold')
## e_contG.place(x=295, y = 120)
contG=Entry(raiz, textvariable=str_contG, font='Helvetica 18 bold', width=5,state = DISABLED)
contG.place(x=420, y= 120)

## e_contB=Label(raiz, bg="SkyBlue1", text="Benito: ", textvariable=j2, font='Helvetica 18 bold')
## e_contB.place(x=295, y = 160)
contB=Entry(raiz, textvariable=str_contB, font='Helvetica 18 bold', width=5,state = DISABLED)
contB.place(x=420, y=160)



boton1 = Button(raiz, cursor="mouse", bd=20, bg="white", relief="flat",image=imgblanco, textvariable=v1, command=eb1, width=30, height=30)
boton1.place(x=20, y=20)
boton2 = Button(raiz, cursor="mouse", bd=20, bg="white", relief="flat",image=imgblanco, textvariable=v2, command=eb2, width=30, height=30)
boton2.place(x=100, y=20)
boton3 = Button(raiz, cursor="mouse", bd=20, bg="white", relief="flat",image=imgblanco, textvariable=v3, command=eb3, width=30, height=30)
boton3.place(x=180, y=20)


boton4 = Button(raiz, cursor="mouse", bd=20, bg="white", relief="flat",image=imgblanco, textvariable=v4, command=eb4, width=30, height=30)
boton4.place(x=20, y=120)
boton5 = Button(raiz, cursor="mouse", bd=20, bg="white", relief="flat",image=imgblanco, textvariable=v5, command=eb5, width=30, height=30)
boton5.place(x=100, y=120)
boton6 = Button(raiz, cursor="mouse", bd=20, bg="white", relief="flat",image=imgblanco, textvariable=v6, command=eb6, width=30, height=30)
boton6.place(x=180, y=120)

boton7 = Button(raiz, cursor="mouse", bd=20, bg="white", relief="flat",image=imgblanco, textvariable=v7, command=eb7, width=30, height=30)
boton7.place(x=20, y=220)
boton8 = Button(raiz, cursor="mouse", bd=20, bg="white", relief="flat",image=imgblanco, textvariable=v8, command=eb8, width=30, height=30)
boton8.place(x=100, y=220)
boton9 = Button(raiz, cursor="mouse", bd=20, bg="white", relief="flat",image=imgblanco, textvariable=v9, command=eb9, width=30, height=30)
boton9.place(x=180, y=220)

reinicia = Button(raiz, cursor="circle", bg="blue", text="Juego Nuevo", font='Helvetica 12 bold', fg="yellow", command=nuevo, width=10, height=2, state=DISABLED)
reinicia.place(x=295, y=210)

partida = Button(raiz, cursor="circle", bg="yellow", text="Partida Nueva", font='Helvetica 12 bold', fg="blue", command=partida, width=10, height=2, state=DISABLED)
partida.place(x=295, y=270)

imagen=Label(raiz, image=fondo)
imagen.place(x = 1, y = 1)

n_ventana = Button(raiz, cursor="circle", bg="yellow", text="Usuarios", font='Helvetica 12 bold', fg="blue", command=man_usuarios, width=10, height=2)
n_ventana.place(x=295, y=330)



raiz.mainloop()