from library1 import *

from matplotlib import pyplot as pyplt

if __name__ == "__main__":
	vectors = generateVector(0.1,1,10)
	plot(vectors[0], vectors[1], vectors[2])
	pyplt.show()
