#파이썬은 트리를 딕션너리로 구현한다. so insertNode함수 구현이 필요없다.
import sys
read = sys.stdin.readline
class Node:
    def __init__(self, data,left,right):
        self.left=left
        self.right=right
        self.data=data

def preorder(root):
    print(root.data, end="")
    if root.left != '.':
        preorder(tree[root.left])
    if root.right != '.':
        preorder(tree[root.right])

def inorder(root):
    if root.left != '.':
        inorder(tree[root.left])
    print(root.data, end="")
    if root.right != '.':
        inorder(tree[root.right])


def postorder(root):
    if root.left != '.':
        postorder(tree[root.left])
    if root.right != '.':
        postorder(tree[root.right])
    print(root.data, end="")

tree={}
N = int(read())
for i in range(N):
    data,left,right = read().split()
    tree[data]=Node(data,left,right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])


# for Node in tree.keys():
#     print(tree[Node].left)

