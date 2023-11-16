import matplotlib.pyplot as plt
import numpy as np

def funcion(x,y):
    return (2-3*x -y)/(x-1) 
def funcion2(x,y):
    return (1+4*x*y)/(3*x**2)
def iterar(x, y, f): 
    '''Itera la función'''
    while x <= xf:
        #constantes (pesos)
        a1 = 1/6
        a2 = 1/3
        a3 = 1/3
        a4 = 1/6
        
        #Pendientes
        k1 = f(x, y)
        k2 = f(x +(h/2), y + (h/2)*k1)
        k3 = f(x +(h/2), y + (h/2)*k2)
        k4 = f(x +h, y + h*k3)
        
        #función
        xn = x + h
        yn = y + h*(a1*k1 + a2*k2 + a3*k3 + a4*k4) 
        
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
iterar(x0, y0, funcion2)
pintar(puntos)
