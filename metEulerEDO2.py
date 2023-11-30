'''
Es igual que el EDO1 pero con una variable más que sale de un CV, con esto conseguimos un vector
u(x)=y(x) y v(x)=y'(x) 

'''

import matplotlib.pyplot as plt
import numpy as np

def funcion(x,y):
    return (-2*x*(np.exp(x**2)*y-1))/(np.exp(x**2))

def valorA(x):
    return -2*x

def valorB(x):  
    return 0*x

def iterar(x, u, v, b, a, f): 
    '''Itera la función'''
    while x <= xf:
        xn = x + h
        un = u + h * v
        vn = v + h * (-b * u - a * v + f(x))
        iterar(xn, un, vn, valorB(xn), valorA(xn), f)
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

iterar(x0, u0, v0, valorB(x0), valorA(x0), funcion)
pintar(puntos)

'''#funciones particulares de la solución real
iterar_solu(x0, funcion1)
pintar(puntos_solus)
puntos_solus=[]
iterar_solu(x0, funcion2)
pintar(puntos_solus)
puntos_solus=[]'''



    


    
