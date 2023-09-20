"""Decoradores en Python"""
#Jasser Esteban Villarreal Buitrago


"""
Un decorador en Python es una función que recibe otra función como parámetro.
le añade cosas y retorna una función diferente. Son herramientas muy útiles.
Nos permiten envolver una función dentro de otra y modificar el comportamiento 
de esta última sin modificarla permanentemente.
"""


# def funcion_decoradora(funcion_parametro):
#     def funcion_interior():
#         print("vamos a realizar un calculo:")
#         funcion_parametro()
#         print("calculo terminado.")
#     return funcion_interior


#@funcion_decoradora
def suma():
    print(10+20+30)

#@funcion_decoradora
def resta():
    print(100-13-17)


suma()          #valores fijos

resta()

################################################################
"""

def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args,**kwargs):                   #procese los argumentos, *args,**kwargs)
        print("vamos a realizar un calculo:")
        funcion_parametro(*args,**kwargs)
        print("calculo terminado.")
    return funcion_interior


#@funcion_decoradora
def suma(num1,numb2,numb3):  #recibir n parametros
    print(num1+numb2+numb3)

#@funcion_decoradora
def resta(num1,numb2,numb3):
    print(num1-numb2-numb3)

@funcion_decoradora
def potencia(base,exponente):
    print(pow(base,exponente))

suma(25,25,25)

resta(100,25,25)

potencia(base=2,exponente=4)   #clave valor **kwargs
"""