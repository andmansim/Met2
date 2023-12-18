import matplotlib.pyplot as plt
import numpy as np

#La función cambia con el ejercicio
#En el resultado coger el número que más se parezca al punto inicial dado
def funcion(x,y):
    #es despejar y'(x)
    return y - x**2 +1 

def funcion_particular (x, c):
    #Ponemos la solución de la edo con la C sacada en dicho punto
    return (x + 1)**2 + (c * np.exp(x))

def iterar(x, y, f): 
    '''Itera la función'''
    
    if x > xf:
        return [(x, y)]
  
    xn = x + h
    yn = y + h * f (x,y)
    #iterar(xn, yn, f)
    #puntos1.append((xn, yn))
    print(xn, yn)
    #return xn, yn
    return [(x, y)] + iterar(xn, yn, f)



#Código para pintar las soluciones particulares de la solución real
def iterar_solu(x,f, c): 
    '''Itera la función'''
    
    if x > xf:
        return [(x, f(x, c))]
    
    xn = x + h
    yn =  h * f (x, c)
    #iterar_solu(xn, f)
    #puntos_solus_part.append((xn, yn))
    print(xn, yn)
    return [(x, f(x, c))] + iterar_solu(xn, f, c)



def pintar(puntos):
    '''Pinta la gráfica'''
    if isinstance(puntos[0], tuple):
        # Si hay solo un punto, lo convertimos en una lista de un solo elemento
        puntos = [puntos]

    for i, puntos_funcion in enumerate(puntos):
        x = [j[0] for j in puntos_funcion]
        y = [j[1] for j in puntos_funcion]
        plt.plot(x, y, label=f'Función {i+1}')

    plt.legend()
    plt.show()

#main
puntos = [] #lista de puntos
puntos_solus = [] #lista de puntos de las soluciones particulares
xf = float(input('Introduce el extremo final: ')) #punto final
n = int(input('Número de divisiones: '))

for i in range(1, 4):
    puntos1 = []
    print(f'Punto inicial {i}')
    x0 = float(input('Introduce la x inicial: ')) #punto inicial
    y0 = float(input('Introduce la y inicial: ')) #punto inicial
    h = (xf - x0)/n #intervalo pequeño
    puntos.append(iterar(x0, y0, funcion))

#función real
pintar(puntos)

#funciones particulares de la solución real
for i in range(1, 4):
    puntos_solus1 = []
    print('Soluciones particulares')
    print(f'C {i}')
    x0 = float(input('Introduce la x inicial: ')) #punto inicial
    c = float(input('Introduce la constante C: '))
    puntos_solus.append(iterar_solu(x0, funcion_particular, c))
    
pintar(puntos_solus)




    


    
