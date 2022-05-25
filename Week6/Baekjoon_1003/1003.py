from sys import stdin 
T = int(input())
for i in range(T):
    d = [ [0, 0] for i in range(41)]
    d[0][0] = 1
    d[1][1] = 1
    N = int(stdin.readline())
    for j in range(2, N+1):
        d[j][0] = d[j-1][0]+d[j-2][0]
        d[j][1] = d[j-1][1]+d[j-2][1]
    print(d[N][0], d[N][1])