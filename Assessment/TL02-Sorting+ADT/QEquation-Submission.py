"""
For IT5003 - by SYJ 

Version 1.0 (2019 October)
- For Lab 

"""

class QEquation():
    """ Class representing a quadratic equation, ax^2 + bx + c = 0"""
    def __init__(self, a, b, c):
        """ a, b and c are real number, a != 0 """
        pass #replace with your own code
    
    def discriminant(self):
        """ Return discriminant b^2 - 4ac """
        return 0

    def getRealRoots(self):
        """ Returns the real root(s) of equation

            If there is no real roots, return None
            Otherwise return the roots as a tuple:
            (oneRoot)         OR
            (rootA, rootB)

        """
        return None

    def intersect(self, other):
        """ Returns the NUMBER of intersection point(s) between this equation and another"""
        return 0

    def toString(self):
        """ Print format: ax^2 + bx + c = 0

            a, b and c are printed with 2 places precision
        """
        return ""

def buildQE():
    """ ask user for a, b and c, then return a constructed QEquation object"""
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    return QEquation(a, b, c)

def main():
    
    eq1 = buildQE()
    print(eq1.toString())
    print(eq1.discriminant())
    print(eq1.getRealRoots())

    eq2 = buildQE()
    print(eq2.toString())
    print(eq2.discriminant())
    print(eq2.getRealRoots())

    print("The two parabolas intersected "+str(eq1.intersect(eq2))+" time(s).")

if __name__ == "__main__":
    main()