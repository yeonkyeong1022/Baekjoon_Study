from sys import stdin 

N = int(stdin.readline())
array = [i for i in range(N)]
S = [] 
used = [False for i in range(N)]
combList = []
minDiff = 500
for i in range(N):
    S.append(list(map(int, stdin.readline().split())))
K = N//2   # 두 그룹으로 나누어야 하므로(K만큼 뽑는 조합의 수)

def comb(idx, combLen):
    global minDiff
    if combLen == K:
        
        startTeam = 0
        linkTeam = 0

        for i in range(N-1):
            for j in range(i+1, N):
                if used[i] == True and used[j]==True:
                    startTeam+=(S[i][j]+S[j][i])
                elif used[i]==False and used[j]==False:
                    linkTeam+=(S[i][j]+S[j][i])

        abilityDiff = abs(startTeam-linkTeam)
        if minDiff>abilityDiff:
            minDiff = abilityDiff
        return 
    
    for i in range(idx+1, len(array)):
        if used[i] == False:
            used[i] = True
            comb(i, combLen+1)
            used[i] = False 
    return 

comb(-1, 0)

print(minDiff)

