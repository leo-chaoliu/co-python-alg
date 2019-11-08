from abc import ABC, abstractmethod     #Abstract Base Class
import math
from ComplexBase import ComplexBase


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

class ComplexPolar(ComplexBase):
    """ Complex Number implemented with Polar form"""
    def __init__(self, magnitude, phase):
        """ Uses magnitude and phase (theta) part internally """
        self._mag = magnitude
        self._phase = phase

    def getReal(self):
        """ Return the real part """
        return self._mag * math.cos(self._phase)

    def getImaginary(self):
        """ Return the iaginary part """
        return self._mag * math.sin(self._phase)

    def getMagnitude(self):
        """ Return the magnitude part """
        return self._mag

    def getPhase(self):
        """ Return the phase part """
        return self._phase
    
    def _convertPhaseAngle(self, real, imag ):
        """ Helper method to calculate phase angle """
        if real > 0 or imag != 0:
            #using half-angle identity to reduce cases
            den = math.sqrt(real**2 + imag**2) + real
            radian = 2 * math.atan( imag / den)
        elif real < 0 and imag == 0:
            radian = math.pi / 2
        else:
            radian = None
        return radian
                    
    def add(self, other):
        """ Perform self = self + other """
        real = self.getReal() + other.getReal()
        imag = self.getImaginary() + other.getImaginary()

        self._mag =  math.sqrt( real**2 + imag**2 )
        self._phase = self._convertPhaseAngle(real, imag)

    def minus(self, other ):
        """ Perform self = self - other """
        real = self.getReal() - other.getReal()
        imag = self.getImaginary() - other.getImaginary()

        self._mag =  math.sqrt( real**2 + imag**2 )
        self._phase = self._convertPhaseAngle(real, imag)

    def time( self, other ):
        """ Perform self = self * other """
        self._mag *= other.getMagnitude()
        self._phase += other.getPhase()

    def toRectangularString(self):
        """ Return a string in rectangular form, i.e. A + Bi"""
        return  "({:.3f}, {:.3f}i)".format(self.getReal(), self.getImaginary())

    def toPolarFormString(self):
        """ Return a string in polar form, i.e. magnitude( cos Theta, i sin Theta)"""
        return "{0:.3f}(cos {1:.3f}, i sin {1:.3f})".format(self.getMagnitude(), self.getPhase())

def main():
    #Just basic testing, see "User-ComplexNumber.py" for the user program
    c1 = ComplexPolar(5.831, 1.030)   
    
    #printing tests
    print( "c1 is "+ c1.toRectangularString() )
    print( "the same as " + c1.toPolarFormString() )

    #simple arithmetic test
    c2 = ComplexPolar(9.9, -2.356)
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