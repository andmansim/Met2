import matplotlib.pyplot as plt
import numpy as np

#La función cambia con el ejercicio
#En el resultado coger el número que más se parezca al punto inicial dado
def funcion(x,y):
    return (-2*x*(np.exp(x**2)*y-1))/(np.exp(x**2))

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
def funcion3(x):
    return ((x**2) -1)/(np.exp(x**2))



#main
x0 = float(input('Introduce la x inicial: ')) #punto inicial
y0 = float(input('Introduce la y inicial: ')) #punto inicial
xf = float(input('Introduce el extremo final: ')) #punto final
n = int(input('Número de divisiones: '))
h = (xf - x0)/n #intervalo pequeño
puntos = [] #lista de puntos
puntos_solus=[] #lista de puntos de las soluciones particulares

iterar(x0, y0, funcion)
pintar(puntos)

#funciones particulares de la solución real
iterar_solu(x0, funcion1)
pintar(puntos_solus)
puntos_solus=[]
iterar_solu(x0, funcion2)
pintar(puntos_solus)
puntos_solus=[]
iterar_solu(x0, funcion3)
pintar(puntos_solus)


    


    
