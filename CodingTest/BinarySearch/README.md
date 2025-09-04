# BinarySearh

## 순차 탐색

### what?
- 리스트 안에 있는 특정 데이터를 찾기 위해 데이터 **정렬 여부와 상관 없이** **앞에서부터** 데이터를 하나씩 차례대로 확인하는 방법
- 시간 복잡도 : O(N)
### why?
- 시간만 충분하다면 데이터가 아무리 많아도 찾을 수 있다.
### when?
- 보통 **정렬되지 않은** 리스트에서 데이터를 찾을 때 사용!
1. 리스트에 특정 값이 있는지 체크 할 때
2. 리스트에서 특정 값을 가지는 원소의 개수를 찾는 count() 메서드를 이용할 때도 순차탐색으로 이뤄진다.
---
## 이진 탐색

### what?
- 배열 내부가 **정렬되어** 있을 때 특정 데이터를 찾는 방법
- 시작점,끝점,중간점을 나타내는 3개의 변수 사용
- 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교하는 알고리즘!
- 시간 복잡도 : O(logN)
### How?
1. 재귀 함수
```python
# 이진 탐색 소스코드 구현 (재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

```
2. 반복문
```python
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# 밑에는 재귀와 동일
```
3. bisect 모듈(이진 탐색 라이브러리)
```python
from bisect import bisect_left, bisect_right

def count_by_value(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index-left_index
    
n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_value(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)
```
4. c++ 모듈(이진 탐색 라이브러리)
<br>
두 함수 모두 정렬된(**오름차순**) 컨테이너에서만 정확하게 동작
- lower_bound(begin, end, value)

    - value **이상(≥)**인 첫 번째 원소를 가리키는 이터레이터 반환

- upper_bound(begin, end, value)

    - value **초과(>)**하는 첫 번째 원소를 가리키는 이터레이터 반환

- 용도
    1. 정렬된 배열에서 값의 삽입 위치 찾기

    2. 특정 값의 등장 범위 찾기

        - count = upper_bound - lower_bound 로 개수 구하기

    3. 중복된 값 처리 (equal_range와 비슷)
```c++
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> vec = {1, 2, 4, 4, 4, 5, 6};

    auto lower = std::lower_bound(vec.begin(), vec.end(), 4);
    auto upper = std::upper_bound(vec.begin(), vec.end(), 4);

    std::cout << "lower_bound(4)의 인덱스: " << (lower - vec.begin()) << '\n';  // 2
    std::cout << "upper_bound(4)의 인덱스: " << (upper - vec.begin()) << '\n';  // 5

    std::cout << "lower_bound 값: " << *lower << '\n';  // 4
    std::cout << "upper_bound 값: " << *upper << '\n';  // 5

    return 0;
}

```

### when?
- 코테에서 이진 탐색은 탐색 범위가 큰 상황에서 사용
1. 탐색 범위가 **2000만**을 넘어가면 이진 탐색으로 접근!
2. 처리할 데이터의 개수나 값이 **1000만** 단위 이상으로 넘어갈 때! 
---
## 트리 자료구조
---
## 이진 탐색 트리
---
## 빠르게 입력 받기
- 이진 탐색 문제는 입력 데이터 혹은 탐색 범위가 매우 넓다
- 이 경우 input()보다 sys라이브러리의 **readline()** 함수를 사용하여 시간초과를 해결할 수 있다.
    - 단, 줄 바꿈 기호 제거를 위해 **rstrip()**과 함께 써라
```python
import sys

# 하나의 문자열 데이터 입력 받기
input_data = sys.stdin.readline().rstrip()
# 입력 받은 문자열 그대로 출력하기
print(input_data)
```
---
## 파라메트릭 서치
### what?
- 원하는 조건에 가장 알맞는 값을 찾는 문제
- Ex) "특정 범위 내에서 조건을 만족하는 가장 큰 값을 찾아라!"

### How?
- 코테에서는 파라메트릭 서치 문제를 보통 이진 탐색으로 해결한다.
- 보통 이진 탐색을 이용한 파라메트릭 서치 문제는 재귀보다는 반복문으로 해결한다.
---
## 실전 문제 1
- 이진 탐색
- 계수 정렬
- 집합 자료형
    - 단순히 특정 데이터가 존재하는지 검사할 때 매우 효과적인 방법
## 실전 문제 2
- 파라메트릭 서치
## 기출문제
### 백준
[공유기 설치](https://www.acmicpc.net/problem/2110)
### 프로그래머스
[입국심사](https://school.programmers.co.kr/learn/courses/30/lessons/43238)
<br>
[징검다리 건너기](https://school.programmers.co.kr/learn/courses/30/lessons/64062)
<br>
[선입 선출 스케줄링](https://school.programmers.co.kr/learn/courses/30/lessons/12920)