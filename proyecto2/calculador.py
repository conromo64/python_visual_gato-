continuar="s"
while continuar=="s":
    ##Comienza el ciclo while
    print("Dato 1")
    numero1=float(input())
    print("Dato 2")
    numero2=float(input())
    print("Suma(+)/Resta(-)/Multiplicación(*)/División(/)")
    operacion=input()
    if operacion=="+":
        resultado=numero1+numero2
    elif operacion=="-":
        resultado=numero1-numero2
    elif operacion=="*":
        resultado=numero1*numero2
    elif operacion=="/":
        resultado=numero1/numero2
    else:
        resultado=0
    print("El resultado es ",resultado)
    print("desea continuar s/N")
    continuar=input()
    ## termina el ciclo while
print("adios")