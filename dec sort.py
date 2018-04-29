a=[5,1,7,5,88,665,2,3,72,95]
def dec_sort(L):
    for i in range(1,len(L)):
        j=i-1
        key=L[i]
        while j>=0 and L[j]>key:
            L[j]=L[j+1]
            j-=1
        L[j+1]=key
    print(L)        
    
    
