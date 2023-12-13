milista=[1,2,3]
print(f"la lista original es: {milista}")

milista.append(5)
milista.insert(3,4)
otralista=[6,7,8]
milista.extend(otralista)
print("lista actual")
for elemento in milista:
    print(f"elemento {elemento}")
