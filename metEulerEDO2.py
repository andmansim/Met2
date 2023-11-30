'''
Es igual que el EDO1 pero con una variable más que sale de un CV, con esto conseguimos un vector
u(x)=y(x) y v(x)=y'(x) 

'''

import matplotlib.pyplot as plt
import numpy as np

def funcion(x,u, v):
    #la función es y'' + a*y' + b*y = f(x)
    #donde a y b dependen de x 
    #sería (-b * u -a * v + f(x)) = y''(x),  donde sustituimos b, a y f(x)
    return -1 * u - 1 * v + 1


def iterar(x, u, v, f): 
    '''Itera la función'''
    while x <= xf:
        xn = x + h
        un = u + h * v
        vn = v + h * f(x, u, v)
        iterar(xn, un, vn, f(xn, un, vn))
        puntos.append((xn, un))
        print(xn, un)
        return xn, un


def pintar(puntos):
    '''Pinta la gráfica'''
    x = []
    y = []
    for i in puntos:
        x.append(i[0])
        y.append(i[1])
    plt.plot(x, y)
    plt.show()


#Código para pintar las soluciones particulares
def iterar_solu(x,f): 
    '''Itera la función'''
    while x <= xf:
        xn = x + h
        yn =  h * f (x)
        iterar_solu(xn, f)
        puntos_solus.append((xn, yn))
        print(xn, yn)
        return xn, yn


def funcion1(x):
    return (x**2)/(np.exp(x**2))
def funcion2(x):
    return (x**2 + 1)/(np.exp(x**2))




#main
x0 = float(input('Introduce la x inicial: ')) #punto inicial
u0 = float(input('Introduce la u inicial (u = y(x)): ')) #punto inicial
v0 = float(input("Introduce la v inicial (v = y'(x)): ")) #punto inicial
xf = float(input('Introduce el extremo final: ')) #punto final
n = int(input('Número de divisiones: '))
h = (xf - x0)/n #intervalo pequeño
puntos = [] #lista de puntos
puntos_solus=[] #lista de puntos de las soluciones particulares

iterar(x0, u0, v0, funcion)
pintar(puntos)

'''#funciones particulares de la solución real
iterar_solu(x0, funcion1)
pintar(puntos_solus)
puntos_solus=[]
iterar_solu(x0, funcion2)
pintar(puntos_solus)
puntos_solus=[]'''



    


    
