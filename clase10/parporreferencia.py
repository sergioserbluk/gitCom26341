#funcion que recibe una coleccion y la multiplica por 2
def doblarnum(nros):
    for indice in range(len(nros)):
        nros[indice]= nros[indice] * 2
    return nros
#aca empieza el programa
minum = [10, 20, 5]
print(doblarnum(minum))
print(minum)