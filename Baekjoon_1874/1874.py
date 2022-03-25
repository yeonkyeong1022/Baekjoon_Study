result=[]
stack=[]
ind = -1
n = int(input())
for i in range(n):
    result.append(int(input()))
    
for i in range(1, n+1):
    stack.append(i)
    print("+")
    
    for j in range(n):
        if result[j]==stack[-1]:
            stack.pop()
            print("-")
        else :
            break
    
    
    
    






    