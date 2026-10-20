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
    if norm_type == 'l1':
        l1 = 0
        for num in arr.reshape(-1):
            l1 += abs(num)
        
        return float(l1)
    
    elif norm_type == 'l2':
        l2 = 0
        for num in arr.reshape(-1):
            l2 += num ** 2

        return np.sqrt(l2)
    
    elif norm_type == 'linf':
        linf = 0;
        for num in arr.reshape(-1):
            linf = max(linf, abs(num))
        
        return float(linf)

    elif norm_type == 'frobenius':
        if (arr.ndim != 2):
            raise ValueError("array must be 2d");
        fro = 0
        for num in arr.reshape(-1):
            fro += num ** 2
        
        return np.sqrt(fro)
    else:
        raise ValueError("not a valid norm")
