from library_dynamic import *
from library_plot import *

from matplotlib import pyplot as pyplt

if __name__ == "__main__":
    file_flag = False
    equation_flag = False

    n = len(sys.argv)
    for i in range(n):
        if '-f' in sys.argv[i]:
            file_flag = True
            filename = sys.argv[i+1]
    
        if '-e' in sys.argv[i]:
            equation_flag = True
            formula_str = sys.argv[i+1]
    
    if file_flag:
        with open(filename) as f:
            formula = f.readlines()
            formula_str = formula[0]
            print("using file mode with", formula_str)
    
    if equation_flag:
        print("using equation mode with", formula_str)

    vectors = generateVector(0.1,1,10, formula_str)
    plott(vectors[0], vectors[1], vectors[2], vectors[3])
    pyplt.show()
