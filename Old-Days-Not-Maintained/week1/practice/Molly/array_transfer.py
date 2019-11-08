arr = [[1,2,3],[4,5,6],[7,8,9]]
print(arr)

def print2DArray(arr):
    for i in range(len(arr)):
        print("{} ".format(arr[i]))

def printEachNumber(arr):
    for i in range(len(arr)):
        row = arr[i]
        for j in range(len(row)):
            print("row{0} col{1} : {2}".format(i, j, row[j]))

print2DArray(arr)
printEachNumber(arr)