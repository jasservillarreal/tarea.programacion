""" Jasser Esteban Vilarreal Buitrago"""
# SANTIAGO ECHEVERRI ARTEAGA #
"""PROGRAMACION"""
#Elija tres ejercicios a desarrollar y entreguelos la proxima clase

"""1. Escriba un programa que le pida al usuario diez números y le
diga cuál es el mayor (menor) número de todos."""

# Inicializamos las variables para el mayor y el menor número



mayor_numero = float('-inf')  # Inicializamos con un valor muy pequeño
menor_numero = float('inf')   # Inicializamos con un valor muy grande

# Pedimos al usuario que ingrese diez números

while True:
 for i in range(10):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    
    # Actualizamos el mayor y el menor número si es necesario
    
    if numero > mayor_numero:
        mayor_numero = numero
    if numero < menor_numero:
        menor_numero = numero
   

# Mostramos el resultado


 print(f"El mayor número es: {mayor_numero}")
 print(f"El menor número es: {menor_numero}")


 
 continuar =input("¿Desea intentarlo de nuevo? (Si/No): ")

 if continuar.lower() != 'si':
   
   break  
 
print("Programa terminado.")

