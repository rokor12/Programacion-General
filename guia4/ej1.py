def main():
    numeros_pares_ingresados = 0
    while numeros_pares_ingresados < 5:
        es_par = False
        multiplo_de_4 = False
        
        numero = int(input("Ingrese numero entero: "))
        
        if numero % 2 == 0: #es par
            es_par = True
            numeros_pares_ingresados += 1
        if numero % 4 == 0: #es divisible por 4
            multiplo_de_4 = True
        
        if multiplo_de_4: #si es multiplo de 4, es si o si par
            print("Numero Par. Tambien multiplo de 4 .Total de numeros pares ingresados: " + str(numeros_pares_ingresados))
        elif es_par: #es solamente par
            print("Numero Par. Total de numeros pares ingresados: " + str(numeros_pares_ingresados))
    print("FIN")
main()
