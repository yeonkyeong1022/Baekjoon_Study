from sys import stdin 

N = int(stdin.readline())
S = [] 
for i in range(N):
    S.append(list(map(int, stdin.readline().split())))
    
def start_link():
    return 