from itertools import combinations

n = int(input())
board = []
teachers=[]
spaces=[]

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j]=='T':
            teachers.append((i,j))
        if board[i][j]=='X':
            spaces.append((i,j))

def watch(x,y,direction):

    if direction==0: #왼쪽방향
        while y>0:
            if board[x][y]=='S': #학생인 경우
                return True
            if board[x][y]=='O': #장애물인 경우
                return False
            y-=1
    
    if direction==1: #오른쪽방향
        while y<n:
            if board[x][y]=='S': #학생인 경우
                return True
            if board[x][y]=='O': #장애물인 경우
                return False
            y+=1

    if direction==2: #위쪽방향
        while x>0:
            if board[x][y]=='S': #학생인 경우
                return True
            if board[x][y]=='O': #장애물인 경우
                return False
            x-=1

    if direction==3: #아래쪽방향
        while x<n:
            if board[x][y]=='S': #학생인 경우
                return True
            if board[x][y]=='O': #장애물인 경우
                return False
            x+=1

    return False #장애물도 없고 못찾았을때

def process():

    for x,y in teachers:

        for i in range(4):
            if watch(x,y,i):
                return True

    return False

find = False

for data in combinations(spaces, 3):

    for x,y in data:
        board[x][y]='O' #장애물 설치

    if not process(): # 학생 못찾음
        find = True
        break;

    for x,y in data:
        board[x][y]='X' #장애물 다시 제거

if find:
    print('YES')
else:
    print('NO')

# 내풀이 -> combination 라이브러리 안씀 DFS로 푼거임
n = int(input())
graph = []
teacher = []

for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j]=='T':
            teacher.append((i,j))

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def check(x,y,direction):

    while 0<=x<n and 0<=y<n:

        if graph[x][y]=='S':
            return True
        if graph[x][y]=='O':
            return False

        x = x+dx[direction]
        y = y+dy[direction]

    return False

def find():

    for x,y in teacher:
        for i in range(4):
            if check(x,y,i):
                return True

    return False

answer = True
def dfs(sx,sy,count):
    global answer

    if count ==3:

        if find()==False:
            answer = False
        return

    for i in range(sx,n):
        sy = sy if sx==0 else 0
        for j in range(sy,n):
            if graph[i][j]=='X':
                graph[i][j]='O'
                dfs(sx,sy+1,count+1)
                graph[i][j]='X'
dfs(0,0,0)

if answer:
    print('NO')
else:
    print('YES')