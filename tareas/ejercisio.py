
#suma de  2 movimientos armonimath.cos simpples
#()
import math

class movimiento_armonico:

    def __init__ (self, frecuencia, amplitud1, fase1, amplitud2, fase2):
        self.frecuencia=frecuencia
        self.amplitud1=amplitud1
        self.fase1=fase1
        self.amplitud2=amplitud2
        self.fase2=fase2


    def calcular_frecuenciaR(self):
        frecuenciaR=self.frecuencia*1

        return frecuencia
    
    def calcular_amplitudresultante(self):
        amplitud=((self.amplitud1*math.cos(self.fase1)+self.amplitud2*math.cos(self.fase2))**(1/2)+(self.amplitud1*math.sin(self.fase1)+self.amplitud2*math.sin(self.fase2))**(1/2))**(1/2)
        
        return amplitud
    
    def calcular_fase(self):
        fase=math.atan((self.amplitud1*math.cos(self.fase1)+self.amplitud2*math.cos(self.fase2))/(self.amplitud1*math.sin(self.fase1)+self.amplitud2*math.sin(self.fase2)))

        return fase
    
while True:
    
 #datos del primer movimiento armonico

 frecuencia= round(float(input("insrese la frecuencia natural de los dos movimientos armonicos x1(t) y x2(t):")),2)
 amplitud1=  round(float(input("ingrese la amplitud del primer movimiento x1(t):")),2)
 fase1 =  round(float(input("ingrese la fase del primer movimiento x1(t):")),2)

 # dato del segundo movimiento armonico  

 amplitud2=  round(float(input("ingrese la amplitud del segundo movimiento x2(t):")),2)
 fase2= round(float(input("ingrese la fase del segundo movimiento x2(t):")),2)
 
 calculadora =movimiento_armonico(frecuencia,amplitud1,fase1,amplitud2,fase2)

 frecuencia_calculada = calculadora.calcular_frecuenciaR()
 amplitud_calculada = calculadora. calcular_amplitudresultante()
 fase_calculada = calculadora.calcular_fase()


 print(f"la frecuencia angular de los movimientos armonicos es:{frecuencia_calculada}")
 print(f"la amplitud resultante de x(t) = x1(t) y x2(t) : {amplitud_calculada}")
 print(f"Fase resultante de x(t) = x1(t) y x2(t): {fase_calculada}")
 print(f"La solucion  de la superposicion de los 2 movimientos armosnicos es: x(t)=({amplitud_calculada})*sen(({frecuencia_calculada})t+({fase_calculada}))")

 continuar =input("¿Desea sumar otro movimiento armonico? (Si/No): ")
 if continuar.lower() != 'si':
        break  
 
print("Programa terminado.")
 # Salir del bucle si el usuario no quiere continuar