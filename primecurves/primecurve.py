## /file primecurve.py
## /author Tatiana Bradley
## /brief Implementation of the PrimeCurve class.

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

    @classmethod
    def default(cls):
        return cls(0, 0, 0)

    # PRINT FUNCTION

    def __repr__(self):
        return "y^2 = x^3 + " + str(self.a) + "x + " + str(self.b) + " over F_" + str( self.prime )
