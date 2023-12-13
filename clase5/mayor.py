
'''
num1 = int(input("ingrese el primer numero "))
num2 = int(input("ingrese el segundo numero "))
num3 = int(input("ingrese el tercer numero "))
if num1>num2 and num1>num3:
    print ("el primer numero es el mayor ",num1)
elif num2>num1 and num2>num3:
        print ("el segundo numero es el mayor ",num2)
elif num3>num1 and num3>num2:
            print ("el tercer numero es el mayor ",num3)
else:
           print ("no se pudo definir un mayor")
'''
'''
num1=int(input("Ingrese num1: "))
num2=int(input("Ingrese num2: "))
num3=int(input("Ingrese el num3: "))
if num1 > num2 and num1 > num3:
    print(f"{num1} es mayor que el resto.")
elif num2 > num1 and num2 > num3:
    print(f"{num2} es mayor que el resto.")
else:
    print(f"{num3} es mayor que el resto.")
'''
'''
numero1 = int (input("Ingresa el primer número: "))
numero2 = int (input("Ingresa el segundo número: "))
numero3 = int (input("Ingresa el tercer número: "))
if numero1>=numero2 and numero1>=numero3:
   mayor=numero1
elif numero2>=numero1 and numero2>=numero3:
    mayor=numero2
else:
    mayor=numero3      
print("el numero mayor es : ", mayor)
'''
num = int(input("ingrese un número"))
nmay=num
i=1
while i<5:
    num =int(input("ingrese otro número"))
    if num > nmay:
        nmay=num
    i+=1
print("el mayor de los num ingresados es " , nmay)