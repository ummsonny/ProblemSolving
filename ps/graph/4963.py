import sys
sys.setrecursionlimit(10000)#이거 쓸데없이 크게 하면 메모리 초과 난다. 명심해랏!!!
dx=[-1,0,1,0,-1,1,1,-1]
dy=[0,1,0,-1,-1,-1,1,1]

def dfs(y,x):
    graph[y][x]=0 #-1도 가능
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or nx>=w or ny<0 or ny>=h:
            continue
        if graph[ny][nx]==1:
            dfs(ny,nx)



while True:
    island_num=0
    w,h = map(int,sys.stdin.readline().split())
    if w==0 and h==0:
        break;
    graph=[]
    
    #그래프 만들기
    #1.
    # for _ in range(h):
    #     graph.append(list(map(int, input().split())))
    #2.
    # graph = [list(map(int, input().split())) for _ in range(h)]
    #3. 1번이랑 i <-> _ 만 다르다.
    for i in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))

    #visited = [[0]*w for i in range(h)] #이거 있으면 오히려 메모리 초과될 수있다. 이거 없이도 방문했다면 0(-1도가능)으로 graph를 바꾼다. 이미 방문한 곳은 없던 곳으로 만들 수 있자나

    for i in range(w):
        for j in range(h):
            if graph[j][i]==1:
                dfs(j,i)
                island_num+=1
    print(island_num)
