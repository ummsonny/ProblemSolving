# Sorting

## 정렬

### what?
- 데이터를 특정한 기준에 따라서 순서대로 나열하는 것
- 정렬은 이진탐색의 전처리 과정!
- 앞으로 오름차순 정렬을 수행한다고 가정!
    - 내림차순은 리스트 뒤집는 연산만 하면된다 -> O(N)의 복잡도
---
## 선택 정렬

### what?
- **가장 작은 데이터를 선택해 맨 앞에 두는 과정을 반복**
- 가장 원시적인 방법으로 매번 가장 작은 것을 선택한다는 의미에서 선택정렬임
### how?
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)
```
### 시간복잡도
- 비교연산 : N+(N-1)+(N-2)+...+2 = N*(N+1)/2
- **O(N^2)**
- 데이터 개수가 10,000개 이상이면 정렬 속도가 아주 급격히 느려짐
---
## 삽입 정렬

### what?
- 선택 정렬보다 효율적
- 삽입 정렬은 필요할 때만 위치를 바꾸므로 **데이터가 거의 정렬**되어 있을 때 훨씬 효율적
- 삽입 정렬은 특정한 데이터를 적절한 위치에 **삽입**한다는 의미에서 삽입 정렬이라고 한다.
- **특정 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬 되어 있다고 가정한다.**

### how?
- 두 번째 데이터부터 시작한다!(첫 번째 데이터는 그 자체로 정렬되어 있다고 판단)
- **정렬 되지 않은 부분 -> 정렬 되어 있는 부분에 적절히 삽입**
    - 정렬 된 부분은 항상 정렬이 된 상태
    - 그러므로 데이터를 삽입할 때 작은 데이터를 만나면 거기서 멈추면 된다.
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)
```
### 시간 복잡도
- 최악의 경우 -> O(N^2)
- 최선의 경우 -> O(N)
- 퀵 정렬보다 보통 비효율적이나, **정렬이 거의 되어 있는 상황**에서는 더 강력함
    - **거의 정렬되어 있는 상태**라면 다른 정렬 알고리즘 보타 삽입 정렬 이용하는 것이 효율적!
---
## 퀵 정렬
### what?
- 가장 많이 사용되는 알고리즘
- 퀵 정렬과 병합 정렬이 제일 좋다. 
- **기준 데이터(피벗)**를 설정하고 피벗보다 작은 리스트와 큰 리스트로 나누는 과정을 반복하여 정렬하는 알고리즘

### how?
- 호어 분할 : 리스트에서 첫 번째 데이터를 피벗으로 설정
1. 피벗 설정
2. 왼쪽에서부터 피벗보다 큰 데이터 찾는다.
3. 오른쪽에서부터 피벗보다 작은 데이터를 찾는다.
4. 2,3에서 찾은 데이터를 서로 위치 교환
5. 위치가 엇갈릴 때까지 2,3,4 반복
    - 엇갈린 위치에 피벗 옮김
6. 피벗 기준으로 나뉜 2개 리스트 각각 퀵 정렬 수행(1번으로 돌아감)
```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복 
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

# 파이썬 장점을 살린 퀵 정렬 소스코드
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
```
### 시간 복잡도
- 평균 시간 복잡도는 O(NlogN)
- 최악의 경우 O(N^2)
    - 데이터가 **무작위**로 입력될 경우 퀵 정렬은 빠르게 동작할 확률이 높다.
    - But, **호어 분할** + **이미 데이터가 정렬된 경우**에는 매우 느리게 동작
---
## 계수 정렬

### what?
- 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘
    - 조건1
        - 데이터의 크기범위가 제한 : 최대값과 최솟값의 차이가 1,000,000을 넘지 않을 때
    - 조건2
        - 데이터가 정수 일때
- 위와 같은 조건이 붙는 이유
    - 모든 범위를 담을 수 있는 크기의 리스트(배열)를 선언해야함으로

### how?
```python
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
```
### 시간 복잡도
- 데이터 개수 : N, 데이터 중 최대값이 K 라면
    - 최악의 경우에도 O(N+K)
    - N : 입력 데이터를 하나씩 확인하면서 리스트에서 적절한 인덱스의 값을 1씩 증가
    - K : 리스트의 각 인덱스에 해당하는 값들을 확인할 때 데이터 중 최대값의 크기만큼 반복(리스트의 크기가 max(array)+1 이므로)
### 공간 복잡도
- 입력 데이터가 0와 999,999 2개라면 리스트의 크기가 100만이 되도록 설정해야함
    - 메모리상 심각한 비효율
- So, 계수정렬은 **데이터 크기가 한정** + **데이터 중복이 많을 때** 효율적
    - Ex) 성적의 경우 100점을 맞은 학생이 여러 명일 수 있기 때문에 계수 정렬이 효과적!
- But **데이터 특성을 파악이 어렵다면** 일반적으로 퀵정렬이 효율적

---
## 파이썬 정렬 라이브러리

## sorted(), sort()
### what?
- 병합 정렬을 기반
### how?
```python
# 1. sorted()
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)

# 2. sort()
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

array.sort()
print(array)
```
- sorted() : 정렬된 리스트를 반환
- sort() : 반환X, 원본을 건드림
```python
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)
```
- sorted()나 sort()는 key매개변수를 입력으로 받을 수 있다.
- key매개변수는 정렬 기준!
    - 람다 함수도 사용 가능(부록 참고)
### 시간 복잡도
- 최악의 경우에도 O(NlogN)을 보장
- 병합 정렬과 삽입 정렬이 섞인 하이브리드 방식의 알고리즘을 사용
---
## 실전 팁! - 3가지 유형
1. 정렬 라이브러리로 푸는 문제
    - 단순히 정렬를 요구하는 문제
2. 정렬 알고리즘의 원리에 대해 물어보는 문제
    - 선택, 삽입, 퀵 정렬 등의 원리를 알아야 풀 수 있다.
3. 더 빠른 정렬이 필요한 문제
    - 퀵 정렬 기반의 정렬 기법으로 못 품
    - 계수 정렬 등 다른 정렬 알고리즘을 쓰거나 기존 알고리즘의 구조적 개선을 거처야 풀 수 있다.
---
## 추가사항
- 병합 정렬은 일반적으로 퀵 정렬보다는 느리다.

