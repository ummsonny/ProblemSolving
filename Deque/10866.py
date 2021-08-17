import sys

n = int(input())

que=[]
for i in range(n):
    ans = sys.stdin.readline().split()

    if ans[0]=='push_front':
        que.insert(0,ans[1])#append는 뒤에 넣기 때문에 insert로 위치를 맨 앞으로 지정해주면서 넣는다. 또는 appendleft(ans[1])도 됨
    elif ans[0]=='push_back':
        que.append((ans[1]))#extend를 쓰면 안되는 이유가 extend(매개변수)에서 매개변수는 list가 들어간다. 그래서 extend("soo")라면 [s,o,o]로 바뀜 
    elif ans[0]=='pop_front':
        if(len(que)<=0):print("-1")
        else:print(que.pop(0))
    elif ans[0]=='pop_back':
        if(len(que)<=0):print("-1")
        else:print(que.pop())#인덱스 안쓰면 맨 뒤에꺼 뺌
    elif ans[0]=='size':
        print(len(que))
    elif ans[0]=='empty':
        print(int(len(que)<=0))
    elif ans[0]=='front':
        if(len(que)<=0):
            print("-1")
        else:
            print(que[0])
    elif ans[0]=='back':
        if(len(que)<=0):
            print("-1")
        else:
            print(que[-1])