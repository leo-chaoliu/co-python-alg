from abc import ABC, abstractmethod     #Abstract Base Class
import math                             #For sin, cos, PI constant
from ComplexBase import ComplexBase     #For ComplexBase Abstract Class as a superclass

"""
For IT5003 - by SYJ 

Version 1.0 (2019 September)
- Implemented Complex Number ADT:
    - Specification: ComplexBase Base Class
    - Implementations: 
        A. Rectangular Form (ComplexRectangular Class)
        B. Polar Form (ComplexPolar Class)

- Basic documentation only

"""

class ComplexRectangular(ComplexBase):
    """ Complex Number implemented with Rectangular form"""

    def __init__(self, real, imag):
        """ Uses real and imaginary part internally """
        self._real = real
        self._imag = imag

    def getReal(self):
        """ Return the real part """
        return self._real

    def getImaginary(self):
        """ Return the imaginary part """
        return self._imag

    def getMagnitude(self):
        """ Return the magnitude part """
        return math.sqrt( self._real**2 + self._imag**2)

    def getPhase(self):
        """ Return the phase part """
        if self._real > 0 or self._imag != 0:
            #Using half-angle indentity to reduce cases
            den = math.sqrt(self._real**2 + self._imag**2) + self._real
            radian = 2 * math.atan( self._imag / den)
        elif self._real < 0 and self._imag == 0:
            radian = math.pi 
        else: 
            radian = None
        return radian

    def add(self, other):
        """ Perform self = self + other """
        self._real = self._real + other.getReal()
        self._imag = self._imag + other.getImaginary() 

    def minus(self, other ):
        """ Perform self = self - other """
        self._real = self._real - other.getReal()
        self._imag = self._imag - other.getImaginary()    

    def time( self, other ):
        """ Perform self = self * other """
        realNew = self._real * other.getReal() - self._imag * other.getImaginary()
        imagNew  = self._real * other.getImaginary() + self._imag * other.getReal()
        self._real = realNew
        self._imag = imagNew

    def toRectangularString(self):
        """ Return a string in rectangular form, i.e. A + Bi"""
        return  "({:.3f}, {:.3f}i)".format(self.getReal(), self.getImaginary())

    def toPolarFormString(self):
        """ Return a string in polar form, i.e. magnitude( cos Theta, i sin Theta)"""
        return "{0:.3f}(cos {1:.3f}, i sin {1:.3f})".format(self.getMagnitude(), self.getPhase())

def main():
    #Just basic testing, see "User-ComplexNumber.py" for the user program
    c1 = ComplexRectangular(3, 5)   
    
    #printing tests
    print( "c1 is " + c1.toRectangularString() )
    print( "the same as " + c1.toPolarFormString() )

    #simple arithmetic test
    c2 = ComplexRectangular(-7, -7)
    print( "c2 is " + c2.toRectangularString() )
    print( "the same as " + c2.toPolarFormString() )

    c1.add(c2)
    print( "c1 + c2 = " + c1.toRectangularString() )

    c1.minus(c2)
    print( "c1 + c2 = " + c1.toRectangularString() )

    c1.time(c2)
    print( "c1 * c2 = " + c1.toRectangularString() )

if __name__ == "__main__":
    main()