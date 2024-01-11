import matplotlib.pyplot as plt
import numpy as np

#ES EL MET DE EULER PERO NO PINTA LAS SOLUCIONES PARTICULARES, SOLO LA REAL

#La función cambia con el ejercicio
#En el resultado coger el número que más se parezca al punto inicial dado
def funcion(x,y):
    #es despejar y'(x)
    return -2*x * (np.exp(x**2)*y - 1)/(np.exp(x**2))

def iterar(x, y, f): 
    '''Itera la función'''
    
    if x > xf:
        return x, y
  
    xn = x + h
    yn = y + h * f (x,y)
    iterar(xn, yn, f)
    puntos.append((xn, yn))
    print(xn, yn)
    return xn, yn
    



#Código para pintar las soluciones particulares de la solución real
def iterar_solu(x,f): 
    '''Itera la función'''
    
    if x > xf:
        return x
    
    xn = x + h
    yn =  h * f (x)
    iterar_solu(xn, f)
    puntos_solus.append((xn, yn))
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
puntos = [] #lista de puntos
puntos_solus = [] #lista de puntos de las soluciones particulares
xf = float(input('Introduce el extremo final: ')) #punto final
n = int(input('Número de divisiones: '))

x0 = float(input('Introduce la x inicial: ')) #punto inicial
y0 = float(input('Introduce la y inicial: ')) #punto inicial
h = (xf - x0)/n #intervalo pequeño
iterar(x0, y0, funcion)
#función real
pintar(puntos)


