import matplotlib.pyplot as plt
import numpy as np

def funcion(x,y):
    return (2-x-y)/(x-y+4)

def funcion2(x,y):
    return 2 *x * np.exp(-3*x) -3*y

def iterar(x, y, f): #saca los distintos puntos de la gráfica
    while x <= xf:
        xn = x + h
        yn = y + h * f (x,y)
        iterar(xn, yn, f)
        puntos.append((xn, yn))
        print(xn, yn)
        return xn, yn


def pintar(puntos):
    x = []
    y = []
    for i in puntos:
        x.append(i[0])
        y.append(i[1])
    plt.plot(x, y)
    plt.show()
    
x0 = int(input('Introdice la x inicial: ')) #punto inicial
y0 = int(input('Introduce la y inicial: ')) #punto inicial
xf = 9 #punto final
n = int(input('Número de divisiones: '))
h = (xf - x0)/n #intervalo pequeño
puntos = [] #lista de puntos

iterar(x0, y0, funcion2)
pintar(puntos)
        


    
