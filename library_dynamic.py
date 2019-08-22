import numpy as np
from sympy import *
import sys

def generateVector(x0, x1, x2, formula_str): 
    x = Symbol("x")
    y = sympify(formula_str)
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
