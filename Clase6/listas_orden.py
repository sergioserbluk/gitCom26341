'''
lista_num=[3,5.1,4,6.3,8,7]
lista_frutas=["anana", "pera", "manzana","kiwi"]
print(f"la lista de num original {lista_num}")
print(f"la lista de frutas original {lista_frutas}")
lista_num.sort()
lista_frutas.sort()
print(f"la lista de num luego de ordenar {lista_num}")
print(f"la lista de frutas luego de ordenar {lista_frutas}")
lista_num.sort(reverse=True)
lista_frutas.sort(reverse=True)
print(f"la lista de num ord a rev {lista_num}")
print(f"la lista de frutas oed a rev {lista_frutas}")
'''
lista_num=[3,5.1,4,6.3,8,7,3,7,3]
lista_frutas=["anana", "pera", "manzana","kiwi"]
ce=len(lista_num)
print(f"la lista de num tiene {ce} elementos")
print(f"la lista de frutas tiene {len(lista_frutas)} elementos")
el = int(input("ingrese un num a buscar "))
print(f"el num {el} aparece {lista_num.count(el) } veces")