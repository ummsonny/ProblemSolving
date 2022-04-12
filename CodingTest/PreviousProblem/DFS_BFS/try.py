from cgi import test
import copy
n = int(input())

graph = []
teachers = []

for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == 'T':
            teachers.append((i,j))
# 조합 문제임

def check():
    
    for teacher in teachers:
        #왼쪽 방향 보자!
        x,y = teacher
        while y>=0:
            if graph[x][y]=='S':
                return True
            elif graph[x][y]=='O':
                break
            y-=1
            
        #위쪽 방향 보자!
        x,y = teacher
        while x>=0:
            if graph[x][y]=='S':
                return True
            elif graph[x][y]=='O':
                break
            x-=1

        #오른쪽 방향 보자!
        x,y = teacher
        while y<n:
            if graph[x][y]=='S':
                return True
            elif graph[x][y]=='O':
                break
            y+=1

        #아래쪽 방향 보자!
        x,y = teacher
        while x<n:
            if graph[x][y]=='S':
                return True
            elif graph[x][y]=='O':
                break
            x+=1

    return False # 



find = True

def dfs(count):
    global find

    if count == 3:
        if not check(): #학생 안걸림
            find = False
        return
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                dfs(count+1)
                graph[i][j] = 'X'

dfs(0)

if find:
    print('NO')
else:
    print('YES')