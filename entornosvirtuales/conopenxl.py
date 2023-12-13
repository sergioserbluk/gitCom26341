from openpyxl import Workbook
#crear el objeto tipo workbook
wb=Workbook()
# seteo el nombre para el archivo
archivo="datos.xlsx"
hoja1=wb.active
hoja1.title="inicial"

hoja1["A1"]="hola"
hoja1["B1"]="clase"

#guardo el archivo con el nombre setado
wb.save(filename=archivo)

#leer un valor
print(hoja1["B1"].value)
input("pulse una tecla")