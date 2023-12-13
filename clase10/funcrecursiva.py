# funcion recursiva para hallar el factoreo de un nro
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n - 1)
# llamada a la funcion
print(factorial(8))

print("hola " + "Esto es una prueba" + 5 + 7)
