import sys
stack=[]
arr=[]
s=1
TF=0

n = int(input())
for i in range(n):
    num = int(sys.stdin.readline())
    while s<=num:
        arr.append('+')
        stack.append(s)
        s+=1
    if stack[-1]==num:
        stack.pop()
        arr.append('-')
    else :
        TF=1
if TF==1:
    print("NO")
else :
    for i in arr:
        print(i)