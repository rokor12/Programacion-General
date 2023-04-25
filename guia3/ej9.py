def bono(sueldo_base):
    b = 0 #bono
    
    if sueldo_base>2000:
        b = sueldo_base * (15/100)
    else:
        b = sueldo_base * (20/100)
    
    return b

def plus(sueldo_base,tiene_hijos,categoria):
    p = 0 #plus
    
    p = plusC(sueldo_base,categoria) #plus por categoria
    
    if categoria < 7:   #solo las categorias 1,2,3,4,5,6 pueden tener plus por hijo
        p += plusH(sueldo_base,tiene_hijos)
    
    return p

def plusH(sueldo_base,tiene_hijos):
    pH = 0
    
    if tiene_hijos:
        pH = sueldo_base * (5/100)
    
    return pH

def plusC(sueldo_base,categoria):
    pC = 0
    if categoria < 4:   #categorias 1,2,3
        pC = sueldo_base * (10/100)
    elif categoria < 7: #categorias 4,5,6
        pC = sueldo_base * (12/100)
    else:               #categorias 7,8,9
        pC = sueldo_base * (20/100)
    
    return pC

def main():
    sueldo_base = int(input("Ingrese el sueldo Base: "))
    tiene_hijos = input("Tiene hijos (s/n)?: ") == 's'
    categoria = int(input("Ingrese la categoria (1-9): "))
    sueldo_final = sueldo_base + bono(sueldo_base) + plus(sueldo_base,tiene_hijos,categoria)
    print("Su sueldo total sera de " + str(sueldo_final))

main()
    
    
