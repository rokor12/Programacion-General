def main():
    total = 0
    aplazos = 0
    aprobados = 0
    promocionados = 0
    promedio_general = 0
    suma_notas = 0
    nota = int(input("Ingrese nota: "))
    while nota!=0:
        if nota>0 and nota<=10:
            total += 1
            suma_notas += nota
            if nota<4:
                aplazos += 1
            elif nota<8:
                aprobados += 1
            else:
                promocionados += 1
        nota = int(input("Ingrese nota: "))
    
    promedio_general = suma_notas / total
    porcentaje_aplazados = aplazos / total * 100
    porcentaje_aprobados = aprobados / total * 100
    porcentaje_promocionados = promocionados / total * 100
    
    print("Cantidad de aplazos: {} ({}%)".format(aplazos,porcentaje_aplazados))
    print("Cantidad de aprobados: {} ({}%)".format(aprobados,porcentaje_aprobados))
    print("Cantidad de promocionados: {} ({}%)".format(promocionados,porcentaje_promocionados))
    print("Promedio general: {}".format(promedio_general))
main()
