from tkinter import *
def cambiar_stringvars(nuevotexto,mitexto):
    mitexto.set(nuevotexto)
v0=Tk()
v0.geometry("200x60")
mitexto=StringVar()
textoentry=StringVar()
entry1=Entry(v0, textvar=textoentry).pack()
label1=Label(v0,textvar=mitexto).pack()
b1=Button(v0, text="Escribir" , command=lambda: cambiar_stringvars(textoentry.get(), mitexto)).pack()
v0.mainloop()
