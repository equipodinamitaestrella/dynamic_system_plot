from library_dynamic import *
from library_plot import *
from help_file import *
from matplotlib import pyplot as pyplt
import numpy as np

def file_parser(file_string):
    equation_flag = False
    a_flag = False
    b_flag = False
    n_flag = False
    x_flag = False
    i_flag = False

    split_string = file_string.split()

    for i in range(len(split_string)):
        if split_string[i] == '-e':
            equation_flag = True
            formula_str = split_string[i+1]
        elif split_string[i] == '-a':
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
    
    return formula_str, a, a_flag, b, b_flag, n, n_flag, x, x_flag, itera, i_flag 
    

if __name__ == "__main__":
    file_flag = False
    equation_flag = False
    a_flag = False
    b_flag = False
    n_flag = False
    x_flag = False
    i_flag = False
    file_flag_avoid = False

    n = len(sys.argv)
    for i in range(n):
        if '-f' in sys.argv[i]:
            file_flag = True
            filename = sys.argv[i+1]
            file_flag_avoid = True

        elif '-e' in sys.argv[i]:
            equation_flag = True
            formula_str = sys.argv[i+1]
        
        elif '--help' in sys.argv[i] and file_flag == False and equation_flag == False:
            helpf()
            exit()

        elif '-a' in sys.argv[i] and a_flag == False:
            a = []
            a.append(float(sys.argv[i+1]))
            a.append(float(sys.argv[i+2]))
            a.append(float(sys.argv[i+3]))
            a_flag = True

        elif '-b' in sys.argv[i] and b_flag == False:
            b = []
            b.append(float(sys.argv[i+1]))
            b.append(float(sys.argv[i+2]))
            b.append(float(sys.argv[i+3]))
            b_flag = True

        elif '-n' in sys.argv[i] and n_flag == False:
            n = []
            n.append(float(sys.argv[i+1]))
            n.append(float(sys.argv[i+2]))
            n.append(float(sys.argv[i+3]))
            n_flag = True

        elif '-x0' in sys.argv[i] and x_flag == False:
            x = []
            x.append(float(sys.argv[i+1]))
            x.append(float(sys.argv[i+2]))
            x.append(float(sys.argv[i+3]))
            x_flag = True

        elif '-i' in sys.argv[i] and i_flag == False:
            itera = int(sys.argv[i+1])
            if itera > 7:
                itera = 7
                print("Notice: iteration value too big, maximum accepted value is 7 and has been set to 7")
            elif itera < 1:
                itera = 1
                print("Notice: iteration value too small, minimum accepted value is 1 and has been set to 1")
            i_flag = True
	
    if file_flag == True:
        with open(filename) as f:
            formula = f.readlines()
            formula_str, a, a_flag, b, b_flag, n, n_flag, x, x_flag, itera, i_flag = file_parser(formula[0])
            print("using file mode with", formula_str)
    
    if equation_flag == True and file_flag_avoid == False:
        print("using equation mode with", formula_str)


    if file_flag == False and equation_flag == False:
        helpf()
        exit()

    if a_flag == False and file_flag_avoid == False:
        print("WARNING:")
        print("No -a flag found")
        print("a's default value set to 1")
        print("if you need help with the use of this software please type:")
        print("python main.py --help")
        a = 1

    if b_flag == False and file_flag_avoid == False:
        print("WARNING:")
        print("No -b flag found")
        print("b's default value set to 1")
        print("if you need help with the use of this software please type:")
        print("python main.py --help")
        b = 1

    if n_flag == False and file_flag_avoid == False:
        print("WARNING:")
        print("No -n flag found")
        print("a's default value set to 1")
        print("if you need help with the use of this software please type:")
        print("python main.py --help")
        n = 1

    if x_flag == False and file_flag_avoid == False:
        print("WARNING:")
        print("No -x flag found")
        print("initial conditions set to default values set to 0.1, 1 and 10")
        print("if you need help with the use of this software please type:")
        print("python main.py --help")
        x0 = 0.1
        x1 = 1
        x2 = 10

    if i_flag == False and file_flag_avoid == False:
        print("WARNING:")
        print("No -i flag found")
        print("i's default value set to 7")
        print("if you need help with the use of this software please type:")
        print("python main.py --help")
        itera = 7

    formulae = generate_combinations(formula_str, a, b, n)
    vectors = generateVector(x, formulae, itera)
    title=formula_str+'_a_'+', '.join(map(str,a))+'_b_'+', '.join(map(str,b))+'_n_'+', '.join(map(str,n))+'_x0_'+', '.join(map(str,x))
    
    plott(vectors, title)
    pyplt.show()
