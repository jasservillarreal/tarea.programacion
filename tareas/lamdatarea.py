""" Jasser Esteban Vilarreal Buitrago"""
# SANTIAGO ECHEVERRI ARTEAGA #
"""PROGRAMACION"""

########################################

#lamda factorial de un numero
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

# Ejemplo de uso
numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")

###################################################

#lamda factorial con una lista

factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
numeros = [5, 4, 3, 2, 1]
resultados = [factorial(numero) for numero in numeros]
print(resultados)

##########################################################


#lamda con una funcion prime
prime = lambda f: lambda x: x * f(f)(x - 1) if x > 0 else 1
factorial = prime(prime)

# Ejemplo de uso
numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")

#####################################


x = lambda n:factorial(7)

print(x(7))

########################################

cuadrado = lambda x: x**2  # Define una función lambda en una sola línea

print(0**0)