def esPerfecto(numero):
    suma_divisores = 0
    for n in range(1,numero):
        if numero%n == 0:
            suma_divisores += n
    return suma_divisores == numero
def main():
    c = 0
    n = 2
    while c<4:
        if esPerfecto(n):
            print(n)
            c+=1
        n+=1
main()
