'''
calif = int(input("Ingrese una calificacion numerica del 1-10: "))
if calif <= 6:
    print("Desaprobado")
elif calif >=7 and calif <=8:
    print("Aprobado")
elif calif >=9 and calif <=10:
    print("Distinguido")
else:
    print("error")
'''
'''
calif = int(input("Ingrese una calificacion numerica del 1-10: "))
if calif <= 6:
    print("Desaprobado")
if calif >=7 and calif <=8:
    print("aprobado")
if calif >=9 and calif <=10:
    print("distinguido")
'''
'''
calif = int(input("Ingrese una calificacion numerica del 1-10: "))
if calif <= 6:
    print("Desaprobado")
elif calif <=8:
    print("Aprobado")
elif calif <=10:
    print("Distinguido")
else:
    print("error")
'''
'''
calif = float(input("ingrese calificacion:"))
if calif <= 6:
    print ("esta desaprobado")
elif calif >= 7 and calif <=8:
    print("esta aprobado")
elif calif > 8:
    print("es ud un distinguido")
'''

while True:
    nota = int(input("INGRESAR LA NOTA DEL ALUMNO: " ))
    if nota == 0:
        print("DESAPROBADO")
        break
    elif nota == 1:
        print("DESAPROBADO")
        break
    elif nota == 2:
        print("DESAPROBADO")
        break
    elif nota == 3:
        print("DESAPROBADO")
        break
    elif nota == 4:
        print("DESAPROBADO")
        break
    elif nota == 5:
        print("DESAPROBADO")
        break
    elif nota == 6:
        print("DESAPROBADO")
        break
    elif nota == 7:
        print  (" APROBADO")
        break
    elif nota == 8:
        print  (" APROBADO")
        break
    elif nota == 9:
        print ("DISTINGUIDO")
        break  
    elif nota == 10:
        print ("DISTINGUIDO")  
        break
    elif nota == 10:
        print ("DISTINGUIDO")
        break
    else:
        print ("error ingrese nuevamente la nota")