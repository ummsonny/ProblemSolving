import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    array = list(map(int, input().split()))
    answer = 0
    for a in array:
        if a % 2 != 0:
            answer += a

    print('#{} {}'.format(test_case, answer))

