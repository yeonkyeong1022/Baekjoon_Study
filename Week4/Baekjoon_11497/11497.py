from sys import stdin 

T = int(stdin.readline())

for i in range(T):
    N = int(stdin.readline())
    L = list(map(int, stdin.readline().split())) 
    L.sort() 
    Result = [0]*N
    i = 0
    for j in L:
        if i % 2 == 0:
            Result[i//2] = j
        else :
            Result[-1-i//2] = j
        i+=1
    max = abs(Result[0]-Result[1])
    for j in range(N-1):
        if max<abs(Result[j]-Result[j+1]):
            max = abs(Result[j]-Result[j+1])
    print(max)