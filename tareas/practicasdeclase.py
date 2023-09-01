#x=int(input("ingrese dinero en copa depositar sin puntos ni comas: "))
#n=int(input("ingrese la cantidad de años: "))
#p=float(input("ingrese el pporcentaje de interes sin el simbolo %: "))
#for i in range(n):
#    x=x*(i+p/100)
#print("su dinero es",x,"cop")

#errores (debugging)
#
for i in range(10):
    num=float(input("ingrese un numero:"))
    if num<0:
        print("ERROR :numero negativo:")
        break
else:
    print("introdujo loS 10 valores ")