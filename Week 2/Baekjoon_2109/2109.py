import sys
Visit = [0]*10001
PD = []
maxP=0
n = int(input())
for i in range(n):
    PD.append(list(map(int, sys.stdin.readline().split())))
PD.sort(key = lambda x:-x[0])
for i in range(n):
    for j in range(PD[i][1], 0, -1):
        if Visit[j] == 0:
            Visit[j] = 1
            maxP += PD[i][0]
            break
        
print(maxP)