def triangles():
    lst=[1] 
    while 1:
        yield lst
        if lst==[1]:
            lst=[1,1]
        else:
            lst_2=lst[:]
            lst_3=lst[:]
            for i in range(len(lst)-1):
                lst_3[i+1]=lst_2[i]+lst_2[i+1]
            lst_3.append(1)
            lst=lst_3[:]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
        
   

        
