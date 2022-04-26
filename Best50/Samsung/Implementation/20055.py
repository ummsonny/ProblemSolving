from collections import deque
n,k = map(int, input().split())
arr_up = list(map(lambda x: [int(x),0], input().split())) #내구도, 로봇유무


arr_up = deque(arr_up)

step = 1
while True:

    #한 칸 회전 -> 내리는 칸 검사
    arr_up.rotate(1)
    arr_up[n - 1][1]=0

    #로봇 이동 -> 내리는 칸 검사
    for i in range(n-2,0,-1):
        if arr_up[i][1] == 1 and arr_up[i+1][0] > 0 and arr_up[i+1][1] == 0:
            arr_up[i][1]=0

            arr_up[i+1][0] -=1
            arr_up[i+1][1] = 1
    arr_up[n-1][1] = 0

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