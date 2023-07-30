from sys import stdin 

N = int(stdin.readline())
AList = list(map(int, stdin.readline().split()))

visited = [False]*N
Visited = [0]*N
# maxLength = 1
# visited[prevValue] = True
for i in range(N):
    length = 1
    prevValue = AList[i]
    # prevValue = 0
    # if visited[i] == True:
    #     continue
    for j in range(i, N):
        curValue = AList[j]
        if curValue > prevValue:
            if Visited[j]>0:
                Visited[j] += length
            length += 1

            # prevValue = AList[j]
            # visited[j] = True
            

print(max(Visited))

'''
100 1 2 3 101 4 5 6 102 7 8
1         2         3
    1 2 3 5  
'''