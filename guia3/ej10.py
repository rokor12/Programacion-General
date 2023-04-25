def multa(velocidad_vehiculo, velocidad_maxima, vehiculo_emergencia):
    velocidad_minima = velocidad_maxima / 2
    if velocidad_vehiculo >= velocidad_minima and velocidad_vehiculo <= velocidad_maxima: #velocidad permitida
        return "No recibe multa"
    elif velocidad_vehiculo < velocidad_minima: # por debajo de la velocidad minima
        if velocidad_vehiculo >= (velocidad_minima - velocidad_minima * (15/100)): # dentro de la tolerancia
            return "Advertencia"
        else:
            return "Recibe multa por entorpecer el transito"
    elif velocidad_vehiculo > velocidad_maxima and not(vehiculo_emergencia): # supera la velocidad_maxima
        if velocidad_vehiculo <= velocidad_maxima + velocidad_maxima * (15/100): # dentro de la tolerancia
            return "Advertencia"
        else:
            return "Recibe multa por exceso de velocidad"
    return "No recibe multa"
def main():
    #tolerancia del 15%
    #minima =  maxima/2
    velocidad_vehiculo  = int(input("Velocidad del vehiculo: "))
    velocidad_maxima    = int(input("Velocidad maxima: "))
    vehiculo_emergencia = input("Emergencia (s/n): ")
    vehiculo_emergencia = vehiculo_emergencia == 's' or vehiculo_emergencia == "S" #transforma el input a booleano
    print(multa(velocidad_vehiculo,velocidad_maxima,vehiculo_emergencia))
main()
