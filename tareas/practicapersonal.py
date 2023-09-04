import math
class Circulo:
    def __init__(self,radio):
        self.radio=radio
    def calcular_area(self):
        area=math.pi*self.radio**2
        return area
radio=float(input("introduzca el radio del circulo:"))
calculadora=Circulo(radio)
area_calculada=calculadora.calcular_area()
print(f"el area del circulo con radio  {radio} es  {area_calculada} unidades cuadradas ")


   