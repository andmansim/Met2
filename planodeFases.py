import matplotlib.pyplot as plt
import numpy as np

def funcionx(x, u, v):
    #Es la función de x'(t) = -v + u*(1 - u**2 + v**2)
    # u = x(t), v = y(t)
    return -v + u * (1 - u**2 - v**2)

def funciony (x, u, v):
    #Es la función de y'(t) = u + v*(1 - u**2 - v**2)
    #u= x(t) y v = y(t)
    return u + v * (1 - u**2 - v**2)

def iterar(x, u, v, fx, fy): 
    '''Itera la función'''
    while x <= xf:
        #constantes (pesos)
        a1 = 1/6
        a2 = 1/3
        a3 = 1/3
        a4 = 1/6
        
        #Pendientes
        k11 = fx(x, u, v) #función especial que llama a una función especial dependiendo del sistema que nos den
        k12 = fy(x, u, v) 
        k21 = fx(x +(h/2), u + (h/2)*k11, v + (h/2)*k12)
        k22 = fy(x +(h/2), u + (h/2)*k11, v + (h/2)*k12)
        k31 = fx(x +(h/2), u + (h/2)*k21, v + (h/2)*k22)
        k32 = fy(x +(h/2), u + (h/2)*k21, v + (h/2)*k22)
        k41 = fx(x +h, u + h*k31, v + h*k32)
        k42 = fy(x +h, u + h*k31, v + h*k32)
        
        
        
        #función
        xn = x + h
        un = u + h*(a1*k11 + a2*k21 + a3*k31 + a4*k41)
        vn = v + h*(a1*k12 + a2*k22 + a3*k32 + a4*k42) 
        
        iterar(xn, un, vn, fx, fy)
        puntos.append((un, vn))
        print(un, vn)
        return un, vn


def pintar(puntosx):
    '''Pinta la gráfica'''
    x1 = []
    y1 = []
    
    
    for i in puntosx:
        x1.append(i[0])
        y1.append(i[1])

    plt.plot(x1, y1)
    plt.show()

#main

x0 = float(input('Introduce la t inicial: ')) #punto inicial
u0 = float(input('Introduce la x inicial (x(t)): ')) #punto inicial
v0 = float(input("Introduce la y inicial (y(t)): ")) #punto inicial
xf = float(input('Introduce el extremo final: ')) #punto final
n = int(input('Número de divisiones: '))
h = (xf - x0)/n #intervalo pequeño
puntos = [] #lista de puntos

iterar(x0, u0, v0, funcionx, funciony)
pintar(puntos)


