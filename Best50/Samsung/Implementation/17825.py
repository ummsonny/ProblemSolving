# 포인터 개념이 쓰였다. 즉, 배열안에 다른 인덱스를 넣어 참조한다.
import sys

input = sys.stdin.readline

a = [0 for _ in range(33)]
for i in range(21):
    a[i] = i+1
a[21] = 21
a[22], a[23], a[24] = 23, 24, 30
a[25], a[26] = 26, 30
a[27], a[28], a[29] = 28, 29, 30
a[30], a[31], a[32] = 31, 32, 20

move_in = [0 for _ in range(16)]
move_in[5], move_in[10], move_in[15] = 22, 25, 27

plus = [0 for _ in range(33)]
for i in range(1, 21):
    plus[i] = i * 2
plus[22], plus[23], plus[24] = 13, 16, 19
plus[25], plus[26] = 22, 24
plus[27], plus[28], plus[29] = 28, 27, 26
plus[30], plus[31], plus[32] = 25, 30, 35

def dfs(dice_index, ans):
    global max_ans
    if dice_index == 10:
        max_ans = max(max_ans, ans)
        return

    for i in range(4):
        x, x0, move = chess[i], chess[i], dice[dice_index]

        if x == 5 or x == 10 or x == 15:
            x = move_in[x]
            move -= 1

        #================================
        if x + move <= 21: # 제일 외곽 둘레 있을때 혹은 도착지점에 딱 도착할때
            x += move
        else:
            for _ in range(move): # 한번 꺾여서 들어갔을 때 혹은 도착지점을 넘을 때
                x = a[x] # 포인터니까
        #================================

        if c[x] and x != 21:
            continue

        c[x0], c[x], chess[i] = 0, 1, x
        dfs(dice_index + 1, ans + plus[x])
        c[x0], c[x], chess[i] = 1, 0, x0

dice = list(map(int, input().split()))
chess = [0 for _ in range(4)]
c = [0 for _ in range(33)]

max_ans = 0
dfs(0, 0)
print(max_ans)