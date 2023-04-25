def main():
    numero = int(input("Ingrese numeros enteros positivos (finalice con 0): "))
    menor = numero
    mayor = numero

    while numero!=0:
        if numero < menor:
            menor = numero
        elif numero > mayor:
            mayor = numero
        numero = int(input())
    print("El mayor es " + str(mayor) + " y el menor es " + str(menor))
main()
