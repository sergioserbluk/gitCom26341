def divide(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print("no se puede dividir por cero!!!")
    else:
        print(f"el resultado de dividir {x} entre {y} es: {result}")
    finally:
        print("fin de la division ")
divide(4,2)
divide(4,0)
divide(8,2)