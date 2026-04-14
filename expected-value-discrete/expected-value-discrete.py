import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    if np.abs(sum(p) - 1) > 1e-6:
        raise ValueError
    return np.average(x, weights=p)
