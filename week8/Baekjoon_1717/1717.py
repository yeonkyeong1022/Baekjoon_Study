from sys import stdin, setrecursionlimit
setrecursionlimit(100000)

def Find(parent, x):
    if parent[x] != x:
        parent[x] = Find(parent, parent[x])
    return parent[x]

def Union(parent, a, b):
    a = Find(parent, a)
    b = Find(parent, b)
    if a>b:
        parent[a] = b 
    else:
        parent[b] = a

n, m = map(int, stdin.readline().split())
parent = [0]*(n+1)
for i in range(1, n+1):
    parent[i] = i 

for _ in range(m):
    uf, a, b = map(int, stdin.readline().split()) # uf: union할지 find할지 확인
    if uf == 1:
        if Find(parent, a) == Find(parent, b):
            print("YES")
        else:
            print("NO")
    else :
        Union(parent, a, b)