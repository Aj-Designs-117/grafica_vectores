import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

root = tkinter.Tk()
root.wm_title("Embedding in Tk")

# Tamaño de la grafica
fig = Figure(figsize=(5, 4), dpi=100)
# valores de la grafica
t = np.arange(0, 3, .01)
#OPERACIO O TIPO DE GRAFICADO
fig.add_subplot().plot(t, 2 * np.sin(2 * np.pi * t))


canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()

# pack_toolbar=False will make it easier to use a layout manager later on.
toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
toolbar.update()

# BARRA DE ACCIONES
toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)

# muestra la grafica
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

tkinter.mainloop()