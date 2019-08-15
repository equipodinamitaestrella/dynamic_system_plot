import matplotlib.pyplot as plt
def generateVector(x0, x1, x2):
    vect1 = [x0]
    vect2 = [x1]
    vect3 = [x2]
    aux1 = x0
    aux2 = x1
    aux3 = x2
    for i in range(10):
        aux1 = aux1**2 + 1
        vect1.append(aux1)
        aux2 = aux2**2 + 1
        vect2.append(aux1)
        aux3 = aux3**2 + 1
        vect3.append(aux1)
    return vect1, vect2 , vect3

def plot(vect1, vect2, vect3):
    #ax = plt.axes()
    plt.grid()
    
    plt.title("Plotting x = x^2 + 1")

    plt.plot(range(11), vect1)
    plt.plot(range(11), vect2)
    plt.plot(range(11), vect3)
