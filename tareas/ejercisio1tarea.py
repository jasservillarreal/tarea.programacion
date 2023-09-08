""" Jasser Esteban Vilarreal Buitrago"""
# SANTIAGO ECHEVERRI ARTEAGA #
"""PROGRAMACION"""
#Elija tres ejercicios a desarrollar y entreguelos la proxima clase

#1. Escriba un programa que le permita al usuario pasar una
#temperatura de grados centígrados, farenheit o Kelvin a la
#escala térmica que el desee.

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_a_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_a_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_a_celsius(kelvin):
    return kelvin - 273.15

def kelvin_a_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

while True:
    print("Elija una opción de conversión:")
    print("1. Celsius a Fahrenheit")
    print("2. Celsius a Kelvin")
    print("3. Fahrenheit a Celsius")
    print("4. Fahrenheit a Kelvin")
    print("5. Kelvin a Celsius")
    print("6. Kelvin a Fahrenheit")
    print("7. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == '1':
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        resultado = celsius_a_fahrenheit(celsius)
        print(f"{celsius} grados Celsius son equivalentes a {resultado} grados Fahrenheit")
    elif opcion == '2':
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        resultado = celsius_a_kelvin(celsius)
        print(f"{celsius} grados Celsius son equivalentes a {resultado} Kelvin")
    elif opcion == '3':
        fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
        resultado = fahrenheit_a_celsius(fahrenheit)
        print(f"{fahrenheit} grados Fahrenheit son equivalentes a {resultado} grados Celsius")
    elif opcion == '4':
        fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
        resultado = fahrenheit_a_kelvin(fahrenheit)
        print(f"{fahrenheit} grados Fahrenheit son equivalentes a {resultado} Kelvin")
    elif opcion == '5':
        kelvin = float(input("Ingrese la temperatura en Kelvin: "))
        resultado = kelvin_a_celsius(kelvin)
        print(f"{kelvin} Kelvin son equivalentes a {resultado} grados Celsius")
    elif opcion == '6':
        kelvin = float(input("Ingrese la temperatura en Kelvin: "))
        resultado = kelvin_a_fahrenheit(kelvin)
        print(f"{kelvin} Kelvin son equivalentes a {resultado} grados Fahrenheit")
    elif opcion == '7':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 7.")

