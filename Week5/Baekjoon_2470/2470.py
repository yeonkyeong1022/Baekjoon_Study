from sys import stdin 
from bisect import bisect_right, bisect_left

N = int(stdin.readline())
liq = list(map(int, stdin.readline().split()))
liq.sort() 

ans1 = liq[0]
ans2 = liq[1]
minMix = 2000000000

for i in range(N-1):
    tmp1 = liq[i]
    bigIdx = bisect_right(liq, abs(tmp1))
    smallIdx = bigIdx-1
    if smallIdx==i :
        smallIdx += 1
    if bigIdx>=N:
        bigIdx -=1
    
    

    tmp2 = liq[smallIdx]
    tmp3 = liq[bigIdx]

    if abs(tmp1+tmp2) < abs(tmp1+tmp3):
        mixLiq = tmp1+tmp2
    else:
        mixLiq = tmp1+tmp3 
    
    if abs(minMix) > abs(mixLiq):
        minMix = mixLiq 
        ans1 = tmp1  
        ans2 = minMix-tmp1
print(ans1, ans2)