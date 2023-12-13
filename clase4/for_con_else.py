cadena="hola"
le=input("ingrese la letra a buscar: ")
for letra in cadena:
    if letra==le:
        print("encontrada")
        break
else: 
    print("no encontrada")