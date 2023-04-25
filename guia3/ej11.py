def mensaje(c_1_metros,c_5_metros,metros_a_cubrir):
    esPosibleCubrir = True
    c_5_metros_usados = 0
    c_1_metros_usados = 0

    #intento usar primero los de 5 metros
    if c_5_metros >= metros_a_cubrir//5: #sobran o alcanzan la cantidad de c_5_metros
        c_5_metros_usados = metros_a_cubrir//5
        metros_a_cubrir %= 5 #me quedo con los metros restantes (operacion de resto)
    else: #uso la cantidad que tengo de c_5_metros
        metros_a_cubrir -= c_5_metros * 5
        c_5_metros_usados = c_5_metros
    #la cantidad de metros restantes deben ser usados si o si por c_1_metros
    if c_1_metros >= metros_a_cubrir: #alcanza los c_1_metros
        c_1_metros_usados = metros_a_cubrir #metros restantes
    else: #no alcanzan los c_1_metros
        esPosibleCubrir = False
    
    if esPosibleCubrir:
        print("Es posible cubrir el tendido.")
        print("Sugerencia:")
        print(str(c_5_metros_usados) + " unidades de caño de 5 metros")
        print(str(c_1_metros_usados) + " unidades de caño de 1 metro")
    else:
        print("No es posible cubrir el tendido.")

def main():
    c_1_metros = int(input("Cantidad de caños de 1 metro: "))
    c_5_metros = int(input("Cantidad de caños de 5 metros: "))
    metros_a_cubrir = int(input("Metros totales a cubrir: "))
    mensaje(c_1_metros,c_5_metros,metros_a_cubrir)
main()
