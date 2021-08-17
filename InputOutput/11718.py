import sys

for line in sys.stdin:
    print(line, end='')

# HelloBaekjoonOneline Judge 이렇게 예상할 수 있는데
#애초에 Hello\n , Baekjoon\n Oneline Judge\n 이런식으로
#각 라인마다 마지막에 개행문자가 있는 상태로 입력되므로 
#정답이 잘나온다. 
#즉, Hello\nBaekjoon\nOneline Judge\n 이게 정답이다.
#11719번 문제도 이 코드가 정답임