import pandas as pd
import csv



# # Nombre del archivo CSV de entrada y salida
# archivo_entrada = 'covid19_clase.csv'
# archivo_salida = 'archivo_salida.csv'

# # Lee las primeras 1000 filas del archivo de entrada
# df = pd.read_csv(archivo_entrada, nrows=1000)

# # Guarda el DataFrame resultante en un nuevo archivo CSV
# df.to_csv(archivo_salida, index=False)

df= pd.read_csv("archivo_salida.csv")

"""1. Realice un programa que importe el archivo compartido “COVID-19_Colombia.csv” y
visualice el encabezado del mismo (primeras cinco columnas)"""



# # Obtener una lista de nombres de columnas y sus posiciones (índices)
# columnas = df.columns

# # Iterar sobre la lista de columnas y sus índices
# for indice, columna in enumerate(columnas):
#     print(f"Columna {indice}: {columna}")


"""2. Identifique los valores repetidos en cada columna y los unifique (Ejemplo: Todos los
valores de Armeniia, ARMENIA y Armenia deben unificarse en ARMENIA)"""


# # # Definir un mapeo para unificar valores en una columna específica
# mapeo_columna = { 'VALLEE': 'VALLE','VALLLE': 'VALLE'}

# # Aplicar el mapeo a una columna específica
# columna_especifica = 'Nombre departamento'  # Reemplaza 'Nombre_Columna' con el nombre de la columna
# df[columna_especifica] = df[columna_especifica].map(mapeo_columna)

# # Repetir estos pasos para cada columna que desees limpiar


"""Cambie las columnas que tienen fechas al formato de pandas datetime y genere para
cada caso nuevas columnas con día, mes y año (Ejemplo: En la columna Fecha de
notificación aparece una fecha 14/3/2020 0:00:00, esta columna debe ser un datetime
correcto y se deben crear tres nuevas columnas en la tabla, una con el dia 14, otra con
el mes 3 y otra con el año 2020)
"""






print(df)











"""5. Elija un departamento y extraiga en vectores de numpy los fallecidos, graves, leves y
moderados por cada ciudad del departamento de su elección"""

# # Definir la columna de interés
# columna_interes = 'Estado'  # Reemplaza 'Nombre_Columna' por el nombre de tu columna

# # Contar la frecuencia de cada valor en la columna
# conteo = df[columna_interes].value_counts()

# # Mostrar el resultado
# print(conteo)

"""7. Exporte una nueva tabla donde solo aparezca la información del departamento seleccionado"""

#print(df)

