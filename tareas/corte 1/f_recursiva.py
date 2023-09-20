



# funcion recursiva para suma de numeros



def suma_recursiva(n):
    
    if n == 0:
        return 0
    
    else:
        return n + suma_recursiva(n - 1)

print("suma recursiva:")
resultado = suma_recursiva(6)
print(resultado)  


#Función recursiva para sumar números de la forma [1,2,[3,4],[5,6],[[7,8]]]


#Función recursiva para hallar la potencia de un número
"""
def potencia_recursiva(n,b):
    
     if b == 0:
         
         return 1

     elif b == 1:

        return n
     
     elif b > 0:

        return n**potencia_recursiva(0,b)

print("potencia recursiva")
resultado_1 = potencia_recursiva(2,2)
print(resultado_1)  

#

def derivada_recursiva(a,n):
    
     if a == 0:
         
         return 0

     elif n == 0:

        return a
     
     
     else :

        return n**derivada_recursiva(a,n)

print("derivada recursiva")
resultado_1 = derivada_recursiva(2,2)
print(resultado_1)  
     """