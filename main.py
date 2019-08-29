from library_dynamic import *
from library_plot import *
from help_file import *
from matplotlib import pyplot as pyplt

if __name__ == "__main__":
    file_flag = False
    equation_flag = False
    a_flag = False
    b_flag = False
    n_flag = False
    x_flag = False
    i_flag = False

    n = len(sys.argv)
    for i in range(n):
        if '-f' in sys.argv[i]:
            file_flag = True
            filename = sys.argv[i+1]

        elif '-e' in sys.argv[i]:
            equation_flag = True
            formula_str = sys.argv[i+1]
        
        elif '--help' in sys.argv[i] and file_flag == False and equation_flag == False:
            helpf()
            exit()

        elif '-a' in sys.argv[i] and a_flag == False:
            a =  sys.argv[i+1]
            a_flag = True

        elif '-b' in sys.argv[i] and b_flag == False:
            b =  sys.argv[i+1]
            b_flag = True

        elif '-n' in sys.argv[i] and n_flag == False:
            n =  sys.argv[i+1]
            n_flag = True

        elif '-x0' in sys.argv[i] and x_flag == False:
            x0 = float(sys.argv[i+1])
            x1 = float(sys.argv[i+2])
            x2 = float(sys.argv[i+3])
            x_flag = True
            print("si entre")

        elif '-i' in sys.argv[i] and i_flag == False:
            itera = int(sys.argv[i+1])
            if itera > 7:
                itera = 7
                print("Notice: iteration value too big, maximum accepted value is 7 and has been set to 7")
            elif itera < 1:
                itera = 1
                print("Notice: iteration value too small, minimum accepted value is 1 and has been set to 1")
            i_flag = True
	
    if file_flag == False and equation_flag == False:
        helpf()
        exit()

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

    if file_flag:
        with open(filename) as f:
            formula = f.readlines()
            formula_str = formula[0]
            print("using file mode with", formula_str)
    
    if equation_flag:
        print("using equation mode with", formula_str)

    formulae = dynamic_system(formula_str, a, b, n)
    vectors = generateVector(x0,x1,x2, formulae, itera)
    title=formula_str+'_a'+str(a)+'_b'+str(b)+'_n'+str(n)+'_x0'+str(x0)+'_'+str(x1)+'_'+str(x2) 
    
    plott(vectors[0], vectors[1], vectors[2], title)
    pyplt.show()
