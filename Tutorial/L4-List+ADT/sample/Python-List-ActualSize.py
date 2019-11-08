import sys

def main():
    n = int(input("N = "))

    aList = []
    for i in range(n):
        print("Length: %5d | Actual Size: %5d bytes"%(len(aList),sys.getsizeof(aList)))
        aList.append(i)



if __name__ == "__main__":
    main()

