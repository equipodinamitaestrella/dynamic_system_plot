import matplotlib.pyplot as plt
import numpy as np
from sympy import *
import sys

'''def f(ax):
    return ax*ax + 1'''

def generateVector(x0, x1, x2):
    """with open("formula.dat") as f:
        formula = f.readlines()
    formula_str = formula[0]"""
    
    file_flag = False
    equation_flag = False

    n = len(sys.argv)
    for i in range(n):
        if '-f' in sys.argv[i]:
            file_flag = True
            filename = sys.argv[i+1]
    
        if '-e' in sys.argv[i]:
            equation_flag = True
            formula_str = sys.argv[i+1]
    
    if file_flag:
        with open(filename) as f:
            formula = f.readlines()
            formula_str = formula[0]
            print("using file mode with", formula_str)
    
    if equation_flag:
        print("using equation mode with", formula_str)
    
    x = Symbol("x")
    y = sympify(formula_str)
    #yprime = y.diff(x)
    f = lambdify(x, y, "numpy")
    print(formula_str)

    vect1 = [x0]
    vect2 = [x1]
    vect3 = [x2]
    aux1 = float(x0)
    aux2 = float(x1)
    aux3 = float(x2)
    for i in range(7):
        aux1 = f(aux1)
        vect1.append(aux1)
        aux2 = f(aux2)
        vect2.append(aux2)
        aux3 = f(aux3)
        vect3.append(aux3)
    return vect1, vect2 , vect3, formula_str

def plott(vect1, vect2, vect3, title):
    fig, ax = plt.subplots()
    ax.plot(vect1, label = 'x = 0.1')
    ax.plot(vect2, label = 'x = 1')
    ax.plot(vect3, label = 'x = 10')
    ax.set_yscale('log')
    ax.set(xlabel = "i", ylabel = '$x_i$', title = title)
    ax.grid()
    fig.savefig(title)
    plt.show