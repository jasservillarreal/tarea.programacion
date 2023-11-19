import pandas as pd
import numpy as np

# #(data)
# #"uu":6,"dbcs",7

# a=pd.Series({"gbd":7,"hnd":7})
# print(a)




##############################################

# # Crear una Serie de Pandas
# data = [10, 20, 30, 20, 40, 10, 50, 60, 50]
# serie = pd.Series(data)
# print(serie)
# # Calcular la suma de la Serie
# suma = serie.sum()
# print("Suma:", suma)

# # Calcular la media de la Serie
# media = serie.mean()
# print("Media:", media)

# # Encontrar el número que más se repite
# num_mas_comun = serie.mode().values[0]
# print("Número que más se repite:", num_mas_comun)

# # Encontrar el número mayor
# num_mayor = serie.max()
# print("Número mayor:", num_mayor)

# # Encontrar el número menor
# num_menor = serie.min()
# print("Número menor:", num_menor)
#######################################################################################



#Crear un generador de NumPy para generar datos aleatorios
def generar_datos_aleatorios(n):
    for _ in range(n):
        yield np.random.randint(1, 100)

# Generar 10 datos aleatorios
generador = generar_datos_aleatorios(10)

# Crear un DataFrame de Pandas a partir de los datos generados
data = {'Datos Aleatorios': list(generador)}
lola= pd.DataFrame(data)

# Mostrar el DataFrame
print(lola)

##############################################################3
#Crear un generador de NumPy para generar datos aleatorios
def generar_datos_aleatoriosS(n):
    for _ in range(n):
        yield np.random.randint(1, 100)

# Generar 10 datos aleatorios
generadorS = generar_datos_aleatoriosS(10)

# Crear un DataFrame de Pandas a partir de los datos generados
dataS = {'Datos Aleatorios1': list(generadorS)}
lolaS= pd.DataFrame(dataS)

# Mostrar el DataFrame
print(lolaS)


# Unir los DataFrames horizontalmente y obtener uno nuevo
result = pd.concat([lola, lolaS], axis=1)

print(result)


####################

############

# diaz=pd.DataFrame([["maria",3],["jose",
# 30]],columns=["fefke","fk"])
# print(diaz)
#########
# data = {"nombre":["santiago","felipe","lna","valentina"],
#         "porcentaje":[4,2,1,2],
#         "nota":[4,4,3,5]
#         }


#  = pd.DataFrame(data)
# promedio = [['porcentaje','nota']].mean()
# print()
# print(promedio)
###############

##numpy con un dta frame

# data1=np.random.randint(5,size=(4,4))
# data=pd.DataFrame(data1,index=["jasser","felipe","diaz","fraga"],columns=["nota1","nota2","nota3","nota4"])
# promedio=data[['nota1','nota2','nota3','nota4']].mean()
# print(data1)
# print(data)
# print(promedio)


#################################
# # data1=np.random.randint(5,size=(4,4))
# # data=pd.DataFrame(data1,index=['nota1','nota2','nota3','nota4'],columns=["jasser","felipe","diaz","fraga"])
# # promedio=data[["jasser","felipe","diaz","fraga"]].mean()
# # print(data1)
# # print(data)
# # print(promedio)
#############################################################
 ##Crear un DataFrame de ejemplo
data = {'Nombre': ['Juan', 'María', 'Pedro'],
        'Edad': [25, 30, 35],
        'Ciudad': ['Madrid', 'Barcelona', 'Valencia']}
df = pd.DataFrame(data)

# Guardar el DataFrame como un archivo CSV
df.to_csv('archivo.csv', index=False)