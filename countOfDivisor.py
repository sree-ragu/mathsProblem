def NoOfDivisor(num):
    i = 1
    cnt = 0
    while i*i<num:
        if num%i==0:
            cnt+=2
        i+=1
    if i*i == num:
        cnt+=1
    return cnt
lst = list(map(int,input().split()))
res = []
for i in lst:
    res.append(NoOfDivisor(i))
print(res)
