from sys import stdin 

N = int(stdin.readline())
bud = list(map(int, stdin.readline().split()))
limit = int(stdin.readline())
start = 0
ans = 0
end = max(bud)
while start<=end:
    sum = 0
    mid = (start+end)//2

    for i in bud:
        if i>mid : 
            sum += mid 
        else :
            sum += i 

    if sum <= limit:
        ans = mid
        start = mid+1 
    else :
        end = mid-1
print(ans)