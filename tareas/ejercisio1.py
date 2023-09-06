
#suma de  2 movimientos armonicos simpples

import math

# Ingresa las amplitudes y fases de los dos movimientos armónicos
amplitud1 = float(input("Ingresa la amplitud del primer MAS: "))
fase1 = float(input("Ingresa la fase del primer MAS (en radianes): "))
amplitud2 = float(input("Ingresa la amplitud del segundo MAS: "))
fase2 = float(input("Ingresa la fase del segundo MAS (en radianes): "))

# Calcula la magnitud resultante
magnitud_resultante = math.sqrt(amplitud1**2 + amplitud2**2)

# Calcula el ángulo resultante
angulo_resultante = math.atan2(amplitud2, amplitud1)

# Convierte el ángulo de radianes a grados si lo deseas
angulo_resultante_grados = math.degrees(angulo_resultante)

# Imprime los resultados
print(f"Magnitud resultante: {magnitud_resultante}")
print(f"Ángulo resultante en radianes: {angulo_resultante}")
print(f"Ángulo resultante en grados: {angulo_resultante_grados}")
