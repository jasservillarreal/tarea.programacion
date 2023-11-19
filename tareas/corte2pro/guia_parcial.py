import pandas as pd
import numpy as np
#()
import csv
"""importar archivo"""

#################################################################

#es bueno para tablas pequeñas
# Especifica el separador correcto (";")
tabla = pd.read_csv("estudiante.csv", delimiter=";")
df=pd.DataFrame(tabla)
# # Visualiza las primeras 6 filas de la tabla
# tablah = tabla.head(3)
# # #Visualiza las ultimas 6 filas de la tabla
# # tablat = tabla.tail(3)
# # #visualiza un rango de filas
# # subset1 = tabla.loc[2:4]
df.fillna(130,inplace=True)#remplaza toda las celdas vacias
# # print(subset1)
print(df)
# #print(tablah)
# #print(tablat)



###############################################

# import csv
# #este es mejor para datos grandes
# # Nombre del archivo CSV (asegúrate de que esté en el mismo directorio que tu script)
# archivo_csv = 'practica.csv'

# # Abre el archivo CSV y lee los datos
# with open(archivo_csv, mode='r', newline='') as archivo_csv:
#     lector = csv.reader(archivo_csv)

#     # Itera sobre cada fila en el archivo CSV
#     for fila in lector:
#         # Imprime cada elemento de la fila, separado por comas
#         print(', '.join(fila))

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# # Supongamos que deseas acceder a las filas 5 a 10 y las columnas 'columna1' y 'columna2'
# subset = tabla.loc[2:4, ['nota1', 'nota 2']]
# print(subset)

# # Supongamos que deseas acceder a las filas 5 a 10 y las columnas 'columna1' y 'columna2'
# subset1 = tabla.loc[2:3]
# print(subset1)

""""""""""""""""""""""""""""""""""""""""""""""""""
# # # # #Cambiar los valores en las filas 2 'columna1' a 00, respectivamente
# df.loc[2,'nota1'] = [300]
# # print(tabla)
# # Cambiar los valores en las filas 3 y 4 de 'columna2' a 200 y 300, respectivamente
# df.loc[2:3,'nota1',"nota2"] = [23,33]




# # # Imprimir la tabla actualizada
# # print(tabla)


# # Reemplazar la columna 'columna3' con una nueva serie de datos
# nueva_serie = [1, 2, 3, 4, 5,4,4,4]
# df['nota1'] = nueva_serie

# print(df)
""""""""""""""""""""""""""""""""""""""""""""""""""""""
# import pandas as pd

# # Lee el archivo CSV y carga los datos en un DataFrame
#  = pd.read_csv('practica.csv')

# # Obtiene los nombres de las columnas
# column_names = .columns

# # Imprime los nombres de las columnas
# print(column_names)

# # Muestra las filas del índice 0 al 4
# print([0:5])

""""""""""""""""""""""""""""""""""""""""""""

mi_lista = [4] * 10
print(mi_lista)