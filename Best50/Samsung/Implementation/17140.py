r,c,k = map(int, input().split())

graph=[]
for _ in range(3):
    graph.append(list(map(int, input().split())))

answer = 0
def caclutate(row, column, graph):

    max_colum, max_column_num = -1,-1

    for i in range(row):
        # R 연산
        count = [0] * 101
        temp = []
        for j in range(column):
            if graph[i][j] > 0:
                count[graph[i][j]] += 1
        for num in range(1, 101):
            if count[num] > 0:
                temp.append((num, count[num]))
        temp.sort(key=lambda x: (x[1], x[0]))

        # 만약 100보다 크면 줄여!
        if len(temp)>50:
            temp = temp[50:]

        graph[i] = []
        for num, numcnt in temp:
            graph[i] += [num, numcnt]

        length = len(graph[i])
        if length > max_colum:
            max_colum = length
            max_column_num = i

    for i in range(row):
        if i == max_column_num:
            continue
        else:
            plus = [0] * (max_colum - len(graph[i]))
            graph[i] += plus

def right_rot90(a):
    n = len(a)
    m = len(a[0])
    new_a = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_a[j][n-1-i] = a[i][j]
    return new_a
def left_rot90(a):
    n = len(a)
    m = len(a[0])
    new_a = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_a[m-1-j][i] = a[i][j]
    return new_a

while True:

    row = len(graph)
    column = len(graph[0])

    if 0<=r-1<row and 0<=c-1<column and graph[r-1][c-1]==k: # 0<=r-1<row and 0<=c-1<column 조건 없으면 indexError난다
        print(answer)
        break
    if answer == 100:
        print(-1)
        break

    # 행, 열 크기 비교
    if row>=column: # 행이 크거나 같은때
        caclutate(row, column, graph)

    else: # 열이 클때
        graph = left_rot90(graph)
        caclutate(column,row,graph)
        graph = right_rot90(graph)

    answer +=1