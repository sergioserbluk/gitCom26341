#creo la funcion sumados
def sumaDos(pn,sn):
    res = int(pn) + int(sn)
    return res
#aca comienza el programa
n1 = input("ingrese un número: ")
n2 = input("ingrese otro número: ")
#llamo a la funcion
print("la suma de los números es: " , sumaDos(n1, n2))