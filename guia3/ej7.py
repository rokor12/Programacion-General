def estanIgualmenteDistanciados(numero1: int, numero2: int, numero3: int) -> bool:
    resultado = False
    numero_menor = 0
    numero_medio = 0
    numero_mayor = 0
    
    #Parte copiada del ejercicio 2
    if (numero1 <= numero2) and (numero1 <= numero3) :   #numero1 es el menor
        numero_menor = numero1
    elif (numero2 <= numero1) and (numero2 <= numero3) : #numero2 es el menor
        numero_menor = numero2
    else:                                                #numero3 es el menor
        numero_menor = numero3

    if ( (numero1 >= numero2) and (numero1 <= numero3) ) or ( (numero1 >= numero3) and (numero1 <= numero2) ):    #numero1 es el del medio
        numero_medio = numero1
    elif ( (numero2 >= numero1) and (numero2 <= numero3) ) or ( (numero2 >= numero3) and (numero2 <= numero1) ):  #numero2 es el del medio
        numero_medio = numero2
    else:                                                                                                         #numero3 es el del medio
        numero_medio = numero3

    #condicion para hayar el numero_mayor
    if (numero1>=numero2) and (numero1>=numero3):   #numero1 es el menor
        numero_mayor = numero1
    elif (numero2>=numero1) and (numero2>=numero3): #numero2 es el menor
        numero_mayor = numero2
    else:                                           #numero3 es el menor
        numero_mayor = numero3
    
    #Compruebo que esten igualmente distanciados
    if (numero_menor+numero_mayor)/2 == numero_medio:
        resultado = True
    else:
        resultado = False
    return resultado

def main():
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    numero3 = int(input("Ingrese el tercer numero: "))
    if estanIgualmenteDistanciados(numero1,numero2,numero3):
        print("Estan igualmente distanciados!")
    else:
        print("NO Estan igualmente distanciados!")
main()
