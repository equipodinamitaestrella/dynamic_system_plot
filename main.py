from library_dynamic import *
from library_plot import *
from help_file import *
from matplotlib import pyplot as pyplt

if __name__ == "__main__":
    file_flag = False
    equation_flag = False

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
	
    if file_flag == False and equation_flag == False:
        helpf()
        exit()

    if file_flag:
        with open(filename) as f:
            formula = f.readlines()
            formula_str = formula[0]
            print("using file mode with", formula_str)
    
    if equation_flag:
        print("using equation mode with", formula_str)

    formulae = dynamic_system(formula_str, 1, 1, 1)
    vectors = generateVector(0.1,1,10, formulae)
    plott(vectors[0], vectors[1], vectors[2], formula_str)
    pyplt.show()
