class CalculadoraVoltaje:
    def __init__(self, intensidad, resistencia):
        self.intensidad = intensidad
        self.resistencia = resistencia

    def calcular_voltaje(self):
        voltaje = self.intensidad * self.resistencia
        return voltaje

# Pedir al usuario la intensidad y la resistencia
intensidad = float(input("Introduce la intensidad en amperios: "))
resistencia = float(input("Introduce la resistencia en ohmios: "))

# Crear una instancia de la clase CalculadoraVoltaje
calculadora = CalculadoraVoltaje(intensidad, resistencia)

# Calcular y mostrar el voltaje
voltaje_calculado = calculadora.calcular_voltaje()
print(f"El voltaje calculado es {voltaje_calculado} voltios.")
