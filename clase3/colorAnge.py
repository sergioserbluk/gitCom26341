color = input("escriba un color: ")
if color.lower() == "rojo" or color.lower() == "amarillo" or color.lower() == "azul":
    print(f"el color {color} es primario")
elif color.lower() == "verde" or color.lower() == "naranja" or color.lower() == "violeta":
    print(f"el color {color} es secundario")
else:
    print(f"{color} esta en una gama de color")