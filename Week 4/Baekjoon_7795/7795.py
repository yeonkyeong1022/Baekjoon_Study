import sys
from bisect import bisect_left, bisect_right
T = int(input())
for i in range(T):
    cnt = 0
    N, M = map(int, input().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    A.sort()
    B.sort()
    
    for i in range(N):
        cnt += bisect_left(B, A[i])

    print(cnt)            
            