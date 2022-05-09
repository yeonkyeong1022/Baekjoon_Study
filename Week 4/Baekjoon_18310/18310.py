import sys
N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
L.sort()
print(L[(N-1)//2])