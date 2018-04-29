def hano(n,a,b,c):
    if n==1:
        print(a+'---->'+c)
    else:
        hano(n-1,a,c,b)
        print(a+'---->'+c)
        hano(n-1,b,a,c)
        
