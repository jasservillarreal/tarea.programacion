""" Jasser Esteban Vilarreal Buitrago"""
# SANTIAGO ECHEVERRI ARTEAGA #
"""PROGRAMACION"""
#Elija tres ejercicios a desarrollar y entreguelos la proxima clase

"""
2. Hay un antiguo método para calcular (aproximar) la raiz
cuadrada de un número dado x. Se parte de una conjetura a y se
calcula a+ x
a
2
. Este resultado es la primera aproximación, pero el
resultado se puede refinar aún más tomando como ansatz este
resultado y repitiendo el procedimiento las veces que sea.
Realice un programa que calcule la raíz cuadrada de un número
dado y lo haga con la precisión que desee el usuario. No puede
hacer uso de la librería math.
"""
while True:

 def aproximacion_raiz_cuadrada(numero, precision=0.0001, max_iteraciones=100):
    # Inicializamos la conjetura inicial a la mitad del número
    conjetura = numero / 2.0
  

    
    for _ in range(max_iteraciones):
        # Calculamos una nueva aproximación usando el método mencionado
        nueva_conjetura = 0.5 * (conjetura + (numero / conjetura))
        
        # Verificamos si la diferencia entre la nueva y la anterior conjetura es menor que la precisión deseada
        if abs(nueva_conjetura - conjetura) < precision:
            return nueva_conjetura
        
        conjetura = nueva_conjetura
    
    # Si no se alcanza la precisión deseada en el número máximo de iteraciones
    return conjetura

# Solicitamos al usuario ingresar el número del cual desea calcular la raíz cuadrada
 numero = float(input("Ingrese un número para calcular su raíz cuadrada: "))

# Solicitamos la precisión deseada al usuario
 precision = float(input("Ingrese la precisión deseada (por ejemplo, 0.0001): "))

# Calculamos la raíz cuadrada con la precisión deseada
 resultado = aproximacion_raiz_cuadrada(numero, precision)

# Mostramos el resultado
 print(f"La raíz cuadrada de {numero} es aproximadamente {resultado} con una precisión de {precision}")


 continuar =input("¿Desea ingresar otras raiz? (Si/No): ")
 if continuar.lower() != 'si':
 
    break  
  
print("Programa terminado.")