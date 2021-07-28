import tkinter
from tkinter import messagebox
from math import sqrt

def calcular():
    n1 = txtnumero1.get()
    coefvariLINE = txtnumero2.get()
    termIndepe = txtnumero3.get()

    A=int(n1)
    B=int(coefvariLINE)
    C=int(termIndepe)


    if (len(n1) == 0):
        messagebox.showinfo(message="Ingrese el coeficiente variable cuadratica !!", title="Mensaje")
        txtnumero1.focus()
    if (len(coefvariLINE) == 0):
        messagebox.showinfo(message="Ingrese el coeficiente variable lineal !!", title="Mensaje")
        txtnumero1.focus()
    if (len(termIndepe) == 0):
        messagebox.showinfo(message="Ingrese el termino independiente!!", title="Mensaje")
        txtnumero1.focus()

    else:

        x1 = 0
        x2 = 0

        if ((B ** 2) - 4 * A * C) < 0:
            print("La solución de la ecuación es con números complejos")
        else:
            x1 = (-B + sqrt(B ** 2 - (4 * A * C))) / (2 * A)
            x2 = (-B - sqrt(B ** 2 - (4 * A * C))) / (2 * A)
            print("Las soluciones de la ecuación son:")
            area.insert(1.0, "\nLas soluciones de la ecuación son:")
            area.insert(1.0, "\nX1:"+str(x1))
            area.insert(1.0, "\nX2:"+str(x2))


ventana = tkinter.Tk()  # instancia del formulario
ventana.title("Ventana Principal")
ventana.geometry("600x500")
# ventana.configure(background='green')
lblnumero1 = tkinter.Label(ventana, text='ingrese el coeficiente de la variable cuadratica:')
lblnumero1.place(x=100, y=50)
txtnumero1 = tkinter.Entry(ventana, width=20)
txtnumero1.place(x=410, y=50)

lblnumero2 = tkinter.Label(ventana, text='ingrese el  coeficiente de la variable lineas:')
lblnumero2.place(x=100, y=80)
txtnumero2 = tkinter.Entry(ventana, width=20)
txtnumero2.place(x=410, y=80)

lblnumero3 = tkinter.Label(ventana, text='ingrese el  termino independiente:')
lblnumero3.place(x=100, y=110)
txtnumero3 = tkinter.Entry(ventana, width=20)
txtnumero3.place(x=410, y=110)

boton = tkinter.Button(ventana, text="calcular raices ", command=calcular)
boton.place(x=250, y=140)
area = tkinter.Text(ventana)
area.config(width=42, height=13)
area.place(x=100, y=190)

ventana.mainloop()  # ejec