import sys

#내 풀이 

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return repr((self.x, self.y))

list = []
n = int(input())
for i in range(n):
    x,y = map(int, input().split())
    list.append(Node(x,y))

list.sort(key = lambda Node : (Node.x,Node.y))
#list.sort(key = lambda Node : Node.x) 19~20줄처럼 따로따로 하면 틀린다. 19의 결과에 20을 적용하는 것이라 틀리다. 즉, x가 같은때 y기준대로 정렬을 못한다. 
# list.sort(key = lambda Node : Node.y) 그래서 18줄 같이 한번에 조건을 주어야한다. 18줄의 말은 x를 기준으로 정렬하고 값이 같을때는 y를 기준으로 정렬하라 라는 뜻!

for i in range(n):
    print(list[i].x,list[i].y)

#---------------------------------------------------------------------------------

#더 좋은 풀이 

#https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline
#왜 input()대신 sys.stdin.readline()으로 입력 받는가?
# n = int(sys.stdin.readline())

# arr=[]
# for i in range(n):
#     arr.append(list(map(int, sys.stdin.readline().split())))

# #https://dailyheumsi.tistory.com/67
# #정렬함수 쓰는 방법!!!!
# arr.sort(key=lambda x : (x[0], x[1]))

# for i in arr:#반복문에는 배열 바로 들어가도 된다 했지? range(n)보다 효율적이다
#     print(i[0],i[1])

#주의!! arr대신 list를 쓰면 34줄에서 안쪽 list가 배열로 바꿔주는 함수가 아니라 내가 생성한 list로 인식해서 오류난다!
#웬만하면 함수 등등 이미 정해진 식별자들은 쓰지말자! 