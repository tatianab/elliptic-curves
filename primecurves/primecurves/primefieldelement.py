## /file primefieldelement.py
## /author Tatiana Bradley
## /brief Implementation of the PrimeFieldElement class

from random import randrange

class PrimeFieldElement:
    """
    A class representing elements of a prime field.
    """

##    DATA MEMBERS: 
##    int value
##    int prime

    # CONSTRUCTORS
    def __init__(self, value, prime):
        if (prime == 0):
            self.value = value
            self.prime = prime
        else:
            self.value = value % prime
            self.prime = prime
            
    @classmethod
    def default(cls):
        return cls(0,0)

    # Construct as a random element
    @classmethod
    def random(cls, prime):
        value = randrange(1, prime)
        return cls(value, prime)

    # PRINT FUNCTION
    def __repr__(self):
        return str(self.value)

    # COMPARISON OPERATORS
    def __cmp__(self, other):
        other = self.toPFE(other)
        return cmp(self.value, other.value)

    def sameField(self, other):
        return ( self.prime == other.prime )

    def isDefault(self):
        return (self.prime == 0)

    # BINARY OPERATORS
    def __add__(self, other):
        other = self.toPFE(other)
        return PrimeFieldElement(self.value + other.value,
                                     self.prime)

    def __sub__(self, other):
        other = self.toPFE(other)
        return PrimeFieldElement(self.value - other.value,
                                     self.prime)
        
    def __mul__(self, other):
        other = self.toPFE(other)
        return PrimeFieldElement(self.value * other.value,
                                     self.prime)

    def __pow__(self, power):
        result = self.toPFE(1)
        for i in range(power):
            result = result * self
        return result

    def __div__(self, other):
        return self * other.inverse()

    # UNARY OPERATORS
    def __neg__(self):
        return PrimeFieldElement( -self.value, self.prime )

    def inverse(self):
        
        u = self.value
        v = self.prime

        x1 = 1
        x2 = 0

        while (u != 1):
            q = v // u
            r = v - q*u
            x = x2 - q*x1

            v = u
            u = r
            x2 = x1
            x1 = x

        return self.toPFE(x1)

    # OTHER FUNCTIONS

    def toPFE(self, other):
        if isinstance(other, (int, long)):
            return PrimeFieldElement(other, self.prime)
        elif isinstance(other, PrimeFieldElement):
            if self.sameField(other):
                return other
            else:
                print "Different fields! Abort!"
        else:
            print "Wrong type"
