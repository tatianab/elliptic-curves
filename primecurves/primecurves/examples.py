## Prime Curves Examples
from primecurves import *

## EXAMPLES
E = PrimeCurve(4, 20, 29)
P = PrimePoint(5, 22, E)
Q = PrimePoint(16, 27, E)
E.getAllPoints()

NotAPoint = PrimePoint(1, 0, E)

A = PrimeFieldElement(3, 5)
B = PrimeFieldElement(4, 5)
EC = PrimeCurve(2,3,5)
P1 = PrimePoint.fromElements(A, B, EC)
A = E.getPoint()

mod = 7919
E2 = PrimeCurve(1001, 75, mod)
P1 = PrimePoint(4023, 6036, E2)
Q1 = PrimePoint(4135, 3169, E2)

K = PrimePoint(1974, 2248, E2)

INF = PrimePoint.inf() # testing the point at infinity
