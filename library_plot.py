import matplotlib.pyplot as plt
import numpy as np

def plott(xs, cube, title):
    dynamic=False
   # cube must be a numpy array
    fig, ax = plt.subplots()
    if len(cube.shape)==3:
        dynamic=True
    
    for i in range(len(cube)): # iterate over matrices each representing orbits with a single equations
        if dynamic:
            for j in range(len(cube[0])): # iterate over each orbit within the given matrix
                ax.plot(cube[i][j], label = 'x = %s'%(cube[i][j][0]))
        else:
            ax.plot(xs,cube[i])
    if dynamic:
        delta_time=3
        seconds=[i*3 for i in range(len(cube[0][0]))]
        plt.xticks(range(len(cube[0][0])),seconds)
        ax.set_yscale('symlog')
        
    #mass=9.5*10**-13
    ax.set(xlabel = "hours", ylabel = 'mass (gr)', title = title)
    ax.grid()
    fig.savefig(title.replace('.',','))
    #plt.legend(loc='best', prop={'size': 6})
    plt.show()
