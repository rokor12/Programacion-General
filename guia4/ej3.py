def esPrimo(numero):
    for n in range(2,numero):
        if numero%n == 0:
            return False
    return True
def main():
    cant = int(input("Ingrese cantidad (numero natural): "))
    
    #Primos entre 1 y cant
    print("Primos entre 1 y " + str(cant) + ":")
    for n in range(2,cant):
        if esPrimo(n):
            print(n,end =" ")
    print()
    #Primeros cant primos
    print("Primeros " + str(cant) + " primos:")
    primos_encontrados = 0
    n = 2
    while primos_encontrados < cant:
        if esPrimo(n):
            primos_encontrados += 1
            print(n, end = " ")
        n += 1
    print()
main()
