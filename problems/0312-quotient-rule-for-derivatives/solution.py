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
        res = 0
        for i, coeff in enumerate(reversed(coeffs)):
            res += coeff * x ** i

        return res
    
    def polynomial_prime(coeffs: list):
        res = 0
        for i, coeff in enumerate(reversed(coeffs)):
            if i != 0:
                res += coeff * i * x ** (i - 1)
        return res
    
    h = polynomial(h_coeffs)
    g = polynomial(g_coeffs)

    h_prime = polynomial_prime(h_coeffs)
    g_prime = polynomial_prime(g_coeffs)

    return (g_prime * h - g * h_prime) / h**2
    
