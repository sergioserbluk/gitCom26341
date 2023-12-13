import math
while True:
    try:
        x=int(input("ingrese un num: "))
        break
    except:
        print("ingrese un num valido!!")
while True:
    try:
        y=int(input("ingrese un num: "))
        break
    except:
        print("ingrese un num valido!!")
print(f"la raiz de {x} es {math.sqrt(x)}")
print(f"la raiz de {y} es {math.sqrt(y)}")
print(f"la pot de {x} a {y} es {math.pow(x,y)} ")