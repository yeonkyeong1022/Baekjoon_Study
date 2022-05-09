import sys 
A = []
B = []
cnt = 0

def Swap(A, i, j):             # 0, 1
    for I in range(3):
        for J in range(3):
            A[I+i][J+j] = int(not A[I+i][J+j])
    
n, m = map(int, input().split())
for i in range(n):
    A.append(list(map(int, list(sys.stdin.readline().rstrip())))) 

for i in range(n):
    B.append(list(map(int, list(sys.stdin.readline().rstrip()))))
    
for i in range(n-2):
    for j in range(m-2):
        if A[i][j]!=B[i][j]:
            Swap(A, i, j)
            cnt += 1
if A==B:
    print(cnt)
else :
    print(-1)