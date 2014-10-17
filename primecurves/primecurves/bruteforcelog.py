"""
 /file bruteforcelog.py
 /author Tatiana Bradley
 /brief Compute elliptic curve discrete logs by
        brute force (enumeration).
"""

from primecurve import *

"""
bruteForceLog()
Computes the discrete log for prime curves
by brute force, i.e., does an exhaustive search.

INPUTS: base, the base point
        point, which is base * some n
OUTPUTS: n where n * base = point,
         or "No log found" if point is
         not a multiple of base
"""
def bruteForceLog(base, point):
    modulus = base.curve.prime
    prev = PrimePoint.inf()           # Start out at INF (analogous to 0)
    for i in range(1, modulus ** 2):  # Loop over possible n's, stopping
        current = prev + base         # if log is found.
        if (current == point):
            return i
        prev = current
    print "No log found"
