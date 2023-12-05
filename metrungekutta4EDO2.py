'''
Ahora es vectorial. Para las kij hemos cambiado las f por el vector u v prima, donde la
a y b dependen de xi, vi, ui y f(xi)
'''


import matplotlib.pyplot as plt
import numpy as np

def funcion(x,y):
    return (-2*x*(np.exp(x**2)*y-1))/(np.exp(x**2))
def iterar(x, y, f): 
    '''Itera la función'''
    while x <= xf:
        #constantes (pesos)
        a1 = 1/6
        a2 = 1/3
        a3 = 1/3
        a4 = 1/6
        
        #Pendientes
        (k11, k12) = [[0, 1], [-b(x), -a(x)]]*[[u], [v]] + [0, f(x)]
        (k21, k22) = [[0, 1], [-b(xn), -a(xn)]]*[[u + (h/2)*k11], [v + (h/2)*k12]] + [0, f(x +(h/2))]
        (k31, k32) = [[0, 1], [-b(xn), -a(xn)]]*[[u + (h/2)*k21], [v + (h/2)*k22]] + [0, f(x +(h/2))]
        (k41, k42) = [[0, 1], [-b(xn), -a(xn)]]*[[u + h*k31], [v + h*k32]] + [0, f(x +h)]
        
        k2 = f(x +(h/2), y + (h/2)*k1)
        k3 = f(x +(h/2), y + (h/2)*k2)
        k4 = f(x +h, y + h*k3)
        
        #función
        xn = x + h
        un = u + h*(a1*k11 + a2*k21 + a3*k31 + a4*k41)
        vn = v + h*(a1*k12 + a2*k22 + a3*k32 + a4*k42) 
        
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

#huele muy mal