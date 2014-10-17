## /file bruteforcelog.py
## /author Tatiana Bradley
## /brief Function to compute elliptic curve discrete logs by
##        brute force.

from primecurve import *

# Finds n where n * base = point
def bruteForceLog(base, point):
    modulus = base.curve.prime
    prev = PrimePoint.inf()
    for i in range(1, modulus ** 2):
        current = prev + base
        if (current == point):
            return i
        prev = current
