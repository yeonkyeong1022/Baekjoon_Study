import sys
a=[]
cnt=0
n, k = map(int, sys.stdin.readline().split())
for i in range(n):
    a.append(int(sys.stdin.readline()))
i = n-1                         # 1
while k!=0:                     # 2
    if a[i]<=k:                 # 3
        cnt += (k//a[i])
        k%=a[i]
    i-=1
print(cnt)