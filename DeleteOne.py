import math as m
def MaxGcd(a,n):

    prefix = [0 for i in range(n+2)]
    suffix= [0 for i in range(n+2)]
    prefix[1] = a[0]
    for i in range(2,n+1):
        prefix[i] = m.gcd(prefix[i-1],a[i-1])
    suffix[n] = a[n-1]
    for i in range(n-1,0,-1):
        suffix[i]= m.gcd(suffix[i-1],a[i-1])
    ans = max(suffix[2],prefix[n-1])
    for i in range(2,n):
        ans = max(ans,m.gcd(prefix[i-1],suffix[i-1]))
    return ans
lst = list(map(int,input().split()))
print(MaxGcd(lst,len(lst)))