"""
" /file pollardsrho.py
" /author Tatiana Bradley
" /brief Implementation of Rollard's rho algorithm for
"        computing the discrete log of an elliptic curve
"
"""

from primefieldelement import *

"""
" Function: pollardsRho
" INPUTS: A PrimeCurve curve
"         a PrimePoint P of prime order (n) on curve
"         a PrimePoint Q in the group generated by P
" OUTPUT: The dicrete log l such that Q = l*P.
"""
def pollardsRho(P, Q, curve):
    pass ## TODO

"""
" Function: pRho
# Simpler version of pollard's rho, using a prime field.
" INPUTS: A prime modulus prime
"         a base gamma
"         an element alpha
" OUTPUT: The dicrete log x such that gamma^x = alpha mod prime.
"""
def pRho(gamma, alpha, prime):
    subsetCutoffs = [ prime/3, (prime/3) * 2 ]
    
    gamma = PrimeFieldElement(gamma, prime)
    alpha = PrimeFieldElement(alpha, prime)

    x = PrimeFieldElement.random(prime - 1)
    initial = x
    y = PrimeFieldElement(0, prime - 1)
    beta = getBeta(alpha, gamma, x, y)
    
    triplet = [ beta, x, y ]
    storedIndex = 0
    storedTriplet = [ beta, x, y ]
    
    while True:

##        print str(storedIndex) + ": " + str(triplet)
        
        if (storedIndex == 0):
            nextIndex = 1
        else:
            nextIndex = storedIndex * 2
            
        for i in range(storedIndex + 1, nextIndex + 1):
            subset = getSubset(triplet[0], subsetCutoffs)
            triplet = transform(triplet, gamma, alpha, subset)
            if (triplet[0] == storedTriplet[0]):
##                print "Found it! index: " + str (i)
##                print triplet
                endX = storedTriplet[1] - triplet[1]
                endY = triplet[2] - storedTriplet[2]
##                print "Congruence: " + str(gamma) + "^" + str(endX) + " = " + str(alpha) + "^" + str(endY)
                return i, initial

        storedTriplet = triplet
        storedIndex = nextIndex
    

def getBeta(alpha, gamma, currentX, currentY):
    return (gamma ** currentX.value) * (alpha ** currentY.value)

def getSubset(element, cutoffs):
    
    if element <= cutoffs[0]:
        return 1
    elif element <= cutoffs[1]:
        return 2
    else:
        return 3

def transform(triplet, gamma, alpha, subset):
    return [ transformBeta(triplet[0], gamma, alpha, subset),
             transformX(triplet[1], subset),
             transformY(triplet[2], subset) ]
    
""" Helper for pRhoPrimeField """
def transformBeta(element, gamma, alpha, subset):
    if subset == 1:
        return gamma*element
    elif subset == 2:
        return element ** 2
    elif subset == 3:
        return alpha*element

def transformX(x, subset):
    
    if subset == 1:
        return x + 1
    elif subset == 2:
        return x * 2
    elif subset == 3:
        return x

def transformY(y, subset):
    if subset == 1:
        return y
    elif subset == 2:
        return y * 2
    elif subset == 3:
        return y + 1

def pRhoRepeated(gamma, alpha, prime, numTrials):

    dict = {}
    
    for i in range(numTrials):
        matchIndex, initial = pRho(gamma, alpha, prime)
        if matchIndex in dict:
            dict[matchIndex] += 1
        else:
            dict[matchIndex] = 1

    print dict


"""
SOME EXPERIMENTAL OUTPUTS:

>>> pRhoRepeated(5, 3, 2017, 100)
{162: 26, 98: 74}

>>> pRhoRepeated(5, 3, 2017, 100)
{98: 71, 162: 29}

>>> pRhoRepeated(5, 3, 2017, 1000)
{16: 17, 98: 736, 162: 247}

>>> pRhoRepeated(5, 3, 2017, 5000)
{16: 80, 24: 2, 162: 1233, 98: 3685}

"""
