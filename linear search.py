def search(v,L):
    if L==[]:
        print('not found')
        return
    for i in range(len(L)):
        if L[i]==v:
            print('Index of %d is %d'% (v,i))
            return
    print('not found')
    return
