elliptic-curves
===============
Play with elliptic curves!
A senior thesis project, Fall 2014.
Feel free to use this code in any way you see fit.

Terms:
ECDLP = elliptic curve discrete log problem

-- /primecurves
   A python package. All things related to elliptic curves over prime fields (Z/pZ).
   
   Structures:
      PrimeCurve        - elliptic curve
      PrimePoint        - point on an elliptic curve
      PrimeFieldElement - element of a prime field F_p, i.e., an integer mod p
      PAdic             - p-adic rational number (in Q_p)       // TODO!
      
   Algorithms:
      bruteforcelog     - compute ECDLP by brute force (enumeration)
      pollardsrho       - compute ECDLP by Pollard's rho algorithm
      traceone          - compute ECDLP on curves of trace one  // TODO!
      
   Other stuff:
      numbertheory      - a few helpful algorithms from number theory: 
                          gcd, successive squaring, etc.
      
      
      
      
      
