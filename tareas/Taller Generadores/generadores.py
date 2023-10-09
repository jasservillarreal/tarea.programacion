"""   Taller: Generadores y gestión de datos   """

#JASSER ESTEBAN VILLARREAL BUITRAGO



""""
1. Generadores y Comprensión de Generadores:

Escribe un generador que produzca la serie de Fibonacci hasta un valor dado n. Luego,
utiliza una comprensión de generadores para obtener todos los números pares en la
serie hasta ese valor.
"""

# def fibonacci_generator(n):
#     a, b = 0, 1
#     while a <= n:
#         yield a
#         a, b = b, a + b

# def even_fibonacci_generator(n):
#     return (x for x in fibonacci_generator(n) if x % 2 == 0)

# n = int(input("Ingrese un valor para n: "))

# print("Serie de Fibonacci hasta", n, ":")
# for num in fibonacci_generator(n):
#     print(num, end=" ")

# print("\nNúmeros pares en la serie de Fibonacci hasta", n, ":")
# for even_num in even_fibonacci_generator(n):
#     print(even_num, end=" ")


"""
2. Manejo de Archivos y Datos:

Dado un archivo CSV que contiene información sobre estudiantes (nombre, edad, calificaciones), escribe un programa que lea el archivo y calcule el promedio de edad de los
estudiantes, promedio de notas y seleccione los que perdieron la asignatura y los que
están entre el 10 % mejor.
"""

# import csv

# # Función para calcular el promedio de una lista de números
# def calcular_promedio(lista):
#     if len(lista) == 0:
#         return 0
#     return sum(lista) / len(lista)

# # Nombre del archivo CSV
# archivo_csv = 'estudiantes.csv'

# # Listas para almacenar datos
# nombres = []
# edades = []
# calificaciones = []

# # Leer el archivo CSV
# try:
#     with open(archivo_csv, 'r', newline='') as archivo:
#         lector_csv = csv.DictReader(archivo)
#         for fila in lector_csv:
#             nombres.append(fila['nombre'])
#             edades.append(int(fila['edad']))
#             calificaciones.append(float(fila['calificaciones']))
# except FileNotFoundError:
#     print(f"El archivo {archivo_csv} no se encontró. Verifica la ruta o nombre del archivo.")
#     exit(1)

# # Calcular promedio de edad y promedio de calificaciones
# promedio_edad = calcular_promedio(edades)
# promedio_calificaciones = calcular_promedio(calificaciones)

# print(f"Promedio de Edad de los estudiantes: {promedio_edad:.2f}")
# print(f"Promedio de Calificaciones de los estudiantes: {promedio_calificaciones:.2f}")

# # Estudiantes que perdieron la asignatura (calificación < 5)
# perdieron_asignatura = [nombre for nombre, calificacion in zip(nombres, calificaciones) if calificacion < 5]
# if perdieron_asignatura:
#     print("Estudiantes que perdieron la asignatura:")
#     for estudiante in perdieron_asignatura:
#         print(estudiante)

# # Estudiantes en el 10 % mejor (calificación >= 90)
# limite_superior = sorted(calificaciones, reverse=True)[len(calificaciones) // 10]
# mejores_estudiantes = [nombre for nombre, calificacion in zip(nombres, calificaciones) if calificacion >= limite_superior]
# if mejores_estudiantes:
#     print("Estudiantes en el 10 % mejor:")
#     for estudiante in mejores_estudiantes:
#         print(estudiante)

"""
3. Manipulación de Datos con Pandas:

Busca a importa el conjunto de datos de Titanic. Luego, calcula la cantidad de pasajeros
que sobrevivieron y la cantidad que no sobrevivieron.
"""

# import pandas as pd

# # Carga el conjunto de datos de Titanic desde un archivo CSV
# archivo_csv = 'titanic.csv'  # Reemplaza con la ruta de tu archivo CSV
# df = pd.read_csv(archivo_csv)

# # Calcula la cantidad de pasajeros que sobrevivieron y que no sobrevivieron
# sobrevivieron = df[df['Survived'] == 1]
# no_sobrevivieron = df[df['Survived'] == 0]

# cantidad_sobrevivieron = len(sobrevivieron)
# cantidad_no_sobrevivieron = len(no_sobrevivieron)

# print(f"Cantidad de pasajeros que sobrevivieron: {cantidad_sobrevivieron}")
# print(f"Cantidad de pasajeros que no sobrevivieron: {cantidad_no_sobrevivieron}")



""""
4. Exportación de Datos:

Escribe un programa que genere una lista de diccionarios, donde cada diccionario representa un empleado con información como nombre, salario y departamento. Luego,
exporta estos datos a un archivo JSON.
"""
# import json

# # Crear una lista de diccionarios con información de empleados
# empleados = [
#     {"nombre": "Empleado1", "salario": 50000, "departamento": "Ventas"},
#     {"nombre": "Empleado2", "salario": 60000, "departamento": "Tecnología"},
#     {"nombre": "Empleado3", "salario": 55000, "departamento": "Recursos Humanos"},
#     {"nombre": "Empleado4", "salario": 70000, "departamento": "Ventas"},
#     {"nombre": "Empleado5", "salario": 65000, "departamento": "Tecnología"}
# ]

# # Nombre del archivo JSON de destino
# archivo_json = 'empleados.json'

# # Exportar la lista de empleados a un archivo JSON
# with open(archivo_json, 'w') as archivo:
#     json.dump(empleados, archivo, indent=4)

# print(f"Los datos de empleados han sido exportados a {archivo_json}.")

"""
5. Manipulación de Datos Numéricos:

Lee un archivo de texto con una lista de números separados por comas. Escribe un
generador que lea estos números y produzca su suma acumulativa. Sin usar librerías.
"""

# def suma_acumulativa_generador(archivo):
#     suma = 0
#     with open(archivo, 'r') as f:
#         for linea in f:
#             numeros = linea.strip().split(',')
#             for numero in numeros:
#                 try:
#                     valor = float(numero)
#                     suma += valor
#                     yield suma
#                 except ValueError:
#                     continue

# archivo = 'numeros.txt'

# print("Suma acumulativa de números:")
# for suma_acumulativa in suma_acumulativa_generador(archivo):
#     print(suma_acumulativa)


"""
6. Comprensión de Listas y Generadores:

Escribe una función que tome una lista de palabras como entrada y devuelva un generador que produzca solo las palabras que tienen más de 5 letras.

"""

# def palabras_mas_de_5_letras(lista_palabras):
#     return (palabra for palabra in lista_palabras if len(palabra) > 5)

# # Ejemplo de uso
# lista_de_palabras = ["manzana", "pera", "banana", "uva", "sandía", "fresa", "kiwi"]
# generador = palabras_mas_de_5_letras(lista_de_palabras)

# for palabra in generador:
#     print(palabra)

"""
7. Procesamiento de Texto:

Escribe una clase que reciba la ruta de un archivo (debe ser un texto extenso dividido
en párrafos), lea el archivo de texto. Tenga un método que genere una lista de tuplas
con cada párrafo y su longitud. Otro método que reciba un número N y retorne los N
párrafos más largos. Sin usar librerías
"""
# class ProcesadorTexto:
#     def __init__(self, ruta_archivo):
#         self.ruta_archivo = ruta_archivo
#         self.parrafos = []

#     def leer_archivo(self):
#         try:
#             with open(self.ruta_archivo, 'r') as archivo:
#                 texto = archivo.read()
#                 self.parrafos = [parrafo.strip() for parrafo in texto.split('\n\n')]
#         except FileNotFoundError:
#             print(f"El archivo {self.ruta_archivo} no se encontró.")

#     def generar_lista_tuplas(self):
#         lista_tuplas = [(parrafo, len(parrafo)) for parrafo in self.parrafos]
#         return lista_tuplas

#     def parrafos_mas_largos(self, N):
#         lista_tuplas = self.generar_lista_tuplas()
#         lista_tuplas_ordenadas = sorted(lista_tuplas, key=lambda x: x[1], reverse=True)
#         return lista_tuplas_ordenadas[:N]

# # Ejemplo de uso
# if __name__ == "__main__":
#     procesador = ProcesadorTexto('archivo.txt')  # Reemplaza 'archivo.txt' con la ruta de tu archivo de texto

#     procesador.leer_archivo()

#     lista_tuplas = procesador.generar_lista_tuplas()
#     print("Lista de tuplas (párrafo, longitud):")
#     for tupla in lista_tuplas:
#         print(tupla)

#     N = 3  # Cambia N según la cantidad de párrafos más largos que desees obtener
#     parrafos_mas_largos = procesador.parrafos_mas_largos(N)
#     print(f"\nLos {N} párrafos más largos:")
#     for i, (parrafo, longitud) in enumerate(parrafos_mas_largos, start=1):
#         print(f"Párrafo {i}:")
#         print(parrafo)
#         print(f"Longitud: {longitud} caracteres\n")

"""
9. Manipulación de Datos JSON:

Lee un archivo JSON que contiene información sobre productos (nombre, precio, cantidad en stock). Escribe un generador que produzca solo los productos que tienen un
precio superior a cierto umbral.
"""

# import json

# def productos_con_precio_superior(archivo_json, umbral):
#     with open(archivo_json, 'r') as archivo:
#         productos = json.load(archivo)
#         for producto in productos:
#             if producto['precio'] > umbral:
#                 yield producto

# archivo_json = 'productos.json'  # Reemplaza con la ruta de tu archivo JSON
# umbral = 10.0  # Define el umbral de precio

# print(f"Productos con precio superior a {umbral}:")
# for producto in productos_con_precio_superior(archivo_json, umbral):
#     print(producto)
