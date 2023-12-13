import os
def menu():
    os.system("cls")
    print("*********menu*********")
    print("1 para sumar")
    print("2 para restar")
    print("3 para mult")
    print("4 para divi")
    print("5 para salir")
    op=int(input("seleccione una opcion: "))
    return op
def sumar(pn,sn):
    res=pn + sn
    return res
def restar(pn, sn):
    res= pn - sn
    return res
def multi(pn,sn):
    res=pn * sn
    return res
def divi(pn, sn):
    try:
        res = pn / sn
        return res
    except:
        print("no es posible dividir por 0")
        return
#arranca el programa
resp="N"
while True:
    op=menu()
    if op!=5: #si la op es 5 no pide los numero ya que el us quiere salir
        if resp=="N":
            n1=float(input("ingrese un num: "))
        else:
            n1=res
        n2=float(input("ingrese otro num: "))
    if op==1:
        res=sumar(n1,n2)
        print(f" {n1} + {n2} = {res}")
        #input("presione enter para continuar...")
    elif op==2:
        res=restar(n1,n2)
        print(f"el resultado de restar {n1} y {n2} es {res}")
        #input("presione enter para continuar...")
    elif op == 3:
        res=multi(n1,n2)
        print(f"el resultado de mult {n1} y {n2} es {res}")
        #input("presione enter para continuar...")
    elif op == 4:
        res=divi(n1,n2)
        print(f"el resultado de divi {n1} entre {n2} es {res}")
        #input("presione enter para continuar...")
    elif op == 5:
        break 
    resp=input("quiere seguir operando con el resultado? S/N: ")


