def odd_num():
    n  = 1
    while True:
        n += 2
        yield n

def primes():
    yield 2
    it  = odd_num()
    while True:
        n = next(it)
        yield n
        it = filter(lambda x,n=n : x % n>0,it)

for a in primes():
    if a <100:
        print(a)
    else:
        break
