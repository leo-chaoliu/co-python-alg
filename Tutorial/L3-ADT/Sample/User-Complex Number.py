from abc import ABC, abstractmethod     #Abstract Base Class
import math

#Our own implementations
from ComplexPolar import ComplexPolar
from ComplexRectangular import ComplexRectangular

def main():

    # Version 2.0
    # c1 = ComplexRectangular(30, 10)
    # c2 = ComplexRectangular(20, 20) 

    # Version 3.0
    # c1 = ComplexPolar(31.62, 0.322)
    # c2 = ComplexPolar(28.28, 0.785) 

    # Version 4.0
    c1 = ComplexRectangular(30, 10)
    c2 = ComplexPolar(28.28, 0.785) 

    print("Complex number c1:")
    print(c1.toRectangularString())
    print(c1.toPolarFormString())

    print("Complex number c2:")
    print(c2.toRectangularString())
    print(c2.toPolarFormString())

    print("add c2 to c1")
    c1.add(c2)

    print("Complex number c1:")
    print(c1.toRectangularString())



if __name__ == "__main__":
    main()

