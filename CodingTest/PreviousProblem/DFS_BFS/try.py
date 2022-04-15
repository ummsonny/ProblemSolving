from collections import deque

def state(next_state, board):

    next_state = list(next_state)
    print('hello')
    x1, y1, x2, y2 = next_state[0][0], next_state[0][1], next_state[1][0], next_state[1][1]
    length = len(board)
    candidates = [] #갈 수 있는 상태 넣어놓기

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(4):
        nx1 = x1 + dx[i]
        ny1 = y1 + dy[i]
        nx2 = x2 + dx[i]
        ny2 = y2 + dy[i]

        if 0<=nx1<length and 0<=ny1<length and 0<=nx2<length and 0<=ny2<length:
            if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
                candidates.append({(nx1,ny1),(nx2,ny2)})

    # 회전
    #1. 가로로 있다면
    if x1 == x2:
        # 위쪽으로 회전
        if (x1-1 >= 0) and board[x1-1][y1] == 0 and board[x2-1][y2] == 0:
            candidates.append({(x1,y1),(x1-1,y1)})
            candidates.append({(x2,y2),(x2-1,y2)})
        # 아래쪽으로 회전
        if (x1+1 < length) and board[x1+1][y1] == 0 and board[x2+1][y2] == 0:
            candidates.append({(x1,y1),(x1+1,y1)})
            candidates.append({(x2,y2),(x2+1,y2)})

    #2. 세로로 있다면
    elif y1 == y2:
        # 왼쪽으로 회전
        if (y1-1>=0) and board[x1][y1-1] == 0 and board[x2][y2-1] == 0:
            candidates.append({(x1,y1),(x1,y1-1)})
            candidates.append({(x2,y2),(x2,y2-1)})
        if (y1+1<length) and board[x1][y1+1] == 0 and board[x2][y2+1] == 0:
            candidates.append({(x1,y1),(x1,y1+1)})
            candidates.append({(x2,y2),(x2,y2+1)})
    return candidates

def solution(board):
    q = deque()
    visited_state = []
    n = len(board)

    pose = {(0,0),(0,1)}
    q.append((pose, 0))

    while q:

        next_state, cost = q.popleft()

        if (n-1,n-1) in next_state:
            return cost

        for next_state in state(next_state, board):
            if next_state not in visited_state:
                visited_state.append(next_state)
                q.append((next_state,cost+1 ))

    return 
