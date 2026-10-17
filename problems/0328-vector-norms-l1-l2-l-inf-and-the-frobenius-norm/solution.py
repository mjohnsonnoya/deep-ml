import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here
    if (norm_type == 'frobenius'):
        if (arr.ndim != 2):
            raise ValueError("Must be 2D")
        
        frob = 0;
        for x in arr.flat:
            frob += x ** 2
        
        return float(np.sqrt(frob))
    
    elif (norm_type == 'l1'):
        l1 = 0;
        for x in arr.flat:
            l1 += abs(x)
        
        return float(l1)
    elif (norm_type == 'linf'):
        linf = 0
        for x in arr.flat:
            linf = max(linf, abs(x))
        
        return float(linf)

    elif (norm_type == "l2"):
        l2 = 0
        for x in arr.flat:
            l2 += abs(x) ** 2
        
        return float(np.sqrt(l2))

    
    else:
        raise ValueError("The provided norm_type is invalid.")

