## Función para la lectura de datos en un vector
def leer_vector():
    datos=[0,0,0,0,0]
    for i in range(0,5):
        datos[i]=int(input("Dime el dato numero {}: ".format(i) ))
    return datos
## Procedimiento de ordenamiento de un vector
def ordena_vector(vector):
    for cont in range(0,5):
        mayor=vector[cont]
        ap_mayor=cont
        for cont2 in range(cont+1,5):
            if mayor < vector[cont2]:
                mayor=vector[cont2]
                ap_mayor=cont2
        vector[ap_mayor]=vector[cont]
        vector[cont]=mayor
    return vector
##  Procedimiento de impresión de los datos contenidos en unn vector
def imprimir_vector(vector):
    print("Los datos ordenados son: ")
    for i in range(0, 5):
        print("dato ",i,vector[i])
    pausa=input()


## prcedimiento principal donde arranca la ejecución del programa
vector=leer_vector()
ordenado=ordena_vector(vector)
imprimir_vector(ordenado)