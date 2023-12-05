'''
Ahora es vectorial. Para las kij hemos cambiado las f por el vector u v prima, donde la
a y b dependen de xi, vi, ui y f(xi)
'''


import matplotlib.pyplot as plt
import numpy as np

def funcion(x, u, v, n):
    '''la función es y'' + a*y' + b*y = f(x)'''
    #donde a y b dependen de x
    #u(x)=y(x) y v(x)=y'(x)
    #sería (-b * u -a * v + f(x)) = y''(x),  donde sustituimos b, a y f(x)
    return (-n**2 *u - x * v)/(1-x**2)

def iterar(x, u, v, f): 
    '''Itera la función'''
    while x <= xf:
        #constantes (pesos)
        a1 = 1/6
        a2 = 1/3
        a3 = 1/3
        a4 = 1/6
        
        #Pendientes
        k11 = v
        k12 = f(x, u, v) 
        k21 = v + (h/2)*k11
        k22 = f(x +(h/2), u + (h/2)*k11, v + (h/2)*k12)
        k31 = v + (h/2)*k21
        k32 = f(x +(h/2), u + (h/2)*k21, v + (h/2)*k22)
        k41 = v + h*k31
        k42 = f(x +h, u + h*k31, v + h*k32)
        
        
        #función
        xn = x + h
        un = u + h*(a1*k11 + a2*k21 + a3*k31 + a4*k41)
        vn = v + h*(a1*k12 + a2*k22 + a3*k32 + a4*k42) 
        
        iterar(xn, un,vn, f)
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

#main
x0 = float(input('Introduce la x inicial: ')) #punto inicial
u0 = float(input('Introduce la u inicial (u = y(x)): ')) #punto inicial
v0 = float(input("Introduce la v inicial (v = y'(x)): ")) #punto inicial
xf = float(input('Introduce el extremo final: ')) #punto final
n = int(input('Número de divisiones: '))
h = (xf - x0)/n #intervalo pequeño
puntos = [] #lista de puntos

ene = float(input('Introduce el valor de n: '))
uu = (-1)**ene

def factorial(numero):
    resultado = 1
    for i in range(1, numero +1):
        resultado *= i
    return resultado

for m in range (0, int(ene/2)):
    sumatorio =sum((-1)**m *(factorial(ene - m - 1)/(factorial(m) * factorial(ene - 2*m-1))) * (-2)**(ene-2*m-1)) 
vv = (ene/2) * sumatorio

iterar(x0, uu, vv, funcion)
pintar(puntos)

