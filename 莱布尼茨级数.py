import time
pi=1
for i in range(1,300000):
    pi=pi+(1/(2*i+1)*((-1)**i))
print(pi*4)

