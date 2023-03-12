def countDivisor(n):
    i = 1
    res = []
    while i*i<n:
        if n%i==0:
            res.append(i)
            res.append(n//i)
        i+=1
    if i*i == n:
        res.append(i)
    return res
def primeNumber(n):
    if n == 0 or n== 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
n = int(input())
tot = 0
for i in range(1,n+1):
    cnt = 0
    res = countDivisor(i)
    #print(res)
    for j in res:
        if primeNumber(j):
            cnt+=1
    if cnt == 2:
        #print(i)
        tot +=1
print(tot)
