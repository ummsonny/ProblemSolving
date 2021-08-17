# 내 코드 
def fuc(a,b):
    if(b==0):
        return a;
    else:
        return fuc(b, a%b)


a,b = map(int, input().split())

min = fuc(a,b)
#max = (a//min)*(b//min)*min
max = a*b//min #이게 더 깔끔 

print(min)
print(max)

# 갈끔한 코드
import sys
A,B = map(int, sys.stdin.readline().split())
a,b = A,B

while b!=0:
    a = a%b
    a,b = b,a

print(a)
print(A*B//a)