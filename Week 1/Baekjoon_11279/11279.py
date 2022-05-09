import sys
def maxHeap(arr, i):
    left = 2*i
    right = (2*i)+1
    min = i
    if left<len(arr) and data[i]<data[left]:
        min = left
    if right<len(arr) and data[i]<data[right]:
        min = right
        if data[right]<data[left]:
            min = left
    if min != i:
        data[i], data[min] = data[min], data[i]
        maxHeap(arr, min)


data = [None]
N = int(input())
for i in range(N):
    x = int(sys.stdin.readline())
    if x>0:
        data.append(x)
        l = len(data)-1
        while l>1:
            if data[l]>data[l//2]: # 부모노드보다 크면
                data[l], data[l//2] = data[l//2], data[l] #교환
                l=l//2 #비교대상 한 칸 위로
            else :
                break
    elif len(data)==1:
        print("0")
    else :
        data[1], data[-1] = data[-1], data[1]
        print(data.pop())
        maxHeap(data, 1)
        