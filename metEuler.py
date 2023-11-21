import matplotlib.pyplot as plt
import numpy as np

def funcion(x,y):
    return (y-x**2+1)

def iterar(x, y, f): 
    '''Itera la función'''
    while x <= xf:
        xn = x + h
        yn = y + h * f (x,y)
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

#iterar(x0, y0, funcion)
#pintar(puntos)

#Código para pintar las soluciones particulares
def iterar2(x,f): 
    '''Itera la función'''
    while x <= xf:
        xn = x + h
        yn =  h * f (x)
        iterar(xn, f)
        puntos.append((xn, yn))
        print(xn, yn)
        return xn, yn

def grafica(x, xf, f, h):
    '''Pinta la gráfica'''
    x = np.linspace(x, xf, h)
    y = f(x)
    plt.plot(x, y)
    plt.show()
    
def funcion1(x):
    return (-0.5*np.exp(x) + x**2 + 2*x + 1)
def funcion2(x):
    return (-np.exp(x) + x**2 + 2*x + 1)
def funcion3(x):
    return (-2*np.exp(x) + x**2 + 2*x + 1)

iterar2(x0, funcion1)
iterar2(x0, funcion2)
iterar2(x0, funcion3)
pintar(puntos)

grafica(x0, xf, funcion1)  
grafica(x0, xf, funcion2)
grafica(x0, xf, funcion3)    


    
