from tkinter import *
import numpy as np
import functools
import matplotlib.pyplot as plt
# import matplotlib.patches as patches
# from matplotlib.backends.backend_tkagg import (
#     FigureCanvasTkAgg, NavigationToolbar2Tk)
# # Implement the default Matplotlib key bindings.
# from matplotlib.backend_bases import key_press_handler
# from matplotlib.figure import Figure

class params:
    def __init__(self,a,b):
        self.real = int(a)
        self.imaginario = int(b)


def grafics (lista, colores = ["r", "g", "b"]):
    x = [0]*len(lista)
    y = [0]*len(lista)
    u = []
    v = []

    for vector in lista:
        u.append(vector.real)
        v.append(vector.imaginario)

    izda = min(-1, min(u)-1)
    dcha = max(1, max(u)+1)
    abjo = min(-1, min(v)-1)
    arba = max(1, max(v)+1)

    plt.quiver(x, y, u, v, angles='xy',scale_units='xy',scale=1,color=colores)

    plt.axhline(0,color='black')
    plt.axvline(0,color='black')

    plt.xlim([izda,dcha])
    plt.ylim([abjo,arba])


def calcVector(VecX, VecY, VecX1, VecY1, label10):

    AVX = float(VecX.get())
    AVY = float(VecY.get())
    BVX = float(VecX1.get())
    BVY = float(VecY1.get())

    AXBY = np.array([AVX , BVX])
    AXBY = AXBY.astype(int)

    BXBY = np.array([AVY, BVY])
    BXBY = BXBY.astype(int)

    AB = (AXBY) - (BXBY)
    label10["text"] = AB

    x1 = params(AVX, BVX)
    x2 = params(AVY, BVY)

    ax = grafics([x1, x2])
    plt.show()

def calcAreaParalelo(Base, Height, label6):
    base = float(Base.get())
    height = float(Height.get())

    # Operacion
    Area = int(base * height)
    label6["text"] = Area

    x1 = params(base,height)
    x2 = params(height, base)

    ax = grafics([x1, x2])
    plt.show()

# VENTANA PARA GRAFICAR UN VECTOR
def openVector():
    root.withdraw()
    win1 = Toplevel()
    win1.geometry('500x350')
    win1.title("Area del Vector")

    titleWindow = Label(win1, text = "Introduzca sus Datos")
    titleWindow.config(font = ("Arial", 24), padx = 5, pady = 10)
    titleWindow.grid(row = 0, column = 0, columnspan = 4)

    #PRIMERA FILA DE DATOS
    label1 = Label(win1, text = "A =")
    label1.config(font = ("Arial", 12), padx = 5, pady = 10)
    label1.grid(row = 1, column = 0)

    label2 = Label(win1, text = "X")
    label2.config(font = ("Arial", 12), pady = 10)
    label2.grid(row = 1, column = 1)

    VecX = Entry(win1)
    VecX.grid(row = 1, column = 2)

    label3 = Label(win1, text = "menos")
    label3.config(font = ("Arial", 12), padx = 5, pady = 10)
    label3.grid(row = 1, column = 3)


    label4 = Label(win1, text = "Y")
    label4.config(font = ("Arial", 12), padx = 15, pady = 10)
    label4.grid(row = 1, column = 4)

    VecY = Entry(win1)
    VecY.grid(row = 1, column = 5)

    #SEGUNDA FILA DE DATOS
    label5 = Label(win1, text = "B =")
    label5.config(font = ("Arial", 12), padx = 5, pady = 10)
    label5.grid(row = 2, column = 0)

    label6 = Label(win1, text = "X")
    label6.config(font = ("Arial", 12), pady = 10)
    label6.grid(row = 2, column = 1)

    VecX1 = Entry(win1)
    VecX1.grid(row = 2, column = 2)

    label7 = Label(win1, text = "menos")
    label7.config(font = ("Arial", 12), padx = 5, pady = 10)
    label7.grid(row = 2, column = 3)

    label8 = Label(win1, text = "Y")
    label8.config(font = ("Arial", 12), padx = 15, pady = 10)
    label8.grid(row = 2, column = 4)

    VecY1 = Entry(win1)
    VecY1.grid(row = 2, column = 5)

    label9 = Label(win1, text = "Resultado:")
    label9.config(font = ("Arial", 12), padx = 20, pady = 10)
    label9.grid(row = 3, column = 0, columnspan = 4)
    label10 = Label(win1, text = "")
    label10.config(font = ("Arial", 12), pady = 10)
    label10.grid(row = 3, column = 2, columnspan = 3)

    btnCalcVec = Button(win1, text = "Calcular", command = lambda: calcVector(VecX, VecY, VecX1, VecY1, label10))
    btnCalcVec.config( font = ("Arial", 15),  width = 20,)
    btnCalcVec.grid(row = 4, column = 0,  columnspan = 7, ipady = 5, pady = 20)

    btnClose = Button(win1, text = "Cerrar", command = win1.destroy)
    btnClose.config( font = ("Arial", 15),  width = 20,)
    btnClose.grid(row = 5, column = 0,  columnspan = 7, ipady = 5)
    

def openParalelo():
    root.withdraw()
    win2 = Toplevel()
    win2.geometry('520x350')
    win2.title("Area del Paralelogramo")

    titleWindow = Label(win2, text = "Introduzca sus Datos")
    titleWindow.config(font = ("Arial", 24), padx = 5, pady = 10)
    titleWindow.grid(row = 0, column = 0, columnspan = 4)

    #PRIMERA FILA DE DATOS
    label1 = Label(win2, text = "Area = ")
    label1.config(font = ("Arial", 12), padx = 5, pady = 10)
    label1.grid(row = 1, column = 0)

    label2 = Label(win2, text = "Base")
    label2.config(font = ("Arial", 12), padx = 5, pady = 10)
    label2.grid(row = 1, column = 1)

    Base = Entry(win2)
    Base.grid(row = 1, column = 2)

    label3 = Label(win2, text = "por")
    label3.config(font = ("Arial", 12), padx = 5, pady = 10)
    label3.grid(row = 1, column = 3)

    label4 = Label(win2, text = "Altura")
    label4.config(font = ("Arial", 12), padx = 5, pady = 10)
    label4.grid(row = 1, column = 4)

    Height = Entry(win2)
    Height.grid(row = 1, column = 5)

    label5 = Label(win2, text = "Resultado:")
    label5.config(font = ("Arial", 12), padx = 5, pady = 10)
    label5.grid(row = 2, column = 0, columnspan = 4)
    label6 = Label(win2, text = "")
    label6.config(font = ("Arial", 12))
    label6.grid(row = 2, column = 2,  columnspan = 2)

    btnCalcParale = Button(win2, text = "Calcular", command = lambda: calcAreaParalelo(Base, Height, label6) )
    btnCalcParale.config( font = ("Arial", 15),  width = 20,)
    btnCalcParale.grid(row = 3, column = 0,  columnspan = 7, ipady = 5, pady = 20)

    btnClose = Button(win2, text = "Cerrar", command = win2.destroy)
    btnClose.config( font = ("Arial", 15),  width = 20,)
    btnClose.grid(row = 4, column = 0,  columnspan = 7, ipady = 5)


# VENTANA PRINCIPAL

root = Tk()
root.geometry('500x400')
root.title("Operaciones")

label = Label(root, text = 'Operaciones Gemetricas')
label.config(font = ("Arial", 24), padx = 5, pady = 10)
label.pack(anchor=NW)

btn1 = Button(root, text = "Grafica un vector", command = openVector)
btn1.config( font = ("Arial", 15),  width = 20 )
btn1.pack(pady = 50, ipady = 5)

btn2 = Button(root, text = "Area de un paralelogramo", command = openParalelo)
btn2.config( font = ("Arial", 15),  width = 20 )
btn2.pack(ipadx = 5, ipady = 5)

root.mainloop()






