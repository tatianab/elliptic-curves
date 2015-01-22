"""
    \file   randomcurve.py
    \author Tatiana Bradley
    \brief  Generate (and verify) prime curves at random.
    \detail Algorithms for random curve generation adapted
            from Hankerson, Menezes and Vanstone (2004).
            Uses SHA-256 hash function.
"""
from primecurves import *
from random import *
from math import *
from bitstring import *
import hashlib

BITS_IN_BYTE = 8
hashFunction = hashlib.sha256                           # The hash function to use. (SHA-256)
HASH_LENGTH = hashFunction().digest_size * BITS_IN_BYTE # The length of the hash function
                                                        # digest, in bits.

"""
" generateRandomCurve()
" INPUT: prime, a prime > 3.
" OUTPUT: a random seed
"         a random curve over F_prime
"""
def generateRandomCurve(prime):
    # STEP 1
    t = long( ceil( log(prime, 2) ) )
    s = t - 1
    v = t - s * HASH_LENGTH

    result = 0
    
    while result == 0 or ((4 * result + 27) % prime) == 0:

        # STEP 2
        seedLength = HASH_LENGTH + 5
        seed       = BitString.random(seedLength)

        # STEP 3
        hashedSeed = seed.getHashedValue(hashFunction, HASH_LENGTH)
        r0         = hashedSeed.rightBits(v)

        # STEP 4
        R0         = r0.clearLeftBit()

        # STEP 5
        seedAsInt = seed.toInt()

        # STEP 6 and 7
        binaryResult = BitString("")
        for i in range(s):
            rawString = BitString.fromInt((seedAsInt + i) % (2 ** seedLength), seedLength)
            binaryResult += rawString.getHashedValue(hashFunction, HASH_LENGTH)

        # STEP 8
        result = binaryResult.toInt()
        
        # STEP 9 (while loop condition)

    # STEP 10
    a, b = generateParameters(result, prime)

    # STEP 11
    return seed, PrimeCurve(a, b, prime)

def generateTraceOne(prime):
    for i in range(prime ** 2):
        Seed, Curve = generateRandomCurve(prime)
        Curve.getAllPoints()
        if (Curve.getOrder() == prime):
            return Curve
    return "FAILURE"
        
""" HELPER FUNCTIONS """

"""
" Generate a, b such that
" r * b^2 = a^3 mod prime
"""
def generateParameters(r, prime):
    found = False
    while not found:
        b = choice(range(prime))
        for a in range(prime):
            found = (r * (a ** 2)) % prime == (b ** 3) % prime
    return a, b
        
        

# EXAMPLE:
Seed, Curve = generateRandomCurve(29)
    
