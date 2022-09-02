from collections import deque
n,k = map(int, input().split())
arr_up = list(map(lambda x: [int(x),0], input().split())) #내구도, 로봇유무


arr_up = deque(arr_up)

step = 1
while True:

    #한 칸 회전 -> 내리는 칸 검사
    arr_up.rotate(1)
    arr_up[n - 1][1]=0 # 내리는 위치는 무조건 내려야함!!****

    #로봇 이동 -> 내리는 칸 검사
    for i in range(n-2,0,-1):
        if arr_up[i][1] == 1 and arr_up[i+1][0] > 0 and arr_up[i+1][1] == 0:
            arr_up[i][1]=0

            arr_up[i+1][0] -=1
            arr_up[i+1][1] = 1
    arr_up[n-1][1] = 0 # 내리는 위치는 무조건 내려야함!!****

    #올리기
    if arr_up[0][0] > 0:
        arr_up[0][0] -=1
        arr_up[0][1] = 1

    count=0
    for i in range(2*n):
        if arr_up[i][0] == 0:
            count +=1

    if count >= k:
        break

    step +=1

print(step)

# 내풀이 -> 위코드의 '내리는 위치' 처리가 더 좋다.
from collections import deque

n, k = map(int, input().split())
q = deque(list(map(lambda x : [0,int(x)], input().split()))) #[로봇, 내구도]

step = 0
while True:

    step+=1

    #회전
    q.rotate(1)
    if q[n-1][0]==1: #즉시 내림
        q[n-1][0]=0

    #로봇 이동
    for i in range(n-2,-1,-1):
        if q[i][0]==1:
            if q[i+1][0]==0 and q[i+1][1]>0:
                if i==n-2:
                    q[i][0]=0
                    q[i+1][1]-=1
                else:
                    q[i][0]=0
                    q[i+1][0]=1
                    q[i+1][1]-=1

    #로봇 올림
    if q[0][1]>0:
        q[0][0]=1
        q[0][1]-=1

    cnt = 0
    for element in q:
        if element[1]==0:
            cnt+=1
    if cnt >=k:
        break
print(step)