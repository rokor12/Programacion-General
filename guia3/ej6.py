def esPar(numero):
    if numero%2 == 0:
        resultado = True
    else:
        resultado = False
    return resultado

def condicion(numero1,numero2):
    resultado = ""
    if esPar(numero1):
        if numero2 < numero1:
            resultado = "Correcto!"
        else:
            resultado = "Incorrecto!"
    else:
        if numero2 > numero1:
            resultado = "Correcto!"
        else:
            resultado = "Incorrecto!"
    return resultado
def main():
    numero1 = int(input("Ingrese un numero entero positivo: "))
    numero2 = 0
    if esPar(numero1):
        numero2 = int(input("Ingrese un numero menor que "+str(numero1)+": "))
    else:
        numero2 = int(input("Ingrese un numero mayor que "+str(numero1)+": "))
    print(condicion(numero1,numero2))
main()
