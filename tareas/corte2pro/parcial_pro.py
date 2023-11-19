import pandas as pd
import csv
""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""IMPORTAR ARCHIVOS"""

###IDEAL PARA TABLAS PEQUEÑAS
###Especifica el separador correcto (";")
#df= pd.read_csv("practica.csv")

# ### Visualiza las primeras 6 filas de la tabla
# dfh = df.head(3)
# ###Visualiza las ultimas 6 filas de la tabla
# dft = df.tail(3)
# ###visualiza un rango de filas
# subset1 = df.loc[2:4]

# # print(dfh)
print(df)
# # print(dfh)
# # print(subset1)


################################################################

# import csv
# ###ESTE ES MEJOR PARA DATOS GRANDES
# ###Nombre del archivo CSV (asegúrate de que esté en el mismo directorio que tu script)
# archivo_csv = 'practica.csv'

# ### Abre el archivo CSV y lee los datos
# with open(archivo_csv, mode='r', newline='') as archivo_csv:
#     lector = csv.reader(archivo_csv)

#     ### Itera sobre cada fila en el archivo CSV
#     for fila in lector:
#         ### Imprime cada elemento de la fila, separado por comas
#         print(', '.join(fila))

############################################################

####BUENO PARA TABLAS MEDIANAS

# ### Lista de nombres de archivos CSV,
# ### puedo poner varios['archivo1.csv', 'archivo2.csv', 'archivo3.csv']
# archivos_csv = ['practica.csv']

# for archivo in archivos_csv:
#     ### Carga el archivo CSV en un DataFrame
#     df = pd.read_csv(archivo)
    
#     ### Muestra las primeras 5 filas del DataFrame
#     print(f"Contenido de {archivo}:")
#     print(df.head(20))
#     print("\n")
###########################
### puedo visualizar mejor los datos
datos=open("practica.csv","r+")
for item in datos:
    print(item)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""VISUALIZAR COLUMNAS O FILAS"""

# Obtiene los nombres de las columnas
column_names = df.columns

# Imprime los nombres de las columnas
print(column_names)
########################################################

# ## TAMBIEN ME VOTA EL NOMBRE DE LAS  COLUMNAS


###########################################

###NO ME FUNCIONO
# Supongamos que tienes un DataFrame df
###df = pd.read_csv('tu_archivo.csv')

# # # Muestra la columna "nombre_columna" con su nombre
# nombre_columna="Publicado"
# print(df[nombre_columna].to_string(index=False))
########################################


# # Supongamos que tienes un DataFrame df

# # Accede a la FILA en la posición 1 y obtén sus valores como un arreglo NumPy
# FILA_values = df.iloc[:2].values

# # Imprime los valores de la columna
# print(FILA_values)



################################

# ###NO FUNCIONO SIRVE PARA FILAS 
# # Supongamos que tienes un DataFrame df


# # # Especifica el índice de la columna que deseas ver (por ejemplo, la columna en la posición 1)
# # indice_columna = 12

# # # Obtiene los valores de la columna utilizando el índice
# # columna = df.iloc[: indice_columna]

# # # Imprime los valores de la columna
# # print(columna)


################################################



""""""""""""""""""""""""""""""""""""""""""
"""MANIPULAR COLUMNAS"""

""""""""""""""""""""""""""""""""""""""""""""""""""
"""ELIMINAR COLUMNAS"""
###REMPLAZAR DATOS

# df.fillna(130,inplace=True)


# # datos=open("practica.csv","r+")
# # for item in datos:
# #     print(item)
# print(df)