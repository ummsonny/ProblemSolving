import sys
n = int(input())

for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    A,B = a,b
    while b!=0:
        a = a%b
        a,b = b,a
    print(A*B//a)