def libre(vec_gato,posicion):
    jugado=True
    if posicion==1:
        if (vec_gato[0][0]=="1"):
            jugado=False
    elif posicion==2:
        if (vec_gato[0][1]=="2"):
            jugado=False
    elif posicion==3:
        if (vec_gato[0][2]=="3"):
            jugado=False
    elif posicion==4:
        if (vec_gato[1][0]=="4"):
            jugado=False
    elif posicion==5:
        if (vec_gato[1][1]=="5"):
            jugado=False
    elif posicion==6:
        if (vec_gato[1][2]=="6"):
            jugado=False
    elif posicion==7:
        if (vec_gato[2][0]=="7"):
            jugado=False
    elif posicion==8:
        if (vec_gato[2][1]=="8"):
            jugado=False
    elif posicion==9:
        if (vec_gato[2][2]=="9"):
            jugado=False
    return jugado

def lee_jugada(vec_gato, turno):
    print("Posición ",turno,": ")
    posicion=int(input())
    while (libre(vec_gato,posicion)):
        print("ya se jugo ese posicion")
        print("Posición ", turno, ": ")
        posicion = int(input())
    if posicion==1:
        vec_gato[0][0]= turno
    elif posicion==2:
        vec_gato[0][1] = turno
    elif posicion==3:
        vec_gato[0][2] = turno
    elif posicion==4:
        vec_gato[1][0] = turno
    elif posicion==5:
        vec_gato[1][1] = turno
    elif posicion==6:
        vec_gato[1][2] = turno
    elif posicion==7:
        vec_gato[2][0] = turno
    elif posicion==8:
        vec_gato[2][1] = turno
    elif posicion==9:
        vec_gato[2][2] = turno
    return vec_gato

def imprime_gato(gato):
    print("  ",gato[0][0]," | ",gato[0][1]," | ",gato[0][2])
    print("---------------")
    print("  ",gato[1][0]," | ",gato[1][1]," | ", gato[1][2])
    print("---------------")
    print("  ",gato[2][0]," | ",gato[2][1]," | ", gato[2][2])

    return


def valida_ganador(gato):
    gano="N"
    if (gato[0][0]==gato[0][1] and gato[0][0]==gato[0][2]):
        gano="S"
        print("gano ",gato[0][0])
    elif (gato[1][0]==gato[1][1] and gato[1][0]==gato[1][2]):
        gano = "S"
        print("gano ", gato[1][0])
    elif (gato[2][0]==gato[2][1] and gato[2][0]==gato[2][2]):
        gano = "S"
        print("gano ", gato[2][0])
    elif (gato[0][0]==gato[1][1] and gato[0][0]==gato[2][2]):
        gano = "S"
        print("gano ", gato[0][0])
    elif (gato[0][2]==gato[1][1] and gato[0][2]==gato[2][0]):
        gano = "S"
        print("gano ", gato[0][0])
    elif (gato[0][0]==gato[1][0] and gato[0][0]==gato[2][0]):
        gano = "S"
        print("gano ", gato[0][0])
    elif (gato[0][1]==gato[1][1] and gato[0][1]==gato[2][1]):
        gano = "S"
        print("gano ", gato[0][0])
    elif (gato[0][2]==gato[1][2] and gato[0][2]==gato[2][2]):
        gano = "S"
        print("gano ", gato[0][0])
    return gano

contx=0
cont0=0
sigue="s"
while (sigue=="s" or sigue=="S"):
    jugador="X"
    termina="N"
    vec_gato=[["1","2","3"],["4","5","6"],["7","8","9"]]
    imprime_gato(vec_gato)
    contador=0
    while (termina=="N" and contador<9):
        vec_gato=lee_jugada(vec_gato, jugador)
        imprime_gato(vec_gato)
        termina=valida_ganador(vec_gato)
        if jugador == "X":
            jugador = "0"
        else:
            jugador = "X"
        contador=contador+1
    if (contador>9):
        print("empate")
        input()
    print("desea continuar s/n ")
    sigue=input()