
def filter(L,target):
  
    if L == []:
        return []
    
    last_vaule = L.pop()
    
    ans = filter(L,target)

    if last_vaule != target:
        ans.append(last_vaule)
    
    return ans

        




    

def main():
    ans = filter([1,4,3,6,2,5,3],3)
    print(ans)

main()


    