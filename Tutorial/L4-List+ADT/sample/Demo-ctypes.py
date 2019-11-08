from ctypes import *

def main():
    array = (5 * c_int)()

    for i in range (5):
        array[i] = 3000 + i

    for i in range (5):
        print("Item[%d] = %d" %(i, array[i]))

    print(hex(addressof(array)))

    #cause exception
    array[10] = 123


if __name__ == "__main__":
    main()

