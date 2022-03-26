import sys
def minHeap(arr, i):
    left = 2*i
    right = (2*i)+1
    min = i
    if left<len(arr) and (abs(data[i])>abs(data[left]) or abs(data[i])==abs(data[left]) and data[i]>data[left]):
        min = left
    if right<len(arr) and (abs(data[i])>abs(data[right]) or abs(data[i])==abs(data[right]) and data[i]>data[right]):
        min = right
        if abs(data[right])>abs(data[left]) or abs(data[right])==abs(data[left]) and data[right]>data[left]:
            min = left
    if min != i:
        data[i], data[min] = data[min], data[i]
        minHeap(arr, min)
data = [None]
N = int(input())
for i in range(N):
    x = int(sys.stdin.readline())
    if x!=0:
        data.append(x)
        l = len(data)-1
        while l>1:
            if abs(data[l])<abs(data[l//2]) or abs(data[l])==abs(data[l//2]) and data[l]<data[l//2]: 
                data[l], data[l//2] = data[l//2], data[l] #교환
                l=l//2 
            else :
                break
    elif len(data)==1:
        print("0")
    else :
        data[1], data[-1] = data[-1], data[1]
        print(data.pop())
        minHeap(data, 1)
    
