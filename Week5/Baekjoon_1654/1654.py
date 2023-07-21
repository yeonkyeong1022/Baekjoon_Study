from sys import stdin 

K, N = map(int, stdin.readline().split())
nums = []
for i in range(K):
    nums.append(int(stdin.readline()))

start = 0
end = max(nums)
result = 0

while start<=end :
    mid = (start+end)//2
    if mid == 0:
        mid = 1
    cnt = 0
    for i in nums:
        cnt += i//mid
    
    if cnt < N:
        end = mid-1
    else :
        result = mid 
        start = mid+1
    
print(result)