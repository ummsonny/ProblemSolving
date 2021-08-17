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

n = int(input())
st = Stack()

for i in range(n):
    a = sys.stdin.readline().split() #배열로 받아버림이 포인트

    
    if a[0]=='push':
        st.__push__(int(a[1]))
    elif a[0]=='pop':
        print(st.__pop__())
    elif a[0]=='size':
        print(st.__size__())
    elif a[0]=='empty':
        print(st.__isEmpty__())
    elif a[0]=='top':
        print(st.__top__())