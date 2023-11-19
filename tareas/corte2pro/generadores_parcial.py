"""En este ejemplo, hemos definido un generador llamado generador_datosque produce números aleatorios y lo hemos
   utilizado para generar datos. Luego, hemos convertido los datos generados en un DataFrame de pandas para realizar
     operaciones de La clave para mezclar generadores con pandas y numpy es asegurar de que los dato"""

# import pandas as pd
# import numpy as np

# # Generador que produce números aleatorios
# def generador_datos(n):
#     for _ in range(n):
#         yield np.random.randint(1, 100)

# # Crear un DataFrame de pandas a partir de los datos generados
# n = 10  # Número de datos a generar
# data_generator = generador_datos(n)
# df = pd.DataFrame({'Datos': list(data_generator)})

# # Realizar operaciones de manipulación de datos con pandas y numpy
# promedio = np.mean(df['Datos'])
# suma = np.sum(df['Datos'])

# # Imprimir los resultados
# print("Datos generados:")
# print(df)
# print(f"Promedio: {promedio}")
# print(f"Suma: {suma}")

"""Ejemplo 1: Generador de Números Primos

En este ejemplo, vamos a generar números."""

# import pandas as pd
# import numpy as np

# # Generador de números primos
# def generador_primos():
#     num = 2
#     while True:
#         es_primo = True
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 es_primo = False
#                 break
#         if es_primo:
#             yield num
#         num += 1

# # Crear un DataFrame de pandas a partir de los primeros 10 números primos
# n = 10
# data_generator = generador_primos()
# primos = [next(data_generator) for _ in range(n)]
# df = pd.DataFrame({'Números Primos': primos})

# # Realizar operaciones con numpy
# suma = np.sum(primos)
# promedio = np.mean(primos)

# # Imprimir resultados
# print("Primeros 10 números primos:")
# print(df)
# print(f"Suma: {suma}")
# print(f"Promedio: {promedio}")


"""Ejemplo 3: Serie de Fibonacci

Generaremos los primeros N términos de la serie de Fibonacci utilizando un generador y luego calcularemos
 algunas estadísticas sobre estos números."""
# import pandas as pd
# import numpy as np

# # Generador de la serie de Fibonacci
# def generador_fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b

# # Crear un DataFrame de pandas con los primeros 10 términos de Fibonacci
# n = 10
# data_generator = generador_fibonacci(n)
# fibonacci = [next(data_generator) for _ in range(n)]
# df = pd.DataFrame({'Fibonacci': fibonacci})

# # Calcular la suma y el promedio con numpy
# suma = np.sum(fibonacci)
# promedio = np.mean(fibonacci)

# # Imprimir resultados
# print("Primeros 10 términos de la serie de Fibonacci:")
# print(df)
# print(f"Suma: {suma}")
# print(f"Promedio: {promedio}")


"""Ejemplo 4: Sumatoria de una Serie Numérica
En este ejemplo, generaremos los primeros N términos de una serie numérica y luego
 calcularemos su suma."""

# import pandas as pd
# import numpy as np

# # Generador de una serie numérica (por ejemplo, serie aritmética)
# def generador_serie(n):
#     for i in range(1, n + 1):
#         yield i

# # Crear un DataFrame de pandas con los primeros 10 términos de la serie
# n = 10
# data_generator = generador_serie(n)
# serie = [next(data_generator) for _ in range(n)]
# df = pd.DataFrame({'Serie Numérica': serie})

# # Calcular la suma con numpy
# suma = np.sum(serie)

# # Imprimir resultados
# print("Primeros 10 términos de la serie numérica:")
# print(df)
# print(f"Suma: {suma}")


"""Ejemplo 5: Generador de Secuencia de Cuadrados Perfectos
Generaremos una secuencia de cuadrados perfectos utilizando un generador y luego calcularemos algunas
 estadísticas sobre estos números."""

# import pandas as pd
# import numpy as np

# # Generador de cuadrados perfectos
# def generador_cuadrados_perfectos(n):
#     for i in range(1, n + 1):
#         yield i**2

# # Crear un DataFrame de pandas con los primeros 10 cuadrados perfectos
# n = 10
# data_generator = generador_cuadrados_perfectos(n)
# cuadrados_perfectos = [next(data_generator) for _ in range(n)]
# df = pd.DataFrame({'Cuadrados Perfectos': cuadrados_perfectos})

# # Calcular la suma, el promedio y la desviación estándar con numpy
# suma = np.sum(cuadrados_perfectos)
# promedio = np.mean(cuadrados_perfectos)
# desviacion_estandar = np.std(cuadrados_perfectos)

# # Imprimir resultados
# print("Primeros 10 cuadrados perfectos:")
# print(df)
# print(f"Suma: {suma}")
# print(f"Promedio: {promedio}")
# print(f"Desviación Estándar: {desviacion_estandar}")


"""Ejemplo 6: Generador de Secuencia de Números Primos Gemelos
Generaremos una secuencia de números primos gemelos utilizando un generador y luego analizaremos
 las diferencias entre estos números."""

# import pandas as pd
# import numpy as np

# # Generador de números primos gemelos
# def generador_primos_gemelos(n):
#     p = 3
#     while n > 0:
#         if all(p % i != 0 for i in range(2, int(p**0.5) + 1)):
#             if all((p + 2) % i != 0 for i in range(2, int((p + 2)**0.5) + 1)):
#                 yield p, p + 2
#                 n -= 1
#         p += 2

# # Crear un DataFrame de pandas con los primeros 5 pares de primos gemelos
# n = 5
# data_generator = generador_primos_gemelos(n)
# primos_gemelos = list(data_generator)
# df = pd.DataFrame({'Primos Gemelos': primos_gemelos})

# # Calcular las diferencias entre los números gemelos con numpy
# diferencias = [p2 - p1 for p1, p2 in primos_gemelos]

# # Imprimir resultados
# print("Primeros 5 pares de números primos gemelos:")
# print(df)
# print("Diferencias entre los números gemelos:")
# print(diferencias)
