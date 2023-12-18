import matplotlib.pyplot as plt
import numpy as np

#La función cambia con el ejercicio
#En el resultado coger el número que más se parezca al punto inicial dado
def funcion(x,y):
    return (2-3*x -y)/(x-1)

def segunda_derivada(x, y):
    return (3*x + 2*y -1)/(x-1)**2

def iterar(x, y, f, d2): 
    '''Itera la función'''
    if x > xf:
        return x, y
    
    xn = x + h
    yn = y + h * f (x,y) + (h**2/2) * d2(x,y)
    
    iterar(xn, yn, f, d2)
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

iterar(x0, y0, funcion, segunda_derivada)
pintar(puntos)
