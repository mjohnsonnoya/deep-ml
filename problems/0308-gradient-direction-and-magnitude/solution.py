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
    magnitude = np.sqrt(sum(val ** 2 for val in gradient))

    if magnitude == 0:
        return {
        'magnitude': magnitude,
        'direction': gradient,
        'descent_direction': gradient
    }
    direction = [val/magnitude for val in gradient]
    descent_direction = [-1 * val for val in direction]

    return {
        'magnitude': magnitude,
        'direction': direction,
        'descent_direction': descent_direction
    }