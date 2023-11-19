"""jasser estenan villarreal buitrago"""

import  pandas as pd
import numpy as np
import csv


df= pd.read_csv("Materiales.csv")

"""1. (0.5 Puntos) Dado el DataFrame df que contiene datos sobre conductores
y materiales, escribe c´odigo en Pandas para eliminar todas las filas con
valores nulos en la columna “Longitud”."""

# df = df.drop(df[df['Longitud']==""].index)

# print(df)

import pandas as pd

# Carga el archivo CSV en un DataFrame
df = pd.read_csv('tu_archivo.csv')

# Utiliza el método dropna para eliminar las filas con valores nulos en la columna "Longitud"
df = df.dropna(subset=['Longitud'])

# Ahora puedes guardar el DataFrame resultante de nuevo en un archivo CSV si lo deseas
df.to_csv('archivo_sin_nulos.csv', index=False)


"""2. (0.5 Puntos) Utiliza Pandas para calcular el promedio, valor m´aximo,
valor m´ınimo y desviaci´on est´andar de cada columna en el DataFrame df
y redondea el resultado a 2 decimales."""

# df_info = df.describe()

# print(df_info)

"""3. (1.0 Punto) Supongamos que deseas unificar las categor´ıas similares en la
columna ”Tipo de Conductor”. Escribe c´odigo en Pandas para unificar las
categor´ıas en ”CONDUCTOR”, ”AISLANTE” y ”SEMICONDUCTOR”."""

# # # Definir la columna de interés
# # columna_interes = 'Tipo de Conductor'  # Reemplaza 'Nombre_Columna' por el nombre de tu columna

# # # Contar la frecuencia de cada valor en la columna
# # conteo = df[columna_interes].value_counts()

# # # Mostrar el resultado
# # print(conteo)


# #
# mapeo_columna = { 'aislante': 'Aislante','Aislante': 'Aislante','Conductor': 'Conductor',
#                  'conductor': 'Conductor','condctor': 'Conductor','semiconductor': 'Semiconductor',
#                  'SEMICONDUCTOR': 'Semiconductor','semi': 'Semiconductor','semicondugctor': 'Semiconductor',
#                  'AISLANTE': 'Aislante','aislamte': 'Aislante','Aislado': 'Aislante','CONDUCTOR': 'Conductor'}

# # Aplicar el mapeo a una columna específica
# columna_especifica = 'Tipo de Conductor'  # Reemplaza 'Nombre_Columna' con el nombre de la columna
# df[columna_especifica] = df[columna_especifica].map(mapeo_columna)

# # Repetir estos pasos para cada columna que desees limpiar
# print(df)


"""4. (0.5 Puntos) Utiliza NumPy para calcular el producto escalar entre los
arreglos resistencias y di´ametros. Luego, redondea el resultado a 2
decimales.
"""
# Producto_escalar= df['Diametro'] * df['Resistencia']
# print(Producto_escalar)

"""5. (0.5 Puntos) Genera una columna adicional con la corriente asumiendo los
materiale Ohmnicos.
"""
#df['CORRIENTE'] = df['Voltaje'] / df['Resistencia']

# print(df)


"""6. (1.0 Punto) Genera un dataframe en un contexto de la f´ısica con al menos
una columna categ´orica y 4 num´ericas con datos aleatorios pero generados
de forma diferente dependiendo de la categor´ıa. Guardala como archivo
csv."""

data_N=np.random.randint(10,size=(5,5))
data1=pd.DataFrame(data_N,index=["HIERRO","PLATA","ORO","COBRE","MADERA"],
                  columns=["Conductividad","resistencia","humedad","dureza","toxico"])

l=["ALTO","BAJO","BAJO","MEDIO","ALTO"]
data2=pd.DataFrame(l, columns=["RIESGO"])
print(data1)
print(data2)

RESUL=pd.concat([data2,data1], axis=1)
print(RESUL)
RESUL.to_csv('datos_actualizados.csv', index=False)

"""7. (0.5 Puntos) Genera una matriz cuadrada A de dimensi´on mayor o igual
a 100 × 100 y un vector b de dimensi´on 100 Soluciona el sistema Ax = b,
encuentra la inversa (si existe) de A, su determinante, valores propios y
vectores propios.
"""
# data1=np.random.randint(5,size=(100,100))
# data=np.random.randint(5,size=(100,1))

#lo=numpy.linalg.det(array)
#print(f"el determinante es: {lo}"")

#print(data1)
#print(data)
