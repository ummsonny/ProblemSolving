import sys
#print(len(sys.stdin.readline())#이렇게 하면 맨 뒤의 '\n'이 문자열의 일부로 인식된다.
print(len(sys.stdin.readline().rstrip()))