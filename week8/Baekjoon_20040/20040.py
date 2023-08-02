from sys import stdin, exit, setrecursionlimit

setrecursionlimit(100000)

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a>b:
        parent[a] = b
    else:
        parent[b] = a 

n, m = map(int, stdin.readline().split())
parent = [0]*(n)
cycle = False
result = 0
for i in range(n):
    parent[i] = i 
edges = []
for _ in range(1,m+1):
    u, v = map(int, stdin.readline().split())
    edges.append((u, v))

idx = 0
for u, v in edges:
    idx+=1   
    if find(parent, u)== find(parent, v):
        cycle = True 
        break
    union(parent, u, v)

if cycle:
    print(idx)
else:
    print("0")
