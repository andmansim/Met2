import matplotlib.pyplot as plt
import numpy as np

def funcion(x,y):
    return (1 + 4*x*y)/(3*x**2)

def iterar(x, y, f): 
    '''Itera la función'''
    while x <= xf:
        xn = x + h
        yn = y + h * f (x + (h/2), y+ (h/2) * f(x,y))
        iterar(xn, yn, f)
        puntos.append((xn, yn))
        print(xn, yn)
        return xn, yn


def pintar(puntos):
    '''Pinta la gráfica'''
    x = []
    y = []
    for i in puntos:
        x.append(i[0])
        y.append(i[1])
    plt.plot(x, y)
    plt.show()

#main
x0 = float(input('Introduce la x inicial: ')) #punto inicial
y0 = float(input('Introduce la y inicial: ')) #punto inicial
xf = float(input('Introduce el extremo final: ')) #punto final
n = int(input('Número de divisiones: '))
h = (xf - x0)/n #intervalo pequeño
puntos = [] #lista de puntos

iterar(x0, y0, funcion)
pintar(puntos)
    