import numpy as np
from sympy import *
import sys

def generateVector(x0, x1, x2, formulae): 
    # formalae must be a lambdified sympy expression
    
    vect1 = [x0]
    vect2 = [x1]
    vect3 = [x2]
    aux1 = float(x0)
    aux2 = float(x1)
    aux3 = float(x2)
    for i in range(7):
        aux1 = formulae(aux1)
        vect1.append(aux1)
        aux2 = formulae(aux2)
        vect2.append(aux2)
        aux3 = formulae(aux3)
        vect3.append(aux3)
    return vect1, vect2 , vect3

def dynamic_system(eq_str, a, b, n):
    # eq_str must have a, b y n integers or floting point values to insert into the expression

    eq_str=eq_str.replace('a', str(a))
    eq_str=eq_str.replace('b', str(b))
    eq_str=eq_str.replace('n', str(n))
    x = Symbol("x")
    y = sympify(eq_str)
    f = lambdify(x, y, "numpy")
    
    return f
