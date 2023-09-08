""" Jasser Esteban Vilarreal Buitrago"""
# SANTIAGO ECHEVERRI ARTEAGA #
"""PROGRAMACION"""
#Elija tres ejercicios a desarrollar y entreguelos la proxima clase




#3. Escriba un programa que le permita al usuario ingresar
#cualquier cantidad de calificaciones. El usuario indica que ha
#terminado ingresando un número negativo. Se debe imprimir la
#nota más baja, la mas alta y el promedio.


# Inicializamos variables para la nota más alta, la más baja y la suma de las calificaciones

nota_mas_alta = float('-inf')  # Inicializamos con un valor muy pequeño
nota_mas_baja = float('inf')   # Inicializamos con un valor muy grande
suma_calificaciones = 0
contador_calificaciones = 0

while True:


 while True:

    calificacion = float(input("Ingrese una calificación (o un número negativo para terminar): "))
    
    if calificacion < 0:
        # El usuario ingresó un número negativo, terminamos el bucle
        break
    
    # Actualizamos la nota más alta y la más baja
    if calificacion > nota_mas_alta:
        nota_mas_alta = calificacion
    if calificacion < nota_mas_baja:
        nota_mas_baja = calificacion
    
    # Acumulamos la calificación en la suma total
    suma_calificaciones += calificacion
    contador_calificaciones += 1

 if contador_calificaciones > 0:
    # Calculamos el promedio
    promedio = suma_calificaciones / contador_calificaciones
    
    # Mostramos los resultados
    print(f"Nota más alta: {nota_mas_alta}")
    print(f"Nota más baja: {nota_mas_baja}")
    print(f"Promedio: {promedio}")
 else:
    print("No se ingresaron calificaciones.")

 continuar =input("¿Desea ingresar otras notas? (Si/No): ")
 if continuar.lower() != 'si':
 
    break  
  
print("Programa terminado.")