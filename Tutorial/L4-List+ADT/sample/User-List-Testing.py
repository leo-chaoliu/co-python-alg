#Our own List ADT implementations
from ListArray import ListArray
from ListLinkedList import ListLinkedList

def main():
    l = ListArray()
    #l = ListLinkedList()

    if l.insert( 1, 333 ):
        print("333 Insertion successful!\n")
    else:
        print( "333 Insertion FAILED!\n" )
        
    print(l.toString())

    l.insert( 1, 111 )
    l.insert( 3, 777 )
    l.insert( 3, 555 )
    print("After a few insertions: "+l.toString())

    print("First item is %d" % l.retrieve(1))
    print("Last item is %d" % l.retrieve(l.getLength()))

    l.remove(1)
    l.remove(2)
    l.remove( l.getLength() )

    print("After a few deletions:")
    print("First item is %d" % l.retrieve(1))
    print("Last item is %d" % l.retrieve(l.getLength()))
    
    print("Final List is "+l.toString())


if __name__ == "__main__":
    main()

