
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
    
 #datos del primer movimiento armonico

frecuencia= float(input("insrese la frecuencia natural de los dos movimientos armonicos:"))
amplitud1=  float(input("ingrese la amplitud del primer movimiento:"))
fase1 =  float(input("ingrese la fase del primer movimiento:"))

 # dato del segundo movimiento armonico  

amplitud2=  float(input("ingrese la amplitud del segundo movimiento:"))
fase2= float(input("ingrese la fase del segundo movimiento:"))
 
calculadora =movimiento_armonico(frecuencia,amplitud1,fase1,amplitud2,fase2)

frecuencia_calculada = calculadora.calcular_frecuenciaR()
amplitud_calculada = calculadora. calcular_amplitudresultante()
fase_calculada = calculadora.calcular_fase()


print(f"la frecuencia de los movimientos es:{frecuencia_calculada}")
print(f"amplitud resultante: {amplitud_calculada}")
print(f"Fase resultante: {fase_calculada}")
print(f"La solucion  de la superposicion de los 2 movimientos armosnicos es: x(t)={amplitud_calculada}*sen({frecuencia_calculada}t+{fase_calculada})")
