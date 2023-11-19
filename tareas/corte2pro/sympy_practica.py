import sympy as sym

# #La clase Racional representa un número racional como un par de dos Números Enteros: el numerador
# #  y el denominador, por lo que representa 1/2, 5/2 y
# #  así sucesivamente:Rational(1, 2)Rational(5, 2)

# a = sym.Rational(1, 2)
# print(a)

# #SymPy utiliza mpmath en segundo plano, lo que permite realizar cálculos utilizando aritmética de precisión}
# #  arbitraria. De esa manera, algunas constantes especiales, como mi, Pi, oh(Infinito), se tratan como símbolos
# #  y se pueden evaluar con precisión arbitraria:

# sym.pi**2


# b = sym.pi.evalf()
# print(b)

# c= (sym.pi + sym.exp(1)).evalf()
# print(c)



# sym.oo > 99999
# print(sym.oo > 99999)

# sym.oo + 1
# print(sym.oo + 1)

# # Calcula la raíz cuadrada de 2 con 100 decimales
# sqrt_2 = sym.sqrt(2)
# decimal_representation = sqrt_2.evalf(100)

# print(decimal_representation)



# # Define las fracciones
# frac_1 = sym.Rational(1, 2)
# frac_2 = sym.Rational(1, 3)

# # Calcula la suma
# result = frac_1 + frac_2

#print(result)

x = sym.Symbol('x')
y = sym.Symbol('y')


# print(x + y + x - y)


# print((x + y) ** 2)

##Utilice esto para expandir una expresión algebraica. Intentará denificar potencias y multiplicaciones:
# print(sym.expand((x + y) ** 3))
# print(3 * x * y ** 2 + 3 * y * x ** 2 + x ** 3 + y ** 3)

# # # x**3 + 3*x**2*y + 3*x*y**2 + y**3
# # # x**3 + 3*x**2*y + 3*x*y**2 + y**3


# print(sym.expand(x + y, complex=True))
# print(sym.I * sym.im(x) + sym.I * sym.im(y) + sym.re(x) + sym.re(y))
# print(sym.expand(sym.cos(x + y), trig=True))
# print(sym.cos(x) * sym.cos(y) - sym.sin(x) * sym.sin(y))


# # re(x) + re(y) + I*im(x) + I*im(y)
# # re(x) + re(y) + I*im(x) + I*im(y)
# # -sin(x)*sin(y) + cos(x)*cos(y)
# # -sin(x)*sin(y) + cos(x)*cos(y)

####Utilice simplificar si desea transformar una expresión a una forma más simple:

#print(sym.simplify((x + x * y) / x))




####Los límites son fáciles de usar en SymPy, siguen la sintaxis , por lo que para calcular el límite de as ,
#  deberías emitir :limit(function, variable, point)f(x)x\flecha derecha 0limit(f, x, 0)

print(sym.limit(sym.sin(x) / x, x, 0))

#También puedes calcular el límite en el infinito:

print(sym.limit(x, x, sym.oo))

print(sym.limit(1 / x, x, sym.oo))

print(sym.limit(x ** x, x, 0))