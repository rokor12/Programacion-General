def sumaDigitos(numero):
    mil = numero // 1000
    numero -= mil * 1000
    centenas = numero // 100
    numero -= centenas * 100
    decenas = numero // 10
    numero -= decenas * 10
    unidades = numero
    return mil+decenas == centenas+unidades
def main():
    numero = int(input("ingrese un numero de 4 digitos: "))
    if sumaDigitos(numero):
        print("cumple la condicion")
    else:
        print("no cumple la condicion")
main()
