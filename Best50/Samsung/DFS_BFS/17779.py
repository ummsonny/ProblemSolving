n = int(input())
temp = []
for _ in range(n):
    temp.append(list(map(int, input().split())))

graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        graph[i+1][j+1]=temp[i][j]

# 2. 경계선을 만들어
answer = 1e9
def solve(x,y,d1,d2):
    global answer
    boundary = [[0] * (n + 1) for _ in range(n + 1)]
    # 1
    for i in range(d1+1):
        boundary[x+i][y-i]=1
    # 2
    for i in range(d2+1):
        boundary[x+i][y+i]=1
    # 3
    for i in range(d2+1):
        boundary[x+d1+i][y-d1+i]=1
    # 4
    for i in range(d1+1):
        boundary[x+d2+i][y+d2-i]=1
    # for b in boundary:
    #     print(b)
    # print()

    answer_tuple = count(x,y,d1,d2,boundary)
    answer = min(answer,max(answer_tuple)-min(answer_tuple))

# 3. 최대값, 최솟값 구해
def count(x,y,d1,d2,boundary):

    s1,s2,s3,s4,s5 = 0,0,0,0,0
    # 1번 선거구
    for r in range(1,x+d1):
        for c in range(1,y+1):
            if boundary[r][c]==1:
                break
            s1+=graph[r][c]
            boundary[r][c]=-1

    # 2번 선거구
    for r in range(1,x+d2+1):
        # for c in range(y+1,n+1): 이건 안됨!! 사각형을 생각! 경계선 안의 값도 s2에 들어간다.
        for c in range(n,y,-1):
            if boundary[r][c]==1:
                break
            s2+=graph[r][c]
            boundary[r][c]=-1

    # 3번 선거구
    for r in range(x+d1,n+1):
        for c in range(1,y-d1+d2):
            if boundary[r][c]==1:
                break
            s3+=graph[r][c]
            boundary[r][c]=-1

    # 4번 선거구
    for r in range(x+d2+1,n+1):
        # for c in range(y-d1+d2,n+1):이건 안됨!! 사각형을 생각! 경계선 안의 값도 s4에 들어간다.
        for c in range(n,y-d1+d2-1,-1):
            if boundary[r][c]==1:
                break
            s4+=graph[r][c]
            boundary[r][c]=-1

    # 5번 선거구 -> 이 방법 말고 처음에 배열 입력 받을때 전체 인구수 다 더해서 변수에 저장한다음 s1~s4빼서 구해도 됨
    for r in range(1,n+1):
        for c in range(1,n+1):
            if boundary[r][c]==-1:
                continue
            s5+=graph[r][c]

    return s1,s2,s3,s4,s5


# 1. 경우의 수
for x in range(1, n + 1):
    for y in range(1, n + 1):
        for d1 in range(1, n + 1):
            for d2 in range(1, n + 1):
                # 무조건 만족인 것을 제외하고 생각! 아래 3 조건이 여기서 문제풀이의 핵심!
                if x + d1 + d2 > n:
                    continue
                if y + d2 > n:
                    continue
                if y - d1 < 1:
                    continue
                solve(x, y, d1, d2)
print(answer)