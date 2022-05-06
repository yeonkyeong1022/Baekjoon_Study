from sys import stdin 

N, L = map(int, stdin.readline().split())

Pipe = list(map(int, stdin.readline().split()))

Pipe.sort()
tape = 0
i=0
j=0
while i<N:
    if Pipe[i]-Pipe[j]+1 <= L:
        i+=1
    else :
        j = i
        tape += 1
tape += 1
print(tape)
        