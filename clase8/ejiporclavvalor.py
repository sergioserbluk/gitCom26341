casacas={
    1:"Lopez",
    2:"Ramirez",
    5:"Rios",
    14:"Ayala",
    15:"Rivolta",
    22:"Fleitas",
    27:"Gutierres"
}
#extraigo clave y valor
print("lista de jugadores")
for casaca,nombre in casacas.items():
    print(f" jugador {nombre} camiseta nº {casaca}")