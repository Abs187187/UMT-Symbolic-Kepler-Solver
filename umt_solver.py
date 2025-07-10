import math
import numpy as np

def umt_elliptical(M, e, terms=30):
    """
    UMT Symbolic Solver for Kepler's Equation (Elliptical)
    M: mean anomaly [radians]
    e: eccentricity (e < 1)
    terms: number of harmonic terms in the expansion
    Returns eccentric anomaly E [radians]
    """
    # Use math.factorial here, NOT np.math.factorial
    E0 = M + sum((e**k / math.factorial(k)) * np.sin(k*M) for k in range(1, terms+1))
    E1 = E0 - (E0 - e*np.sin(E0) - M) / (1 - e*np.cos(E0))
    for _ in range(2):
        E1 = E1 - (E1 - e*np.sin(E1) - M) / (1 - e*np.cos(E1))
    return E1

import math
import numpy as np

def umt_elliptical(M, e, terms=30):
    """
    UMT Symbolic Solver for Kepler's Equation (Elliptical)
    M: mean anomaly [radians]
    e: eccentricity (e < 1)
    terms: number of harmonic terms in the expansion
    Returns eccentric anomaly E [radians]
    """
    # Use math.factorial here, NOT np.math.factorial
    E0 = M + sum((e**k / math.factorial(k)) * np.sin(k*M) for k in range(1, terms+1))
    E1 = E0 - (E0 - e*np.sin(E0) - M) / (1 - e*np.cos(E0))
    for _ in range(2):
        E1 = E1 - (E1 - e*np.sin(E1) - M) / (1 - e*np.cos(E1))
def umt_hyperbolic(M, e):
    """
    UMT Symbolic Solver for Hyperbolic Kepler's Equation
    """
    if abs(M) < 1.0:
        H0 = M / e
    else:
        H0 = np.log(2 * abs(M) / e + 1.8) * np.sign(M)
    H1 = H0 - (e*np.sinh(H0) - H0 - M) / (e*np.cosh(H0) - 1)
    H = H1
    for _ in range(2):
        H = H - (e*np.sinh(H) - H - M) / (e*np.cosh(H) - 1)
    return H  # <--- this must be at the same indentation as the 'for' loop above
