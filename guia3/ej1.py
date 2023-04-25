def calculadora(numero1: int, numero2: int, operador: str):
    resultado = 0
    if operador == "+":     #suma
        resultado = numero1 + numero2
    elif operador == "-":   #resta
        resultado = numero1 - numero2
    elif operador == "*":   #multiplicacion
        resultado = numero1 * numero2
    else:                   #division
        resultado = numero1 / numero2
    return resultado
def main():
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("ingrese el segundo numero: "))
    operador = input("Ingrese la operacion (+, -, *, /): ")
    resultado = calculadora(numero1,numero2,operador)
    print(str(numero1)+" "+operador+" "+str(numero2)+" = "+str(resultado))
main()
