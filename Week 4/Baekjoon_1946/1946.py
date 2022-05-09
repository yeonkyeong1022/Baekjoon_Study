import sys 
from sys import stdin
T=int(stdin.readline())

for i in range(T):
    N = int(stdin.readline())
    Grade = [] 
    cnt = 1
    for j in range(N):
        Grade.append(list(map(int, sys.stdin.readline().split())))
    Grade.sort(key=lambda x:x[0])
    min = Grade[0][1]

    for j in range(1,N):
        if min>Grade[j][1]:
            min = Grade[j][1]
            cnt+=1
    print(cnt)
