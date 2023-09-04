
#hallar area de un circulo

#import math
#class Circulo:
#    def __init__(self,radio):
 #       self.radio=radio
  #  def calcular_area(self):
   #     area=math.pi*self.radio**2
    #    return area
#radio=float(input("introduzca el radio del circulo:"))
#calculadora=Circulo(radio)
#area_calculada=calculadora.calcular_area()
#print(f"el area del circulo con radio  {radio} es  {area_calculada} unidades cuadradas ")


#calcular mi promedio de notas

class nota_del_semestre:
    def __init__(self,not1,nota2,nota3):
        self.nota1=nota1
        self.nota2=nota2
        self.nota3=nota3
    def promedio_semestre(self):
        promedio=(nota1+nota2+nota3)/3
        return promedio
nota1=float(input("ingrese la primer nota: "))
nota2=float(input("ingrese la segunda nota: "))
nota3=float(input("ingrese la tercera nota: "))
calculadora=nota_del_semestre(nota1,nota2,nota3)
nota_total=calculadora.promedio_semestre()
print(f"el promedio de mi semestre es {nota_total}")

    


   