def positivoNegativo(numero):
    resultado = ""
    if numero > 0 :     #es positivo
        resultado = "positivo"
    elif numero < 0 :   #es negativo
        resultado = "negativo"
    else:               #es cero
        resultado = "cero"
    return resultado

def tipoDeNumero(numero):
    resultado = ""
    if numero == int(numero):   #es entero
        resultado = "entero"
        if numero > 0:          #es entero natural
            resultado = "entero natural"
    else:                       #es real
        resultado = "real"
    return resultado

def main():
    numero = float(input("Ingrese un numero: "))
    print("El numero es " + positivoNegativo(numero) + " y " + tipoDeNumero(numero))
main()

