'''
Con Python podemos de manera muy simple manejar archivos.
Vamos a ver las instrucciones basicas, como abrir un archivo, leerlo o escribirle informacion.

Abrir un archivo

open(archivo,modo)

archivo --> Es el nombre del archivo, si no va acompañado de una ruta, se tomara la ruta actual.
modo --> uno de los distintos modos para abrir un archivo.

Modos disponibles:
Read ("r") (Leer)
Append ("a") (Agregar)
Write ("w") (Escribir)
Create ("x") (Crear)


Entonces para abrir un archivo como lectura podemos hacer:

creamos un archivo llamado "colores.txt"
'''
#archivo = open("colores.txt","x")
#archivo.close()

#OJO asegurarnos que el script de python este en la misma ruta!

#archivo = open("colores.txt","r")


#La variable archivo, contiene el contenido de colores.txt

#podemos imprimirlo en pantalla usando el metodo read() --> Nos retorna un str con el contenido del archivo.


#print(archivo.read())
#archivo.close()

'''
#Luego de usar un archivo es muy importante cerrarlo, para ello esta el metodo close()





Para crear un archivo
'''
#archivo = open("archivo_nuevo.txt", "x")
'''
Si queremos abrir el archivo y escribir un nuevo contenido, eliminado el anterior lo abrimos con el modo "w·
y luego ejecutando el metodo write() escribira el nuevo contenido
'''
#archivo = open("colores.txt","w")
#archivo.write("Nuevo contenido etc ")
#archivo.close
#archivo=open("colores.txt", "r")
#print(archivo.read())
#archivo.close
'''
Append
Con apend agregamos algo al final del archivo, asi que abrimos en ese modo el archivo
'''
#archivo = open("colores.txt","a")
 #Y luego agregamos texto con el metodo write()
#archivo.write("\nNegro")
#archivo.close
#archivo=open("colores.txt", "r")
#print(archivo.read())
#archivo.close

'''


Como leer el archivo y trabajarlo

Para leer una linea usamos el metodo readline()

archivo.readline(<tamaño_opcional>)
El tamaño es en bytes y es opcional, no lo usaremos nosotros.

Ejemplo
'''
#archivo = open("colores.txt","r")
#print(archivo.readline())
#archivo.close()

'''
Para recorrer o iterar un archivo lo podemos hacer linea por linea de la siguiente manera directamente sobre el objeto de archivo:
'''
#archivo = open("colores.txt","r")
#for linea in archivo:
#  # Realizamos las tareas necesaria con cada linea, ejemplo la imprimimos decorada
#  print("···",linea)
#archivo.close()
'''
Tambien podemos iterar sdobre el resultado del metodo readlines(), el cual devuelve una lista
'''
#archivo = open("colores.txt","r")
#for linea in archivo.readlines():
#  # Realizamos las tareas necesaria con cada linea, ejemplo la imprimimos decorada
#  print("···",linea)
#archivo.close()
#
