import sys 

class Stack:
    def __init__(self):
        self.arr = []
    def __push__(self, item):
        self.arr.append(item)
    def __pop__(self):
        if not self.__isEmpty__():
            return self.arr.pop(-1) #파이썬에서 -1은 마지막 원소
        else:
            return -1
    def __isEmpty__(self):
        return int(len(self.arr)<=0) #len(self.arr)<=0자체는 False/True가 출력값인데 int()로 변환해주면 0/1로 바뀜 *********
    def __top__(self):
        if not self.__isEmpty__():
            return self.arr[-1]# -1은 마지막 원소
        else:
            return -1
    def __size__(self):
        return len(self.arr)

n = int(sys.stdin.readline())

st = Stack()

for i in range(n):
    st.arr=[]
    arr = sys.stdin.readline()
    arr=arr[:-1]#'\n'개행문자 제거
    for c in arr:
        if c=='(':
            st.__push__(c)
        else:
            if st.__top__()==-1:
                st.__push__(c) # 2.에서 (가 스택에 남으면 NO를 출력하는데 같이 코드에서 처리하려고(43줄) (가 스택에 없고 )남는 경우 그냥 )을 스택에 넣어줌
                break
            else:
                st.__pop__()
    
    if st.__size__() == 0:
        print("YES")
    else:#2의 두가지 경우를 한꺼번에 처리
        print("NO")

#1. 딱 맞아떨어지는 경우
#2. ( 가 남는 경우 혹은 )가 남는 경우

#굉장한 풀이
# a = int(input())
# for i in range(a):
#     b = input()
#     s = list(b)
#     sum = 0
#     for i in s:
#         if i == '(':
#             sum += 1
#         elif i == ')':
#             sum -= 1
#         if sum < 0:
#             print('NO')
#             break
#     if sum > 0:
#         print('NO')
#     elif sum == 0:
#         print('YES')