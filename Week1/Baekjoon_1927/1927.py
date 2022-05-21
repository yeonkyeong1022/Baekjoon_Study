import heapq as hq
import sys
Mheap = []
N = int(input())
for i in range(N):
    x = int(sys.stdin.readline())
    if x>0:
        hq.heappush(Mheap, x)
    elif len(Mheap)==0:
        print("0")
    else :
        print(hq.heappop(Mheap))
        