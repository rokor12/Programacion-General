def aBinario(numero): #sin usar strings
    res = 0
    i = 0
    while numero:
        if numero%2:
            res += 1 * (10**i)
        i += 1
        numero //= 2
    return res
def aBinarioB(numero): #usando strings
    res = ""
    while numero:
        if numero%2:
            res = '1' + res
        else:
            res = '0' + res
        numero //= 2
    return res
def main():
    numero = int(input("Ingrese un numero menor a 1000: "))
    print("Numero a binario: " + str(aBinario(numero)))
    print("Numero a binario: " + aBinarioB(numero))
main()
