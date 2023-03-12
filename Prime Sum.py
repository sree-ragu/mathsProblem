"""
GOLDBACH's conjecture states

"""
def PrimeList(num):
    prime = [True for i in range(num+1)]
    p = 2
    while(p*p<=num):
        if(prime[p] == True):
            for i in range(p*p,num+1,p):
                prime[i] = False
        p+=1
    return prime
n = int(input())
prime = PrimeList(n)
print(prime)
for i in range(2,len(prime)):
    if prime[i]:
        for j in range(i,len(prime)):
            if prime[j]:
                if i+j == n:
                    print(i,j)
                    exit(0)
