import matplotlib.pyplot as plt

def plott(vect1, vect2, vect3, title):
    fig, ax = plt.subplots()
    ax.plot(vect1, label = 'x = %s'%(vect1[0]))
    ax.plot(vect2, label = 'x = %s'%(vect2[0]))
    ax.plot(vect3, label = 'x = %s'%(vect3[0]))
    ax.set_yscale('symlog')
    ax.set(xlabel = "i", ylabel = '$x_i$', title = title)
    ax.grid()
    fig.savefig(title.replace('.',','))
    plt.legend(loc='best')
    plt.show
