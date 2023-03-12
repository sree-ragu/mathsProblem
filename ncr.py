def ncr(n,r,x):
    if(r>n-r):
        r = n-r
    arr = [0 for i in range(r+1)]
    arr[0] = 1
    for i in range(1,n+1):
        for j in range(min(i,r),0,-1):
            arr[j] = (arr[j]+arr[j-1])%x
    return arr[r]
n = int(input())
r = int(input())
x = int(input())
print(ncr(n,r,x))