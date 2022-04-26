from collections import deque

wheel = [deque([0,0,0,0,0])]
for _ in range(4):
    wheel.append(deque(list(map(int, input()))))

k = int(input())


def move_left(number, direction):

    if number == 1:
        return

    if wheel[number-1][2] != wheel[number][6]:
        move_left(number-1, -direction)
        wheel[number-1].rotate(direction)


def move_right(number, direction):

    if number >= 4:
        return

    if wheel[number][2] != wheel[number+1][6]:
        move_right(number + 1, -direction)
        wheel[number + 1].rotate(direction)

for i in range(k):
    number, direction = map(int, input().split())
    #왼쪽
    move_left(number, -direction)
    #오른쪽
    move_right(number, -direction)

    wheel[number].rotate(direction)

result = 0
for i in range(1,5):
    if wheel[i][0] == 1:
        result += 2**(i-1)

print(result)