from functools import reduce
def str2float(s):
    count=s.find('.')
    return reduce(lambda x,y: 10*x+y, map(int,s[0:count]))+ 0.1 * reduce(lambda x,y: 0.1*x+y, map(int, s[len(s)-1:count:-1]))
