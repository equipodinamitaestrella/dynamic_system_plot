import matplotlib.pyplot as plt
import numpy as np
def generateVector(x0, x1, x2):
    vect1 = [x0]
    vect2 = [x1]
    vect3 = [x2]
    aux1 = float(x0)
    aux2 = float(x1)
    aux3 = float(x2)
    for i in range(7):
        aux1 = aux1**2 + 1
        vect1.append(aux1)
        aux2 = aux2**2 + 1
        vect2.append(aux2)
        aux3 = aux3**2 + 1
        vect3.append(aux3)
    return vect1, vect2 , vect3

def plot(vect1, vect2, vect3):
    """ax = plt.axes()
    plt.grid()
    
    plt.title("Plotting x = x^2 + 1")

    plt.plot(range(11), vect1)
    plt.plot(range(11), vect2)
    plt.plot(range(11), vect3)"""

    print(vect1, vect2, vect3)
    fig, ax = plt.subplots()
    ax.plot(vect1, label = 'x = 0.1')
    ax.plot(vect2, label = 'x = 1')
    ax.plot(vect3, label = 'x = 10')
    ax.set_yscale('log')
    ax.set(xlabel = "i", ylabel = '$x_i$', title = "Plot for x = x^2 + 1")
    ax.grid()
    fig.savefig("test.png")
    plt.show