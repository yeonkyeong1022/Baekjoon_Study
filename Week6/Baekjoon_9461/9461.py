from sys import stdin 

T = int(input())
for i in range(T):
    n = int(stdin.readline())
    d = [0]*101 
    d[1] = 1
    d[2] = 1
    d[3] = 1
    for j in range(3, n+1):
        d[j] = d[j-2]+d[j-3]
        
    print(d[n])
        