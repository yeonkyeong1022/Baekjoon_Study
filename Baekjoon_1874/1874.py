result=[]
stack=[]
tmp=[]
ind = -1
n = int(input())
for i in range(n):
    result.append(int(input()))
    
for i in range(1, n+1):
    stack.append(i)
    print("+")
    l = len(stack)
    for j in range(len(tmp)+1, l):
        if result[j]==stack[-1]:
            tmp.append(stack.pop())
            print("-")
        else :
            break
    
    
    
    






    