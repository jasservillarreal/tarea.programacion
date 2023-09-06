
#suma de  2 movimientos armonimath.cos simpples
#()
import math

class movimiento_armonico:

    def __init__ (self,frecuencia,amplitud1,fase1,amplitud2,fase2):
        self.frecuencia=frecuencia
        self.amplitud1=amplitud1
        self.fase1=fase1
        self.amplitud2=amplitud2
        self.fase2=fase2
    
    def calcular_amplitud(self):
        amplitud=((self.amplitud1*math.cos(self.fase1)+self.amplitud2*math.cos(self.fase2))**(1/2)+(self.amplitud1*math.sin(self.fase1)+self.amplitud2*math.sin(self.fase2))**(1/2))**(1/2)
        
    def calcular_fase(self):
        fase=math.atan((self.amplitud1*math.cos(self.fase1)+self.amplitud2*math.cos(self.fase2))/(self.amplitud1*math.sin(self.fase1)+self.amplitud2*math.sin(self.fase2)))

        return movimiento_armonico
 #datos del primer movimiento armonico
 frecuencia=input(float("insrese la frecuencia natural de los dos movimientos armonimath.cos"))
 amplitud1=input(float("ingrese la amplitud del primer movimiento"))
 fase1=input(float("ingrese la fase del primer movimiento"))
 # dato del segundo movimiento armonico  
 amplitud2=input(float("ingrese la amplitud del segundo movimiento"))
 fase2=input(float("ingrese la fase del segundo movimiento"))

    