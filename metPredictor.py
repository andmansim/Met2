#En vez de tomar la pendiente de P0 tomamos el valor promedio de la pendiente de P1 y P0
#Teoría en el campus, con este método hemos obtenido un método proporcional a H^3
import matplotlib.pyplot as plt
import numpy as np

def funcion(x,y):
    return (2-3*x -y)/(x-1) 
def funcion2(x,y):
    return (1+4*x*y)/(3*x**2)
def iterar(x, y, f): 
    '''Itera la función'''
    while x <= xf:
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
iterar(x0, y0, funcion2)
pintar(puntos)
# Con esta función (2-3*x -y)/(x-1) tenemos, solción real es y(6) = -8,20 y la solución aproximada es w100 = -8,20 --> tenemos un error de 0
# Con esta función (1+4*x*y)/(3*x**2) tenemos, solución real es y(4)= -11,46 y la solución aproximada es w100 = -11.45395 --> tenemos un error de 0.00605