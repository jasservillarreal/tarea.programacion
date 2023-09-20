
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
"""

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
#Ejemplo de código orientado a objetos en Python que utiliza condicionales y métodos mágicos,
#  y contiene un ciclo for y un ciclo while


# class Vehiculo:
#      def __init__(self,marca,modelo,año):
#         self.marca=marca
#         self.modelo=modelo
#         self.año=año
#         self.encendido=False
#      def __str__(self):
#         return f"{self.año}{self.marca}{self.modelo}"
#      def encender(self):
#         if not self.encendido:
#             self.encendido=True
#             print(f"{self} ha sido encendido.")
#         else:
#             print(f"{self} ya está encendido.")
#      def apagar(self):
#         if self.encendido:
#             self.encendido = False
#             print(f"{self} ha sido apagado.")
#         else:
#             print(f"{self} ya está apagado.")

# # Crear una lista de vehículos

# vehiculos = [
#     Vehiculo("Toyota", "Camry", 2022),
#     Vehiculo("Honda", "Civic", 2023),
#     Vehiculo("Ford", "Fiesta", 2021)]

# # Usar un ciclo for para mostrar información de los vehículos

# print("Lista de vehículos:")
# for vehiculo in vehiculos:
#     print(vehiculo)

# # Usar un ciclo while para permitir al usuario encender o apagar vehículos
# while True:
#     print("\n¿Qué vehículo deseas encender o apagar? (e para salir)")
#     opcion = input("Marca del vehículo: ")

#     if opcion.lower() == 'e':
#         break

#     encontrado = False
#     for vehiculo in vehiculos:
#         if vehiculo.marca.lower() == opcion.lower():
#             encontrado = True
#             accion = input(f"¿Deseas encender o apagar {vehiculo}? (encender/apagar): ")

#             if accion.lower() == 'encender':
#                 vehiculo.encender()
#             elif accion.lower() == 'apagar':
#                 vehiculo.apagar()
#             else:
#                 print("Acción no válida. Usar 'encender' o 'apagar'.")

#     if not encontrado:
#         print("Vehículo no encontrado en la lista.")

# print("Programa terminado.")


# rectangulo

""""

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        area_rectangulo=self.base * self.altura
        return area_rectangulo

    def perimetro(self):
       perimetro_rectangulo=2 * (self.base + self.altura)
       return perimetro_rectangulo
base = float(input("Introduce la base en metros: "))
altura = float(input("Introduce la altura en metros: "))
    
# Crear una instancia de la clase Rectangulo

mi_rectangulo = Rectangulo(base,altura)

# Calcular el área y el perímetro

area = mi_rectangulo.area()
perimetro = mi_rectangulo.perimetro()

# Imprimir los resultados
print(f"El área del rectángulo es: {area} metros cuadrados")
print(f"El perímetro del rectángulo es: {perimetro} metros")

"""

# Usando un bucle for para imprimir números del 1 al 5


"""
print(f"Usando un bucle for:")
for i in range(1, 6):
    print(i)

# Usando un bucle while para imprimir números del 1 al 5

print("Usando un bucle while:")
contador = 1
while contador <= 12:
    print(contador)
    contador += 2
    
"""
"""
#lamda factorial
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

# Ejemplo de uso
numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")


factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
numeros = [5, 4, 3, 2, 1]
resultados = [factorial(numero) for numero in numeros]
print(resultados)
"""
# prime = lambda f: lambda x: x * f(f)(x - 1) if x > 0 else 1
# factorial = prime(prime)

# # Ejemplo de uso
# numero = 5
# resultado = factorial(numero)
# print(f"El factorial de {numero} es {resultado}")

# multiplicacion=eval(input("ingrese numero que quiere multiplicar por 5 :  "))
# print("su miltiplicacion es ",5*multiplicacion)
#a=int(input("ingresela base: "))
# b=int(input("ingresela esponenre: "))
# def suma(b):
#     if b==0:
#         return 1
    
    
   
#     else:
#         return b*suma(b-1)
# solucion=suma(b)
# print(f"{solucion}")

# class Estudiante:
#     def __init__(self, nombre, edad, nota):
#         self.nombre = nombre
#         self.edad = edad
#         self.nota = nota
# while True:
 
#  estudiantes = [Estudiante("Juan", 18, 90), Estudiante("Maria", 20, 85), Estudiante("Carlos", 19, 92)]
#  print(estudiantes)

#  nombre=str(input("ingrese nombre:"))
#  edad=str(input("ingrese edad:"))
#  nota=str(input("ingrese nota:"))
#  nuevo_estudiante=Estudiante(nombre,edad,nota)
#  estudiantes.append(nuevo_estudiante)
#  for estudiante in estudiantes:
#     print(f"Nombre: {estudiante.nombre}, Edad: {estudiante.edad}, Nota: {estudiante.nota}")
#  continuar=input("ingrese si  o no continuar")
 
#  if continuar.lower() != 'si':
#     break  

# class Estudiante:
#     def __str__(self, nombre, edad, nota):
#         self.nombre = nombre
#         self.edad = edad
#         self.nota = nota

# estudiantes = [Estudiante("Juan", 18, 90), Estudiante("Maria", 20, 85), Estudiante("Carlos", 19, 92)]

# while True:
#     print(estudiantes)
    
#     nombre = input("Ingrese nombre: ")
#     edad = str(input("Ingrese edad: "))  # Convierte la entrada a entero
#     nota = str(input("Ingrese nota: "))  # Convierte la entrada a flotante
    
#     nuevo_estudiante = Estudiante(nombre, edad, nota)
#     estudiantes.append(nuevo_estudiante)
    
#     for estudiante in estudiantes:
#         print(f"Nombre: {estudiante.nombre}, Edad: {estudiante.edad}, Nota: {estudiante.nota}")
    
#     continuar = input("Ingrese 'si' para continuar o cualquier otra cosa para salir: ")
    
#     if continuar.lower() != 'si':
#         break

# Evalúa una expresión matemática.
resultado = eval(input("ingrese:  "))
print(2*resultado)  # Esto imprimirá 14
