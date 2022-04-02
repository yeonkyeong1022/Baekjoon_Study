import sys
import heapq as hq

n = int(sys.stdin.readline())
ST = []
R=[]

for i in range(n):
    ST.append(list(map(int, sys.stdin.readline().split())))
ST.sort()
hq.heappush(R, ST[0][1])

for i in range(1, n):
    if ST[i][0] >= R[0]:
        hq.heappop(R)
        hq.heappush(R, ST[i][1])
    else:
        hq.heappush(R, ST[i][1])
print(len(R))