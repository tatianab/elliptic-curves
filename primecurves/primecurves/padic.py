"""
 /file padic.py
 /author Tatiana Bradley
 /brief A class representing a p-adic in Q_p.
        ** Currently only works for p-adic integers!

"""

class PAdic:
      """
      A p-adic number.

      DATA:
      coeffs (array) - the coefficients of the number, truncated.
      begin  (int)   - the starting power. (default is 0).
      """

      def __init__(self, coeffs, begin, prime):
            self.coeffs = coeffs
            self.begin = begin
            self.prime = prime

      def __repr__(self):
            result = ""
            if len(self.coeffs) == 0:
                  return "0"
            else:
                  result += str(self.coeffs[0])

            for i in range(1, len(self.coeffs)):
                  result += " + " + str(self.coeffs[i]) + "p^" + str(i)
            result += " + " + "O(" + str(len(self.coeffs)) + ")"

            return result


