import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    def polynomial(coeffs: list):
        total = 0
        for i, num in enumerate(reversed(coeffs)):
            total += num * (x ** i)

        return total

    def derivative(coeffs: list):
        total = 0
        for i, num in enumerate(reversed(coeffs)):
            if i == 0:
                continue
            else:                
                total += i * num * (x ** (i - 1))
        
        return total

    numerator = (derivative(g_coeffs) * polynomial(h_coeffs) - derivative(h_coeffs) * polynomial(g_coeffs))

    denominator = polynomial(h_coeffs) ** 2

    return numerator/denominator