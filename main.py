from library_dynamic import *
from library_plot import *

from matplotlib import pyplot as pyplt

if __name__ == "__main__":
	vectors = generateVector(0.1,1,10)
	plott(vectors[0], vectors[1], vectors[2], vectors[3])
	pyplt.show()
