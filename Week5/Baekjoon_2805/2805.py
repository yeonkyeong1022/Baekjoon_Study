from sys import stdin 

N, M = map(int, stdin.readline().split())
tree= list(map(int, stdin.readline().split()))

start= 0
end = max(tree)
result = 0

while start<=end :
    sum = 0
    mid = (start+end)//2
    

    for i in range(len(tree)):
        if tree[i] - mid >0:
            sum += tree[i]-mid
    if sum < M:
        end = mid-1
    else :
        result = mid
        start = mid+1
print(result)

