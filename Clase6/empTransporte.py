'''
l_estaciones=["Paso De Los Libres", "La Cruz", "Santo Tomé", "Gobernador Virasoro"]
while True:
    print("1 para listar estaciones de Ida")
    print("2 para listar estaciones de regreso")
    print("3 para salir")
    op=input("ingrse una opcion")
    if op == "1":
        print("*********estaciones de ida *********")
        for estacion in l_estaciones:
            print(estacion)
    elif op=="2":
        print("*********estaciones de regreso *********")
        l_estaciones.reverse()
        for estacion in l_estaciones:
            print(estacion)
        l_estaciones.reverse()
    elif op=="3":
        break
    else:
        print("opcion incorrecta")

'''
l_estaciones=["Paso De Los Libres", "La Cruz", "Santo Tomé", "Gobernador Virasoro"]
for estacion in l_estaciones:
    print(estacion)
ce=len(l_estaciones)-1
while ce >=0:
    print(l_estaciones[ce])
    ce-=1