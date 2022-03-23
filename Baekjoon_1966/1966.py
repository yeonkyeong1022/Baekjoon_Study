import sys
T = int(input())
for i in range(T):
    N,M=map(int, input().split())
    txt = list(map(int, input().split()))
    ind = M
    cnt=1
    while True:
        tmp = txt[0]
        if txt[0]==max(txt):
            if ind==0:
                break
            cnt+=1
            txt.remove(txt[0])
        else:
            txt.remove(txt[0])
            txt.append(tmp)
        ind = (ind+len(txt)-1)%len(txt)
    print(cnt)