"""
    \file bitstring.py
    \author Tatiana Bradley
    \brief Class representing a bitstring.
"""
from random import *
import hashlib

class BitString:

    """ CONSTRUCTOR """
    def __init__(self, string):
        self.string = string

    """
    Constructor for a random string
    """
    @classmethod
    def random(cls, desiredLength):
        result = "1"
        for i in range(desiredLength - 1):
            result += choice(["1", "0"])
        return cls(result)

    @classmethod
    def fromInt(cls, integer, desiredLength):
        return cls(bin(integer)[2:].zfill(desiredLength))
        
    def __repr__(self):
        return self.string

    """ MEMBER FUNCTIONS """

    def __iadd__(self, other):
        self.string += other.string
        return self

    def length(self):
        return len(self.string)

    def toInt(self):
        return int(self.string, 2)

    def getHashedValue(self, hashFunction, hashLength):
        hexDigest = hashFunction(self.string).hexdigest()
        # Convert the digest to binary, with the correct length
        return BitString(bin(int(hexDigest, 16))[2:].zfill(hashLength))
        
    def setBit(self, index):
        index = self.calculateIndex(index)
        self.changeBit(index, "1")

    def clearBit(self, index):
        index = self.calculateIndex(index)
        self.changeBit(index, "0")

    def clearLeftBit(self):
        self.clearBit(0)

    def calculateIndex(self, index):
        return len(self.string) - index - 1

    def rightBits(self, numBits):
        highestBit = self.calculateIndex(numBits - 1)
        result = self.string[highestBit :]
        return BitString(result)

    def changeBit(self, index, newChar):
        self.string = self.string[: index] + newChar + self.string[index + 1 :]

    

    

    

    
    

    
    
