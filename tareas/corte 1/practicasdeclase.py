#x=int(input("ingrese dinero en copa depositar sin puntos ni comas: "))
#n=int(input("ingrese la cantidad de años: "))
#p=float(input("ingrese el pporcentaje de interes sin el simbolo %: "))
#for i in range(n):
#    x=x*(i+p/100)
#print("su dinero es",x,"cop")

#errores (debugging)
#
#for i in range(10):
#    num=float(input("ingrese un numero:"))
#    if num<0:
#        print("ERROR :numero negativo:")
#        break
#else:
#    print("introdujo loS 10 valores ")


#un juego para adivinar un numero
#a=10
"""
b=100
n=randint(a,b)
for i in range(5)
    gess=int(input("huhihi"))
    if gess>n:
        print("hhdjjddj")
    elif gess<n:
        print("uhdidhid")
    else:
        print("ganaste")
        break

    


from typing import Any

"""
"""
class vector:

    
    Clase vector en 2D con coordenadas cartesianas y polares.
    Permite suma entre vectores y multiplicación
    def __init__(self, a, b):
        self.x = a
        self.y = b
        self.magnitud = (a**2+b**2)**0.5
    def __add__(self, otro):
        F3=vector(self.x+otro.x, self.y+otro.y)
        return(F3)
    def __str__(self):
        cadena="["+str(self.x)+" "+str(self.y)+"]"
        return(cadena)
    def __abs__(self):
        return(self.magnitud)
    def __call__(self, m:float):
        
        #Metodo que recibe la masa m como flotante y retorna un vector con
        correspondiente al vector ingresado dividido la masa

        Args:
            m (float): masa
    
        
        return(vector(self.x/m, self.y/m))
#print(type(str(21)))
F1=vector(2,3)
print(abs(F1))
#F2=vector(-2,3)
#print(F1(3))
if F1(2).magnitud==0:
    print("Está en equilibrio")
else:
    print("No esta en equilibrtio")
#print(F2)
#Resultado=F1 + F2 +F1 + F2 +F2
#print(Resultado.magnitud)
#name=input("Ingrese su nombre: ")
#print("Hola",name)
#edad=float(input("Ingrese su edad: "))
#print("Año",2023-edad)
#print("Tipo de dato edad",type(edad))
#print("Tipo de dato name",type(name))

"""

#JSON
#javaascript,objet,notation
#cadenas y listas[ESTUDIAR]tumplpas y diccionarios
#metodos de dicionarioss
#tumplas,una lista que es inmutable
# con un dicionario la llave no puede ser lista pero si un tumpla
#copy()otro espacio de memoria
#[set y generadores]

"""

for i in [3,20,8]:
    print(i)


lista=[1,2,3,4,5,6,7,8,9]
print(lista[2:8])
print(lista[2:8:2])
#sum(lista)

lista=[1,2,3,4,5,6,7,8,9,10,11]
    #for i in range(9):
   # print(lista.append(i**2))
   # lista.index(2)

"hola mundo!"
palabra="hola mundo!"
palabra[-1]

"""
def torre_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f'Mueve disco 1 de {origen} a {destino}')
        return
    torre_hanoi(n - 1, origen, auxiliar, destino)
    print(f'Mueve disco {n} de {origen} a {destino}')
    torre_hanoi(n - 1, auxiliar, destino, origen)

# Cambia el número de discos según tus necesidades
num_discos = 2

torre_hanoi(num_discos, 'A', 'C', 'B')

 