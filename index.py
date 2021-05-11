import numpy as np
import matplotlib.pyplot as plt


# class ParOrdenado:
#     def __init__(self,a,b):
#         self.real = int(a)
#         self.imaginario = int(b)


# def graficarComp(lista, colores = ["r", "g", "b"]):
#     x = [0]*len(lista)
#     y = [0]*len(lista)
#     u = []
#     v = []
#     print(x)
#     print(y)
#     print(u)
#     print(v)
#     for vector in lista:
#         u.append(vector.real)
#         v.append(vector.imaginario)

#     izda = min(-1, min(u)-1)
#     dcha = max(1, max(u)+1)
#     abjo = min(-1, min(v)-1)
#     arba = max(1, max(v)+1)

#     plt.quiver(x, y, u, v, angles='xy',scale_units='xy',scale=1,color=colores)
#     #plt.quiver([1],[1],angles='xy',scale_units='xy',scale=1)


#     plt.axhline(0,color='black')
#     plt.axvline(0,color='black')

#     plt.xlim([izda,dcha])
#     plt.ylim([abjo,arba])

#     # return plt.gca()
#     #plt.show()


# x1 = ParOrdenado(1,2)
# x2 = ParOrdenado(-3,5)

# ax = graficarComp([x1, x2])
# plt.show()
# plt.grid()

