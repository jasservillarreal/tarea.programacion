import pandas as pd
import numpy as np
#()
import csv

# # tabla1=pd.read_csv("estudiante.csv")
# # tabla=tabla1.head(6)
# # print(tabla)
# # #################
with open('estudiante.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')

    for row in csv_reader:
        print(row)
# # ####################

# # import csv

# # # Nombre del archivo CSV (asegúrate de que esté en el mismo directorio que tu script)
# # archivo_csv = 'estudiante.csv'

# # # Abre el archivo CSV y lee los datos
# # with open(archivo_csv, mode='r', newline='') as archivo_csv:
# #     lector = csv.reader(archivo_csv)

# #     # Itera sobre cada fila en el archivo CSV
# #     for fila in lector:
# #         # Imprime cada elemento de la fila, separado por comas
# #         print(', '.join(fila))
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""



# # # Especifica el separador correcto (";")
# # tabla1 = pd.read_csv("estudiante.csv", delimiter=";")

# # # Visualiza las primeras 6 filas de la tabla
# # tabla = tabla1.head(6)
# # print(tabla)

# # # Calcula el promedio de las columnas "nota1", "nota2", "nota3", "nota4", "nota5"
# # promedio = tabla1[['nota1', 'nota 2', 'nota 3', ]].mean(axis=1)
# # suma = tabla1[['nota1', 'nota 2', 'nota 3', 'nota 4', 'nota 5']].sum()
# # mediana = tabla1[['nota1', 'nota 2', 'nota 3', 'nota 4', 'nota 5']].median()
# # desviacion = tabla1[['nota1', 'nota 2', 'nota 3', 'nota 4', 'nota 5']].std()


# # # Muestra el promedio
# # print("promedio de las notas:")
# # print(promedio)

# # print("suma de las notas:")
# # print(suma)

# # print("media de las notas:")
# # print(mediana)

# # print("desviacion estandar:")
# # print(desviacion)
# """"""""""""""""""""""""""""""""""""
# # # Ejemplo de un generador simple que produce números pares infinitamente
# # def generador_de_pares():
# #     num = 0
# #     while True:
# #         yield num
# #         num += 2

# # # Crear una instancia del generador
# # generador = generador_de_pares()

# # # Utilizar el generador para obtener valores
# # for i in range(5):
# #     print(next(generador))  # Imprime los primeros 5 números pares

# # # El generador puede generar números infinitamente
# # # Puedes detenerlo manualmente o utilizar condicionales en tu código para limitar la generación.
# """"""""""""""""""""""""""""""""""""""""""


# def generador_taylor(funcion, x, n_terminos, **kwargs):
#     """
#     Generador que calcula términos de la serie de Taylor para una función dada.

#     Args:
#     funcion (callable): La función matemática para la cual se calcula la serie de Taylor.
#     x (float): El valor en el que se quiere evaluar la serie de Taylor.
#     n_terminos (int): El número de términos de la serie a calcular.
#     **kwargs: Parámetros adicionales para la función.

#     Yields:
#     float: Términos de la serie de Taylor.
#     """
#     resultado = funcion(x, **kwargs)  # Término inicial (n = 0)
#     yield resultado

#     for n in range(1, n_terminos):
#         derivada_n = calcular_derivada_n(funcion, x, n, **kwargs)
#         termino_n = (derivada_n /factorial(n)) * (x ** n)
#         resultado += termino_n
#         yield resultado

# def calcular_derivada_n(funcion, x, n, h=1e-5, **kwargs):
#     """
#     Función para calcular la n-ésima derivada de una función utilizando aproximación numérica.

#     Args:
#     funcion (callable): La función matemática para la cual se calcula la derivada.
#     x (float): El valor en el que se evalúa la derivada.
#     n (int): Orden de la derivada.
#     h (float): Tamaño del incremento para la aproximación numérica.
#     **kwargs: Parámetros adicionales para la función.

#     Returns:
#     float: Valor de la n-ésima derivada.
#     """
#     h_power_n = h ** n
#     suma = 0
#     for k in range(n + 1):
#         coeficiente = (-1) ** k * factorial(n) / (factorial(k) * factorial(n - k))
#         suma += coeficiente * funcion(x + k * h, **kwargs)
#     return suma / h_power_n

# # Ejemplo de uso
# import math  # Función matemática

# x = 2.0  # Valor en el que se evaluará la serie de Taylor
# n_terminos = 5  # Número de términos de la serie a calcular

# taylor_generator = generador_taylor(math.exp, x, n_terminos)

# for i, termino in enumerate(taylor_generator):
#     print(f"Término {i}: {termino}")
