import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	magnitude = float(np.sqrt(sum([val ** 2 for val in gradient])))

	return {
		"magnitude": magnitude,
		"direction": [val / magnitude for val in gradient] if magnitude != 0 else gradient,
		"descent_direction": [-val / magnitude for val in gradient] if magnitude != 0 else gradient
	}