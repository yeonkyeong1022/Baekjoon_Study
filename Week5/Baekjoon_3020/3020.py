from sys import stdin
# 이분탐색만 생각하지 말고 누적합에 집중해볼 것
# 누적합 활용하여 해결해보기(지금 코드엔 딱히 누적합이랄게 없다.)

# N, H = map(int, stdin.readline().split())
# obstacles = []
# for i in range(N):
#     obstacles.append(int(stdin.readline()))
# start = 0
# end = H
# bottom, top = 0, 0
# result = 0
# minObs = 0
# prevSuck = 0
# pravJong = 0

# #석순 기준
# while start<=end:
#     mid = (start+end)//2
#     bottom = 0
#     top = 0

#     for i in range(N):
#         if i%2==0 and H-obstacles[i]<mid:
#             top+=1
#         elif i%2==1 and obstacles[i]>=mid:
#             bottom+=1
            
#     if top+bottom<minObs:
#         minObs = top+bottom
#         result = mid

#     if bottom<top :
#         end = mid-1
#     else:
#         start = mid+1
#     print(bottom, top, mid)

# # 종유석 기준

# print(bottom+top, result)

#############################3

# 누적합 활용한 풀이

N, H = map(int, stdin.readline().split())
obstacle = [0]*(H+1)
top = [0]*(H+1)
bottom = [0]*(H+1)
# top, bottom 배열은 각각 해당 인덱스의 높이에 몇 개의 장애물이 존재하는지 저장한다.

for i in range(N):
    height = int(stdin.readline())
    if i%2==0:
        bottom[height]+=1
    else :
        top[H-height+1]+=1
# print(top, bottom)

for i in range(2,H+1):
    top[i] += top[i-1] 
for i in range(H-1, 0, -1):
    bottom[i] += bottom[i+1]
for i in range(H+1):
    obstacle[i] = top[i]+bottom[i]
# print(top, bottom)
obstacle.pop(0)
# print(obstacle)
print(min(obstacle),obstacle.count(min(obstacle)))