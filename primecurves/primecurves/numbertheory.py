"""
" /file numbertheory.py
" /author Tatiana Bradley
" /brief Some nice number theory algorithms:
"        gcd, successive squaring, and linear equation solving.
"""


"""
" Raise a number to a power (in Z/mZ)
" using successive squaring.
" OUTPUT: M ** power mod modulus
"""
def successiveSquare(M, power, modulus):
    b = 1
    while power>=1:
        if isOdd(power):
            b = (M*b)%modulus
        M = (M**2)%modulus
        power = power >> 1
        print M

    return b

"""
" Finds the gcd (greatest common divisor)
" of two integers a and m.
"""
def gcd(a,m):
    if a<m:
        big = m
        small = a
    else:
        big = a
        small = m
    mult = big/small
    rem = big - mult*small
    print str(big) + "=" + str(small) + "*" + str(mult) + "+" + str(rem)
    if rem == 0:
        return small
    return gcd(small,rem)

"""
" Solves a linear equation,
" returning the u value.
"""
def linearEquation(a,b):
    x = 1
    g = a
    v = 0
    w = b
    while w>=1:
        q = g/w
        t = g - q*w
        s = x - q*v
        (x,g) = (v,w)
        (v,w) = (s,t)
    y = (g - a*x)/b
    if a>b:
        return x
    else:
        return y


""" True if n is odd. """
def isOdd(n):
    if n%2 == 0:
        return False
    else:
        return True

