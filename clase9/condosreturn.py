def esmayor(ed):
    if ed >= 18:
        return "es mayor de edad"
    return "no es mayor de edad"
edad = int(input("ingrese su edad: "))
print(esmayor(edad))