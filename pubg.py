def gcd(a,b):
    if a == 0 or b == 0:
        return  max(a,b)
    return gcd(b,a%b)
lst = list(map(int,input().split()))
if len(lst) == 1:
    print(lst[0])
    exit(0)
health  = min(lst[0],lst[1])
for i in lst:
    health = gcd(health,i)
print(health)