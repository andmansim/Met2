import matplotlib.pyplot as plt
import numpy as np

#La función cambia con el ejercicio
#En el resultado coger el número que más se parezca al punto inicial dado
def funcion(x,y):
    #es despejar y'(x)
    return y - x**2 +1 

def funcion_particular1 (x):
    #Ponemos la solución de la edo con la C sacada en dicho punto
    return (x + 1)**2 + ((-0.5) * np.exp(x))

def funcion_particular2 (x):
    return (x + 1)**2 + ((-1) * np.exp(x))

def funcion_particular3 (x):
    return (x + 1)**2 + ((-2) * np.exp(x))

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

#funciones particulares de la solución real
iterar_solu(x0, funcion_particular1)  
pintar(puntos_solus)

puntos_solus = []
iterar_solu(x0, funcion_particular2)  
pintar(puntos_solus)

puntos_solus = []
iterar_solu(x0, funcion_particular3)  
pintar(puntos_solus)
