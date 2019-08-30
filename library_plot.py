import matplotlib.pyplot as plt

def plott(cube, title):
    fig, ax = plt.subplots()
    
    for i in range(len(cube)): # iterate over matrices each representing orbits with a single equations
        for j in range(len(cube[0])): # iterate over each orbit within the given matrix
            ax.plot(cube[i][j], label = 'x = %s'%(cube[i][j][0]))
    delta_time=3
    seconds=[i*3 for i in range(len(cube[0][0]))]
    ax.set_yscale('symlog')
    ax.set(xlabel = "hours", ylabel = '$x_i$', title = title)
    plt.xticks(range(len(cube[0][0])),seconds)
    ax.grid()
    fig.savefig(title.replace('.',','))
    #plt.legend(loc='best', prop={'size': 6})
    plt.show()
