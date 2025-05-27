import numpy as np

# Define the matrix A and vector z
A = np.array([[8, 2], [2, 8]])
z = np.array([13.5, -22.5])

# Solve for the vector c
c = np.linalg.solve(A, z)

# Print the solution
print("The solution vector c is:", c)