from sys import stdin

N, H = map(int, stdin.readline().split())
obstacles = []
for i in range(N):
    obstacles.append(int(stdin.readline()))
start = 0
end = H
suck, jong = 0, 0
result = 0
minObs = N
while start<=end:
    mid = (start+end)//2
    suck = 0
    jong = 0

    for i in range(N):
        if i%2==0 and H-obstacles[i]<mid:
            jong+=1
        elif i%2==1 and obstacles[i]>=mid:
            suck+=1
            
    if jong+suck<minObs:
        minObs = jong+suck
        result = mid

    if suck<jong :
        end = mid-1
    else:
        start = mid+1
    print(suck, jong, mid)
print(suck+jong, result)