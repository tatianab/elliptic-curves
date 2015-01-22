"""
 /file examples.py
 /brief Some examples of curves, points and elements to play with.
"""

from primecurves import *

# A curve over a small prime field, and two points on
# that curve.
E = PrimeCurve(4, 20, 29)
P = PrimePoint(5, 22, E)
Q = PrimePoint(16, 27, E)
E.getAllPoints() # try getting all the points!

# An example that doesn't satisfy the curve.
NotAPoint = PrimePoint(1, 0, E)

A = PrimeFieldElement(3, 5)
B = PrimeFieldElement(4, 5)
EC = PrimeCurve(2,3,5)
P1 = PrimePoint.fromElements(A, B, EC)
A = E.getPoint()

# A curve with many more points
mod = 7919
E2 = PrimeCurve(1001, 75, mod)
P1 = PrimePoint(4023, 6036, E2)
Q1 = PrimePoint(4135, 3169, E2)
K = PrimePoint(1974, 2248, E2)

INF = PrimePoint.inf() # the point at infinity

# Some PrimeFieldElements
zero  = PrimeFieldElement(0, 5)
one   = PrimeFieldElement(1, 5)
two   = PrimeFieldElement(2, 5)
three = PrimeFieldElement(3, 5)
four  = PrimeFieldElement(4, 5)

# Trying Monnerat's example
E = PrimeCurve(373, 837, 1019)
P = PrimePoint(293, 914, E)
Q = PrimePoint(794, 329, E)
print P.computeLift()
print Q.computeLift()

