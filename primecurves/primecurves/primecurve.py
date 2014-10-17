## /file primecurve.py
## /author Tatiana Bradley
## /brief Implementation of the PrimeCurve class.

from primepoint import *
from primefieldelement import *

class PrimeCurve:

    """
    " A class representing an elliptic curve
    " over a prime field
    "
    " Equation: y^2 = x^3 + ax + b
    " Underlying prime cannot be 2 or 3!
    """

    """
    " DATA:
    " PrimeFieldElements _a,_b - the parameters of the eq'n
    " int _prime - the underlying prime
    "
    """

    # CONSTRUCTOR

    def __init__(self, a, b, prime):
        self.a = a;
        self.b = b;
        self.prime = prime;
        self.allPoints = [PrimePoint.inf()];
        self.order = None

    @classmethod
    def default(cls):
        return cls(0, 0, 0)

    # PRINT FUNCTION

    def __repr__(self):
        return "y^2 = x^3 + " + str(self.a) + "x + " + str(self.b) + " over F_" + str( self.prime )


    # OTHER FUNCTIONS
    def onCurve(self, x, y):
        x = PrimeFieldElement(x, self.prime)
        y = PrimeFieldElement(y, self.prime)
        lhs = y ** 2
        rhs = x ** 3 + x * self.a + self.b
        return (lhs == rhs)
    
    # GET A "RANDOM" POINT (prelim)
    def getPoint(self):
        found = False
        while (not found):
            x = PrimeFieldElement.random(self.prime).value
            for y in range(self.prime):
                if (self.onCurve(x, y)):
                    return PrimePoint(x, y, self)

    # GET ALL THE POINTS!
    def getAllPoints(self):
        for x in range(self.prime):
            for y in range(self.prime):
                if (self.onCurve(x, y)):
                    self.allPoints += [ PrimePoint(x, y, self) ]

    def getOrder(self):
        if self.order is None:
            if len(self.allPoints) > 1:
                self.order = len(self.allPoints)
            else:
                return "NO INFO"
                # ^ NEEDS TO BE MODIFIED
        return self.order
