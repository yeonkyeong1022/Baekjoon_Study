n = int(input())
result = 0

def C(a, b):
    r1 = 1
    r2 = 1
    for i in range(b):
        r1*=(a-i)
        r2*=(i+1)
    return r1//r2
                
for i in range(0, n//2+1):
    result += C(n-i, i)
print(result%10007)