#En vez de tomar la pendiente de P0 tomamos el valor promedio de la pendiente de P1 y P0
#Teoría en el campus, con este método hemos obtenido un método proporcional a H^3
import matplotlib.pyplot as plt
import numpy as np

def funcion(x,y):
    return (-2*x*(np.exp(x**2)*y-1))/(np.exp(x**2))
def iterar(x, y, f): 
    '''Itera la función'''
    if x > xf:
        return x, y

    xn = x + h
    zn = y + h * f (x,y) #predicción
    yn = y + (h/2) * (f(x,y) + f(xn, zn)) #corrección
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
