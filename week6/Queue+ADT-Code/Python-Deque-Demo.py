from collections import deque

def main():
    dq = deque()

    #Items can be added both ends
    dq.append(111)      #added to the "right", the tail end
    dq.append(122)

    dq.appendleft(999)  #added to the "left", the front end
    dq.appendleft(988)

    print(dq)

    #Items can be removed from both ends

    dq.pop()        #removed from the right end
    dq.popleft()    #removed from the left end
    print(dq)
    
if __name__ == "__main__":
    main()