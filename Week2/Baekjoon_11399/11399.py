import sys
n = int(sys.stdin.readline())
P = []
minT=0
P=list(map(int, sys.stdin.readline().split()))
P.sort()
for i in range(1, n+1):
    minT+=P[-i]*i
print(minT)