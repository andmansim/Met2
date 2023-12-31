import matplotlib.pyplot as plt
import numpy as np

#Las funciones no se modifican, solo se pone los datos que pide en la terminal 

def funcionx(x, u, v):
    #Es la función de x'(t) = p*u -q*u*v
    # u = x(t), v = y(t)
    return p*u - q*u*v

def funciony (x, u, v):
    #Es la función de y'(t) = -r*v + s*u*v
    #u= x(t) y v = y(t)
    return -r*v + s*u*v

def iterar(x, u, v, fx, fy): 
    '''Itera la función'''
    if x > xf:
        return x, u, v
    
    #constantes (pesos)
    a1 = 1/6
    a2 = 1/3
    a3 = 1/3
    a4 = 1/6
    
    #Pendientes
    k11 = fx(x, u, v) 
    k12 = fy(x, u, v) 
    k21 = fx(x +(h/2), u + (h/2)*k11, v + (h/2)*k12)
    k22 = fy(x +(h/2), u + (h/2)*k11, v + (h/2)*k12)
    k31 = fx(x +(h/2), u + (h/2)*k21, v + (h/2)*k22)
    k32 = fy(x +(h/2), u + (h/2)*k21, v + (h/2)*k22)
    k41 = fx(x + h, u + h*k31, v + h*k32)
    k42 = fy(x + h, u + h*k31, v + h*k32)
    
    
    #función
    xn = x + h
    un = u + h*(a1*k11 + a2*k21 + a3*k31 + a4*k41)
    vn = v + h*(a1*k12 + a2*k22 + a3*k32 + a4*k42) 
    
    iterar(xn, un, vn, fx, fy)
    puntos.append((xn, un, vn))
    
    print('Datos de los conejos',xn, un)
    print('Datos de los zorros', xn, vn)
    
    return xn, un, vn

def pintar(puntos):
    '''Pinta la gráfica'''
    x1 = []
    y1 = []
    y2 = []
    
    for i in puntos:
        x1.append(i[0])
        y1.append(i[1])
        y2.append(i[2])
        
        
    plt.plot(x1, y1)
    plt.plot(x1, y2)
    plt.show()

#main
#Para lo de los conejos y zorros
r = float(input('Introduce r: '))
s = float(input('Introduce s: '))
p = float(input('Introduce p: '))
q = float(input('Introduce q: '))

x0 = float(input('Introduce la t inicial: ')) #punto inicial
u0 = float(input('Introduce la x inicial (x(t)): ')) #punto inicial
v0 = float(input("Introduce la y inicial (y(t)): ")) #punto inicial
xf = float(input('Introduce el extremo final: ')) #punto final
n = int(input('Número de divisiones: '))
h = (xf - x0)/n #intervalo pequeño
puntos = [] #lista de puntos
iterar(x0, u0, v0, funcionx, funciony)
pintar(puntos)


