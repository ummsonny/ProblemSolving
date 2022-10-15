from collections import deque
class Node:
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None

class BinaryTree():
    def __init__(self):
        self.root=None

def makeBinaryNum(n, arr):
    x, y = divmod(n, 2)
    arr.append(y)
    if x == 0:
        return arr
    else:
        return makeBinaryNum(x, arr)
def buildTree(arr):

    if not arr:
        return

def solution(numbers):

    for num in numbers:

        # 먼저 이진수로 만들어
        arr = []
        binary = makeBinaryNum(num,arr)

        # 트리 만들어
        buildTree(deque(arr))

    answer = []
    return answer