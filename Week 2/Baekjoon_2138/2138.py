import sys
n = int(input())
A = list(map(int, sys.stdin.readline().rstrip()))
B = list(map(int, sys.stdin.readline().rstrip()))
cnt = 0




if A==B:
    print(cnt)
else :
    print(-1)