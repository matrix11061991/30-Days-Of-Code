from sympy import * 
def diagonalization(M):
	return M.diagonalize()

M = Matrix([[3, -2, 4, -2],
	[5, 3, -3, -2],
	[5, -2, 2, -2],
	[5, -2, -3, 3]])

print(diagonalization(M))
