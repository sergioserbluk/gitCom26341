listalumnos=[
    {"legajo":5001, "apellido":"Lopez", "nombre":"Juan", "nota1":8.5 },
    {"legajo":5002, "apellido":"rios", "nombre":"ana", "nota1":9.5 },
    {"legajo":5003, "apellido":"Vargas", "nombre":"Pedro", "nota1":7.5 },
]

dicalumnos={
    5001: {"apellido":"Lopez", "nombre":"Juan", "nota1":8.5} ,
    5002: {"apellido":"rios", "nombre":"ana", "nota1":9.5},
    5003: {"apellido":"Vargas", "nombre":"Pedro", "nota1":7.5 },
}

#muestro la lista de alumnos
for alumno in listalumnos:
    print(f"Legajo: {alumno['legajo']} alumno: {alumno['apellido']}, {alumno['nombre']} Nota: {alumno['nota1']}")
#muestro el diccionario de alumnos
for leg in dicalumnos.keys():
    print(f"legajo: {leg} alumno: {dicalumnos[leg]['apellido']}, {dicalumnos[leg]['nombre']} Nota: {dicalumnos[leg]['nota1']}")