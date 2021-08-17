import sys

#나는 큐 클래스를 만들어서 풀었다. 하지만 안 그런 풀이는 밑에
#함수 만들자

# class Queue:
#     def __init__(self):
#         self.arr=[]
    
#     def __push__(self, input):
#         self.arr.append(input)
#     def __pop__(self):
#         if self.__empty__():
#             return -1
#         else:
#             a = self.arr[0]
#             self.arr=self.arr[1:]
#             return a
#     def __size__(self):
#         return len(self.arr)
#     def __empty__(self):
#         if len(self.arr)<=0:
#             return 1
#         else:
#             return 0
#     def __front__(self):
#         if self.__empty__():
#             return -1
#         else:
#             return self.arr[0]

#     def __back__(self):
#         if self.__empty__():
#             return -1
#         else:
#             return self.arr[-1]


# n = int(input())

# queue = Queue()
# for i in range(n):
#     ans = sys.stdin.readline().split()

#     if ans[0]=='push':
#         queue.__push__(int(ans[1]))
#     elif ans[0]=='pop':
#         print(queue.__pop__())
#     elif ans[0]=='size':
#         print(queue.__size__())
#     elif ans[0]=='empty':
#         print(queue.__empty__())
#     elif ans[0]=='front':
#         print(queue.__front__())
#     elif ans[0]=='back':
#         print(queue.__back__())

# 클래스 안 만든 풀이
n = int(input())

que=[]
for i in range(n):
    ans = sys.stdin.readline().split()

    if ans[0]=='push':
        que.append(ans[1])
    elif ans[0]=='pop':
        if(len(que)<=0):
            print("-1")
        else:
            print(que.pop(0))
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




