import sys
n = int(sys.stdin.readline())
T = []
cnt = 1
fIdx = 0
for i in range(n):
    T.append(list(map(int, sys.stdin.readline().split())))
T.sort()
T.sort(key= lambda x:x[1])

for i in range(1, n):
    if T[fIdx][1]<=T[i][0]:
        fIdx = i
        cnt+=1
print(cnt)