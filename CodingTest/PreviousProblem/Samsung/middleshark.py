import copy

array = [[None]*4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))

    for j in range(4):
        array[i][j] = [data[j*2], data[j*2+1]-1]


dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]


def turn_left(direction):
    return (direction+1)%8

result = 0 #최종결과

def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i,j)
    return None

def move_all_fishes(array, now_x, now_y):

    for i in range(1,17):
        position = find_fish(array, i)
        if position!=None:
            x,y = position[0], position[1]
            direction = array[x][y][1]

            for j in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]

                if 0<=nx<4 and 0<=ny<4 and (nx!=now_x or ny!=now_y):
                    array[x][y][1] = direction
                    array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                    break

                direction = turn_left(direction)

def get_possible_positions(array, now_x, now_y):

    positions = []
    direction = array[now_x][now_y][1]

    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]

        if 0<=now_x<4 and 0<=now_y<4:
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))

    return positions

def dfs(array, now_x, now_y, total): #특정 상태(노드)의 상황을 담고 있어야 다시 돌아왔을때 상황이 같다. 매개변수 모두 다!

    global result

    array = copy.deepcopy(array) #특정 상태(노드)의 상황을 담고 있어야 다시 돌아왔을때 상황이 같으므로 total도 마찬가지

    total += array[now_x][now_y][0] #특정 상태(노드)의 상황을 담고 있어야 다시 돌아왔을때 상황이 같으므로 total도 마찬가지
    array[now_x][now_y][0] = -1

    move_all_fishes(array, now_x, now_y)

    positions = get_possible_positions(array, now_x, now_y)

    if len(positions) == 0:
        result = max(result, total)
        return

    for next_x, next_y in positions: # 같은 상태(노드) 존재하지 않으므로 visited가 없다.
        dfs(array, next_x, next_y, total) 

dfs(array, 0,0,0)
print(result)


'''
# 상황 복구 방법
1.
    특정 상태(노드)의 상황을 담고 있어야 다시 돌아왔을때 상황이 같다. 즉 나만의 상태가 필요하다!
    그래서 매개변수로 넘겨준다. 그리고 그 매개변수를 담을 지역변수가 존재한다.
2. 
    dfs후에 복구 시키는 코드 넣는다. 

# 똑같은 상황이 존재하지 않는다면 visited가 없어도 된다.
'''