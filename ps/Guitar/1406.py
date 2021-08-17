import sys
# arr = sys.stdin.readline()[:-1]
# n = int(sys.stdin.readline())
# cur = len(arr)

# for i in range(n):
#     com = sys.stdin.readline().split()
#     if com[0]=='L':#왼쪽으로
#         if not cur==0:
#             cur-=1
#     elif com[0]=='D':#오른쪽으로
#         if not cur==len(arr):
#             cur+=1
#     elif com[0]=='B':#왼쪽 삭제cursor값 하락
#         if not cur==0: 
#             arr = arr[:cur-1]+arr[cur:]
#             cur-=1
#     elif com[0]=='P':#왼쪽에 추가cursor값 상승
#         if cur==0:
#             arr = com[1]+arr
#             cur+=1
#         else:
#             arr = arr[:cur]+com[1]+arr[cur:]
#             cur+=1

# print(''.join(arr))
# 문자열 슬라이싱은 [a:b] 라면 O(b-a)가 걸린다. 즉 O(n)이라는 것이다. 그래서 시간복잡도가 너무 높다.

#개선된 코드
stackA= list(sys.stdin.readline()[:-1])
stackB = []
n = int(sys.stdin.readline())

for i in range(n):
    com = sys.stdin.readline().split()
    if com[0]=='L':#왼쪽으로
        if stackA:
            stackB.append(stackA.pop())          
    elif com[0]=='D':#오른쪽으로
        if stackB:
            stackA.append(stackB.pop())
    elif com[0]=='B':#왼쪽 삭제cursor값 하락
        if stackA: 
            stackA.pop()
    elif com[0]=='P':#왼쪽에 추가cursor값 상승
            stackA.append(com[1])

print(''.join(stackA)+''.join(reversed(stackB)))
#1. 슬라이싱 대신 스택을 사용
#2. if 배열 : //리스트가 비어있는지 확인하는 방법 https://codechacha.com/ko/python-check-empty-list/
#3. 38줄에서 stackB.insert(0, stackA.pop())은 O(n)이므로 O(1)인 append로 바꿈 --> stackA와 stackB가 마주보고 있는 것이아니라  ------[ cur ]-------
#등 돌리고 있다. ------[ cur ------[ , 그래서 마지막에 stackB를 reversed를 해주는 것이다. 
