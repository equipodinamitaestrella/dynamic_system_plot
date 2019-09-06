from library_dynamic import *
from library_plot import *
from help_file import *
from matplotlib import pyplot as pyplt
import numpy as np
import random

def parser(com_string): #com_string es el comando en sys.argv
    equation_flag = False
    a_flag = False
    b_flag = False
    n_flag = False
    x_flag = False
    i_flag = False
    dynamic = False
    noise_flag = False
    histo_flag = False
    split_string = com_string.split()

    for i in range(len(split_string)):
        if split_string[i] == '-e':
            equation_flag = True
            formula_str = split_string[i+1]
        elif split_string[i] == '-a' and a_flag == False:
            a_flag = True
            a = []
            a.append(float(split_string[i+1]))
            a.append(float(split_string[i+2]))
            a.append(float(split_string[i+3]))
        elif split_string[i] == '-b' and b_flag == False:
            b = []
            b.append(float(split_string[i+1]))
            b.append(float(split_string[i+2]))
            b.append(float(split_string[i+3]))
            b_flag = True
        elif split_string[i] == '-n' and n_flag == False:
            n = []
            n.append(float(split_string[i+1]))
            n.append(float(split_string[i+2]))
            n.append(float(split_string[i+3]))
            n_flag = True
        elif split_string[i] =='-x0' and x_flag == False:
            x = []
            x.append(float(split_string[i+1]))
            x.append(float(split_string[i+2]))
            x.append(float(split_string[i+3]))
            x_flag = True
        elif split_string[i] == '-i' and i_flag == False:
            itera = int(split_string[i+1])
            if itera > 7:
                itera = 7
                print("Notice: iteration value too big, maximum accepted value is 7 and has been set to 7")
            elif itera < 1:
                itera = 1
                print("Notice: iteration value too small, minimum accepted value is 1 and has been set to 1")
            i_flag = True
            if equation_flag == True:
                print("using equation mode with", formula_str)
        elif split_string[i] == '-d':
            dynamic = True
        elif split_string[i] == '-ns':
            noise = int(split_string[i+1])
            noise_flag=True
        elif split_string[i] == '-hs':
            histo_flag = True
            print("Histogram activated")
            histo = split_string[i+1]

    if equation_flag == False:
        helpf()
        exit()

    if histo_flag == True:
        histogr = (histo_flag, histo)
    else:
        histogr = (histo_flag, 0)

    if dynamic == True:
        print("Evaluating dynamic system")
    else:
        print("Evaluating function")

    if noise_flag == True:
        print("Inserting noise to equation", noise)
    else:
        noise = 0

    if a_flag == False:
        print("WARNING:")
        print("No -a flag found")
        print("a's default value set to 1")
        print("if you need help with the use of this software please type:")
        print("python main.py --help")
        a = 1

    if b_flag == False:
        print("WARNING:")
        print("No -b flag found")
        print("b's default value set to 1")
        print("if you need help with the use of this software please type:")
        print("python main.py --help")
        b = 1

    if n_flag == False:
        print("WARNING:")
        print("No -n flag found")
        print("a's default value set to 1")
        print("if you need help with the use of this software please type:")
        print("python main.py --help")
        n = 1

    if x_flag == False:
        print("WARNING:")
        print("No -x flag found")
        print("initial conditions set to default values set to 0.1, 1 and 10")
        print("if you need help with the use of this software please type:")
        print("python main.py --help")
        x0 = 0.1
        x1 = 1
        x2 = 10

    if i_flag == False:
        print("WARNING:")
        print("No -i flag found")
        print("i's default value set to 7")
        print("if you need help with the use of this software please type:")
        print("python main.py --help")
        itera = 7
    return formula_str, a, b, n, x, itera, dynamic, noise, histogr
    

if __name__ == "__main__":
    file_flag = False

    n = len(sys.argv)
    for i in range(n):
        if '-f' in sys.argv[i]:
            file_flag = True
            filename = sys.argv[i+1]
            
        elif '--help' in sys.argv[i] and file_flag == False:
            helpf()
            exit()

    if file_flag == True:
        with open(filename) as f:
            formula = f.readlines()
            formula_str, a, b, n, x, itera, dynamic, noise, histogr = parser(formula[0])
            print("using file mode with", formula_str)
            
    if file_flag == False:
        formula = " ".join(sys.argv[1:])
        formula_str, a, b, n, x, itera, dynamic, noise, histogr = parser(formula)

    formulae = generate_combinations(formula_str, a, b, n)
    xs = np.arange(x[0], x[1], x[2])
    if dynamic == True:
        vectors_ns = generateVector(xs, formulae, itera, noise)
        if histogr[0] == True:
            vectors = generateVector(xs, formulae, itera, 0)
    else:
        vectors_ns = generateVector(xs, formulae, 0, noise)
        if histogr[0] == True:
            vectors = generateVector(xs, formulae, 0, 0)
    #vector_grams = convert_to_unit(vectors, np.float64(1e-12))
    #vector_grams = convert_to_unit(vectors_ns, np.float64(1e-12))
    if histogr[0] == True:
        errors = errors_table(vectors, vectors_ns)

    title=formula_str+'_a_'+', '.join(map(str,a))+'_b_'+', '.join(map(str,b))+'_n_'+', '.join(map(str,n))+'_x0_'+', '.join(map(str,x))
    
    plott(xs, vector_grams, title)

    if histogr[0] == True:
        plot_histo(errors, histogr[1])
    pyplt.show()
