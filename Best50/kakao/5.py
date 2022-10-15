def execute(cmd,graph,print):


    temp = cmd.split()
    if temp[0]=='UPDATE':
        if len(cmd)>3: #1번
            graph[temp[1]][temp[2]]=temp[3]
        else: #2번
            for i in range(50):
                for j in range(50):
                    if graph[i][j]==temp[1]:
                        graph[i][j] = temp[2]
    elif temp[0]=='MERGE': #3번
        r,c = temp[1],temp[2]
        x,y = temp[3],temp[4]
    elif temp[0]=='UNMERGE':#4번
        r,c = temp[1],temp[2]
    else: #5번
        print.append(graph[temp[1]][temp[2]])


def solution(commands):
    graph = [['EMPTY']*50 for _ in range(50)]
    color = [[0]*50 for _ in range(50)]
    color_element=1

    answer = []
    return answer