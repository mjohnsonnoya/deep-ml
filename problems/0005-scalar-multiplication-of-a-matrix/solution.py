def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	for r in range(len(matrix)):
		for c in range(len(matrix[0])):
			matrix[r][c] *= scalar
	
	return matrix