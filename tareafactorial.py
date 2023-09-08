""" Jasser Esteban Vilarreal Buitrago"""
# SANTIAGO ECHEVERRI ARTEAGA #
"""PROGRAMACION"""


def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

numero = int(input("Ingrese un número para calcular su factorial: "))
if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    resultado = factorial(numero)
    print(f"El factorial de {numero} es {resultado}")

    ####################################################


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un número para calcular su factorial: "))
if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    resultado = factorial(numero)
    print(f"El factorial de {numero} es {resultado}")

    ###########################################################################

factorial=lambda n: 1 if n==1 else n*factorial(n-1)
print(factorial(5))

def torre_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f'Mueve disco 1 de {origen} a {destino}')
        return
    torre_hanoi(n - 1, origen, auxiliar, destino)
    print(f'Mueve disco {n} de {origen} a {destino}')
    torre_hanoi(n - 1, auxiliar, destino, origen)

# Cambia el número de discos según tus necesidades
num_discos = 2

torre_hanoi(num_discos, 'A', 'C', 'B')

    