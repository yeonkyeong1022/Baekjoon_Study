
# n = int(input())
# result = 0

# def C(a, b):
#     r1 = 1
#     r2 = 1
#     for i in range(b):
#         r1*=(a-i)
#         r2*=(i+1)
#     return r1//r2
                
# for i in range(0, n//2+1):
#     result += C(n-i, i)
# print(result%10007)


n = int(input())
d = [0]*1001 
d[0] = 1
d[1] = 1 
for i in range(2, n+1):
    d[i] = d[i-1]+d[i-2]
print(d[n]%10007)