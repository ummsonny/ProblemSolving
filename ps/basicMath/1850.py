import sys
a,b = map(int, sys.stdin.readline().split())

while b!=0:
    a = a%b
    a,b = b,a
print('1'*a)
#유클리드 호제법
