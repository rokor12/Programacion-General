def desaproboAlgunParcial(nota1: int,nota2: int,nota3: int) -> bool:
    if nota1<4 or nota2<4 or nota3<4:
        return True
    else:
        return False
def main():
    nota1 = int(input("Ingrese la nota del primer parcial: "))
    nota2 = int(input("Ingrese la nota del segundo parcial: "))
    nota3 = int(input("Ingrese la nota del tercer parcial: "))
    if desaproboAlgunParcial(nota1,nota2,nota3):
        recuperatorio = int(input("Ingrese la nota del recuperatorio: "))
        if recuperatorio<4:
            print("El alumno fue aplazado")
        else:
            promedio_general = (nota1+nota2+nota3+recuperatorio)/4
            print("Promedio general = "+str(promedio_general))
            print("El alumno debera rendir final.")
    else:
        promedio_general = (nota1+nota2+nota3)/3
        print("Promedio general = "+str(promedio_general))
        if promedio_general>7:
            print("El alumno promosiono la materia")
        else:
            print("El alumno debera rendir final.")
main()
