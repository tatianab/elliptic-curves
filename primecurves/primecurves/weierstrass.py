"""
    \file weierstrass.py
    \author Tatiana Bradley
    \brief A class representing a full weierstrass equation.
           **Should perhaps be merged with prime curve eventually.
"""

class Weierstrass:

    """
    " DATA:
    " params a1, a2, a3, a4, a6
    " EQ'N: y^2 + a1(xy) + a3(y) = x^3 + a2(x^2) + a4(x) + a6
    " prime (F_p is the underlying field)
    "
    """"

    """ CONSTRUCTOR """
    def __init__(self, a1, a2, a3, a4, a6, prime):
        self.a1    = a1
        self.a2    = a2
        self.a3    = a3
        self.a4    = a4
        self.a6    = a6
        self.prime = prime


    # OTHER FUNCTIONS
    def computeLift(x, y):
        pass
    

    

    
