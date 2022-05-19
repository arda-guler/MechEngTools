import numpy as np

def solve_an_eqn():
    num_of_unknowns = int(input("Num. of unknowns:"))
    print("\n")

    coeff_matrix = []

    for i in range(num_of_unknowns):
        coeff_matrix.append([])
        for i2 in range(num_of_unknowns):
            coeff_matrix[i].append(float(input("Var #" + str(i2+1) + " for eqn. #" + str(i+1) + ":")))
        print("\n")

    soln_matrix = []

    for i in range(num_of_unknowns):
        soln_matrix.append(float(input("Sol. for eqn. #" + str(i+1) + ":")))

    print("\n")

    coeff_matrix = np.array(coeff_matrix)
    soln_matrix = np.array(soln_matrix)

    coeff_matrix_inv = np.linalg.inv(coeff_matrix)
    result_matrix = np.matmul(coeff_matrix_inv, soln_matrix)
    print("Solution:\n", result_matrix)

while True:
    solve_an_eqn()
