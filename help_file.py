def helpf():
    print("Dynamic System Plot Help\n")
    print("This program plots any equation the user gives as a parameter along with a range of coeficients and a range of initial conditions, x0. Also, the user must provide the number of iterations the system will do.")
    print("To run this program, please execute:")
    print("python3 main.py <flag> <parameter> <flag> <parameter> ... <flag> <parameter>\n")
    print("FLAGS:")
    print("\t-e : Equation. This flag receives an equation as a parameter (e.g. ax**n + b), also the user must provide the equation's coeficients using the following flags(-a, -b, -n) and the initial conditions of the system using flag -x0. Parameters must be separated by a blank space.")
    print("\t-a : Coeficient a. This flag receives 3 parameters, which are a range for a's values: start, end and step. Range is NOT inclusive on the right limit. It must be separated by a blank space.")
    print("\t-b : Coeficient b. This flag receives 3 parameters, which are a range for b's values: start, end and step. Range is NOT inclusive on the right limit. It must be separated by a blank space.")
    print("\t-n : Coeficient n. This flag receives 3 parameters. which are a range for n's values: start, end and step. Commonly used to indicate the power of 'x'. Range is NOT inclusive on the right limit. It must be separated by a blank space.")
    print("\t-i : Iterations. This flag receives 1 parameter, which is the number of iterations the system will do. It must be at least 1 and a maximum of 7.")
    print("\t-x0 : Initial conditions. This flag receives 3 parameters, user must provide the start, end and step of the range. Range is NOT inclusive on the right limit. It must be separated by a blank space.")
    print("\t-f : File. This flag receives a file name as a parameter. File must contain input values with its proper format specified in this guide.")
    print("\t--help : Help. This flag shows a detailed user guide to run 'Dynamic System Plot'.")


