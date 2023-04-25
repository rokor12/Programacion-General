def condicion(numeroA, numeroB):
    numero_menor = 0
    numero_mayor = 0
    diferencia   = 0
    resultado    = ""
    #hayo el orden de los numeros
    if numeroA <= numeroB:
        numero_menor = numeroA
        numero_mayor = numeroB
    else:
        numero_menor = numeroB
        numero_mayor = numeroA
    
    #compruebo la condicion
    diferencia = numero_mayor - numero_menor
    if (diferencia >= numero_menor) and (diferencia <= numero_mayor):
        resultado = "SI cumple condicion"
    else:
        resultado = "NO cumple condicion"

    return resultado

def main():
    numeroA = int(input("Ingrese un numero A: "))
    numeroB = int(input("Ingrese un numero B: "))
    print(condicion(numeroA,numeroB))
main()
