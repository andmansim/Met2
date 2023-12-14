#ES EL RUNGE KUTTA 4 PARA SISTEMAS DE ECUACIONES DIFERENCIALES

import matplotlib.pyplot as plt
import numpy as np

def funcionx(x, u, v):
    #Ponemos la función x'(t) que nos da el enunciado
    # u = x(t), v = y(t)
    return v

def funciony (x, u, v):
    #Ponemos la función y'(t) que nos da el enunciado
    #u= x(t) y v = y(t)
    return -u + u**2


def iterar(x, u, v, fx, fy):
    
    a1 = 1/6
    a2 = 1/3
    a3 = 1/3
    a4 = 1/6

    k11 = fx(x, u, v)
    k12 = fy(x, u, v)
    k21 = fx(x + (h/2), u + (h/2)*k11, v + (h/2)*k12)
    k22 = fy(x + (h/2), u + (h/2)*k11, v + (h/2)*k12)
    k31 = fx(x + (h/2), u + (h/2)*k21, v + (h/2)*k22)
    k32 = fy(x + (h/2), u + (h/2)*k21, v + (h/2)*k22)
    k41 = fx(x + h, u + h*k31, v + h*k32)
    k42 = fy(x + h, u + h*k31, v + h*k32)

    xn = x + h
    un = u + h*(a1*k11 + a2*k21 + a3*k31 + a4*k41)
    vn = v + h*(a1*k12 + a2*k22 + a3*k32 + a4*k42)
    
    return xn, un, vn

def pintar(puntosx):
    for i, punt in enumerate(puntosx):
        x = punto_inicial[0]
        y = punto_inicial[1]
        
        x_vals = [x]
        y_vals = [y]
        
        while x0 < xf:
            x, y = iterar(x_vals[-1], y_vals[-1] , funcionx, funciony)
            x_vals.append(x)
            y_vals.append(y)
            print(x, y)
            
        plt.plot(x_vals, y_vals, label=f'Punto inicial {i + 1}')
        
    plt.xlabel('x(t)')
    plt.ylabel('y(t)')
    plt.legend()
    plt.show()

# Main
x0 = float(input('Introduce la t inicial: '))
xf = float(input('Introduce el extremo final: '))

puntos_iniciales = []
control = True
while control:
    u0 = float(input('Introduce la x inicial (x(t)): '))
    v0 = float(input("Introduce la y inicial (y(t)): "))
    control = input('Quieres seguir poniendo puntos iniciales? (s/n): ')
    puntos_iniciales.append((u0, v0))
    if control.lower() != 's':
        control = False

n = int(input('Número de divisiones: '))
h = (xf - x0)/n
puntos = []
puntos_solu = []


pintar(puntos_iniciales)


