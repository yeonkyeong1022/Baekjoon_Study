from sys import stdin 

N = int(stdin.readline())
AList = list(map(int, stdin.readline().split()))
operators = list(map(int, stdin.readline().split()))    
minAns = 1000000001
maxAns = -1000000001

def dfs(result, numIdx):
    global minAns, maxAns
    if numIdx>=N:
        if minAns>=result:
            minAns = result
            # print("Min: ", minAns)
        if maxAns<=result:
            maxAns = result
            # print("Max: ", maxAns)
        return
    num = AList[numIdx]
    nextResult = [result+num, result-num, result*num, int(result/num)]
    # print(nextResult)
    for i in range(4):
        if operators[i] >0:
            operators[i]-=1
            # print("operator:", i)
            # print(operators)
            dfs(nextResult[i], numIdx+1)
            operators[i]+=1
            
            
    return
    
dfs(AList[0], 1)
# print(operators, AList)
print(maxAns)
print(minAns)