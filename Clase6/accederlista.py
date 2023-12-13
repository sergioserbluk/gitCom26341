lista=["hola", 1.4, 78, [10,20,30], False,78]
print(f"lista original {lista}")
lista[1]=2.4
print(f"lista modificada {lista}")
indice=lista.index(False)
print(f"false aparece en el indice {indice}")
print(lista[3])