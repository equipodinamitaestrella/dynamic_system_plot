import matplotlib.pyplot as plt
import numpy as np

def plott(fig, ax, xs, cube, title):
	# cube must be a numpy arra
    dynamic=False
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
        ax.set_yscale('log')
        
    #mass=9.5*10**-13
    ax.set(xlabel = "hours", ylabel = 'mass (gr)', title = title)
    ax.grid()
    fig.savefig(title.replace('.',','))
    #plt.legend(loc='best', prop={'size': 6})
    #plt.show()

def plot_histo(fig, ax, errors, bins):
    fig, ax = plt.subplots(errors.shape[0],1)
    if errors.shape[0]==1:
        ax.hist(errors[0], bins=bins)
    else:
        for i in range(errors.shape[0]):
            ax[i].hist(errors[i], bins=bins)
    
def plot_observations(fig, ax, obs_z, obs_d, d_err):
    ax.errorbar(obs_z,obs_d, yerr=d_err, fmt='o')
