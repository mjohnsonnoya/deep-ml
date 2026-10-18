def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if (len(a[0]) != len(b)):
		return -1

	answer = []
	for row in range(len(a)):
		dot_product = 0
		for col in range(len(a[0])):
			dot_product += a[row][col] * b[col]
	
		answer.append(dot_product)
	
	return answer
