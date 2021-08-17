import sys

lines = sys.stdin

for line in lines:
    A, B = map(int, line.split())
    if A==0 and B==0:
        break;
    print(A+B)