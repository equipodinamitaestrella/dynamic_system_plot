import numpy as np
from sympy import *
import sys

def generateVector(x, formulae, itera): 
    # formalae must be a lambdified sympy expression
    # x must be a list of lenght 3 with initial value, last value and step respectively
    # this function returns a cube where each matrix contains all the iterations with a given expression and each row within a matrix contains the iterations of a particular initial condition
    cube=[]
    for eq in formulae:
        eq_matrix=[]
        for x0 in np.arange(x[0],x[1],x[2]):
            vect1 = [float(x0)]
            aux1 = float(x0)

            for i in range(itera):
                aux1 = eq(aux1)
                vect1.append(aux1)
            eq_matrix.append(vect1)
        cube.append(eq_matrix)
        
    return cube

def dynamic_system(eq_str, a, b, n):
    # eq_str must have a, b and n integers or floting point values to insert into the expression

    eq_str=eq_str.replace('a', str(a))
    eq_str=eq_str.replace('b', str(b))
    eq_str=eq_str.replace('n', str(n))
    x = Symbol("x")
    y = sympify(eq_str)
    f = lambdify(x, y, "numpy")
    
    return f

def generate_combinations(eq_str,a,b,n):
    # this function returns a list of all the possible lambdified sympy expressions to be generated from the input parameter values
    # a, b and n need to be lists of lenght 3 where the first index contains the starting value, the second one contains the last value and the third index indicates the step to be taken
    
    equations=[]
    
    for a0 in np.arange(a[0],a[1],a[2]):
        for b0 in np.arange(b[0],b[1],b[2]):
            for n0 in np.arange(n[0],n[1],n[2]):
                equations.append(dynamic_system(eq_str,a0,b0,n0))

    return equations
