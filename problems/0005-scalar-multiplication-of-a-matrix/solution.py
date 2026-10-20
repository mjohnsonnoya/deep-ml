def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	for row in range(len(matrix)):
		for col in range(len(matrix)):
			matrix[row][col] *= scalar

	return matrix