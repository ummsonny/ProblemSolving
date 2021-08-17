import sys

lines = sys.stdin

for line in lines:
    A, B = map(int, line.split())
    print(A+B)


#https://dojang.io/mod/page/view.php?id=2286 : 맵 객체
#https://sozerodev.tistory.com/30 : 풀이