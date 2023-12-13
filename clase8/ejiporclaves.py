casacas={
    1:"Lopez",
    2:"Ramirez",
    5:"Rios",
    14:"Ayala",
    15:"Rivolta",
    22:"Fleitas",
    27:"Gutierres"
}

#recorrer por claves
print("lista de jugadores")
for camiseta in casacas.keys():
    print(f"camiseta nº {camiseta} jugador {casacas[camiseta]}")