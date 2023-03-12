def reduce(a,b):
    mod = 0
    for i in range(len(b)):
        mod = (mod*10+ord(b[i]))%a
    return mod
def gcd(a,b):
    if b == 0:
        return a
    if a == 0:
        return b
    return gcd(b,a%b)
a = int(input())
b = input()

ans = 0
for i in range(a,b+1):
    ans = gcd(ans,i)
print(ans)