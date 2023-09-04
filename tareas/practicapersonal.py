
#hallar area de un circulo
"""""
import math
class Circulo:
    def __init__(self,radio):
        self.radio=radio
    def calcular_area(self):
        area=math.pi*self.radio**2
        return area
radio=float(input("introduzca el radio del circulo:"))
calculadora=Circulo(radio)
area_calculada=calculadora.calcular_area()
print(f"el area del circulo con radio  {radio} es  {area_calculada} unidades cuadradas ")
"""""

#calcular mi promedio de notas

""""
class nota_del_semestre:
    def __init__(self,not1,nota2,nota3):
        self.nota1=nota1
        self.nota2=nota2
        self.nota3=nota3
    def promedio_semestre(self):
        promedio=(nota1+nota2+nota3)/3
        return promedio
nota1=float(input("ingrese la primer nota: "))
nota2=float(input("ingrese la segunda nota: "))
nota3=float(input("ingrese la tercera nota: "))
calculadora=nota_del_semestre(nota1,nota2,nota3)
nota_total=calculadora.promedio_semestre()
print(f"el promedio de mi semestre es {nota_total}")

"""

# ejemplo de código orientado a objetos en Python que utiliza condicionales y métodos mágicos, y contiene un ciclo for y un ciclo while


class Vehiculo:
     def __init__(self,marca,modelo,año):
        self.marca=marca
        self.modelo=modelo
        self.año=año
        self.encendido=False
     def __str__(self):
        return f"{self.año}{self.marca}{self.modelo}"
     def encender(self):
        if not self.encendido:
            self.encendido=True
            print(f"{self} ha sido encendido.")
        else:
            print(f"{self} ya está encendido.")
     def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"{self} ha sido apagado.")
        else:
            print(f"{self} ya está apagado.")

# Crear una lista de vehículos

vehiculos = [
    Vehiculo("Toyota", "Camry", 2022),
    Vehiculo("Honda", "Civic", 2023),
    Vehiculo("Ford", "Fiesta", 2021)]

# Usar un ciclo for para mostrar información de los vehículos

print("Lista de vehículos:")
for vehiculo in vehiculos:
    print(vehiculo)

# Usar un ciclo while para permitir al usuario encender o apagar vehículos
while True:
    print("\n¿Qué vehículo deseas encender o apagar? (e para salir)")
    opcion = input("Marca del vehículo: ")

    if opcion.lower() == 'e':
        break

    encontrado = False
    for vehiculo in vehiculos:
        if vehiculo.marca.lower() == opcion.lower():
            encontrado = True
            accion = input(f"¿Deseas encender o apagar {vehiculo}? (encender/apagar): ")

            if accion.lower() == 'encender':
                vehiculo.encender()
            elif accion.lower() == 'apagar':
                vehiculo.apagar()
            else:
                print("Acción no válida. Usar 'encender' o 'apagar'.")

    if not encontrado:
        print("Vehículo no encontrado en la lista.")

print("Programa terminado.")