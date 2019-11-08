from abc import ABC, abstractmethod     #Abstract Base Class
import math                             #For sin, cos, PI constant

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


class ComplexBase(ABC):
    """
    Base class for Complex Number ADT
    """
    @abstractmethod
    def getReal(self):
        """ Return the real part """
        pass

    @abstractmethod
    def getImaginary(self):
        """ Return the imaginary part """
        pass

    @abstractmethod
    def getMagnitude(self):
        """ Return the magnitude part """
        pass

    @abstractmethod
    def getPhase(self):
        """ Return the phase part """
        pass
    
    @abstractmethod
    def add(self, other):
        """ Perform self = self + other """
        pass

    @abstractmethod
    def minus(self, other):
        """ Perform self = self - other """
        pass

    @abstractmethod
    def time(self, other):
        """ Perform self = self * other """
        pass

    @abstractmethod
    def toRectangularString(self):
        """ Return a string in rectangular form, i.e. A + Bi"""
        pass

    @abstractmethod
    def toPolarFormString(self):
        """ Return a string in polar form, i.e. magnitude( cos Theta, i sin Theta)"""
        pass    

def main():
    c = ComplexBase()   #this should fails as ComplexBase is an abstract class

if __name__ == "__main__":
    main()