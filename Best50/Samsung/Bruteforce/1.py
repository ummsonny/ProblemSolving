from copy import deepcopy

n,m = map(int, input().split())

graph=[]
location = [[0,0],[0,0],[0,0]]

for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == 'R':
            location[1] = [i,j]
        elif graph[i][j] == 'B':
            location[2] = [i,j]
        elif graph[i][j] == 'O':
            location[0] = [i,j]

#좌우상하
dx = [0,0,-1,1]
dy = [-1,1,0,0]

left,right,up,down = 10,10,10,10
candidate = []

def move():

    copy_location = deepcopy(location)

    for a in range(10):

        while True:

            if 

        #다음 칸이 .이면 움직여
        
            #그러다가 갑자기 홀을 만나면 

def dfs(count):
    global left,right,up,down

    if count == 10:
        return
    
    if left >0:
        left-=1
        candidate.append(0)
        dfs(count+1)
        left+=1
        candidate.pop()
    
    if right >0:
        right-=1
        candidate.append(1)
        dfs(count+1)
        right+=1
        candidate.pop()
    
    if up >0:
        up-=1
        candidate.append(2)
        dfs(count+1)
        up+=1
        candidate.pop()

    if down >0:
        down-=1
        candidate.append(4)
        dfs(count+1)
        down+=1
        candidate.pop()