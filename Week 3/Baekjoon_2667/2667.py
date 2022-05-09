import sys 

def dfs(x, y):
    if x<0 or x>=N or y<0 or y>=N:
        return False
    if D[x][y] == 1:
        D[x][y] = 0
        R[-1] += 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False 
cnt = 0
N = int(input())
D = []
R = [0]
for i in range(N):
    D.append(list(map(int, sys.stdin.readline().rstrip())))
for i in range(N):
    for j in range(N):
        if dfs(i, j) == True :
            R.append(0)

R.sort()
print(len(R)-1)
for i in range(1, len(R)):
    print(R[i])