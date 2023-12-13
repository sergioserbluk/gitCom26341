from tkinter import *
def ejecutar(f):
    v0.after(200,f)
def ocultar(ventana):
    ventana.withdraw()
def mostrar(ventana):
    ventana.deiconify()
v0=Tk()
v0.geometry("400x300")
v1=Toplevel(v0)
v1.withdraw()
b1=Button(v0,text="abrir v1", command=lambda:ejecutar(mostrar(v1)))
b1.grid(row=1, column=1)
b2=Button(v0,text="ocultar v1", command=lambda:ejecutar(ocultar(v1)))
b2.grid(row=1,column=2)

v0.mainloop()