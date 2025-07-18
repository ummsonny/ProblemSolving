# 구현

## 설명
- 구현이란 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정
- 어떻게 보면 구현은 모든 범위의 코테 문제 유형을 포함하는 개념 
    - so 구현은 별도의 유형이라고 하기 어렵다
- 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 유형
- 구현은 코드가 길거나, 특점 소수점 자리까지 출력, 문자열을 문자단위로 파싱하는 문제 등 **까다로운** 문제를 의미한다.
---
## 구현 시 고려해야 할 제약 사항

### <자료형>
- c/c++/Java 와 다르게 파이썬은 직접 자료형 지정 안함
    - 정수형 변수의 연산 때문에 고민 할일 없음
- But 실수형 변수는 다른 언어처럼 유효숫자에 따라 연산 결과가 원하는 값이 나오지 않을 수 있음 (하지만 걱정 ㄴㄴ)

### <리스트 크기 - 메모리>
- 코테에서 보통 128~512MB로 메모리 제한
- **리스트 여러 개 선언시, 크기가 1000만 이상인 리스트가 있다면 메모리 용량 제한으로 풀 수 없게 되는 경우도 있당**
    - **하지만 드물다**
    - 코테는 복잡한 최적화 요구 안함으로 제한 메모리량 보다 적게 쓰면 된다는 점만 알아뒁
##### **int 자료형 데이터의 개수에 따른 메모리 사용량**
|데이터 개수(리스트 길이)|메모리 사용량|
|------|---|
|1,000|약 4KB|
|1,000,000|약 4MB|
|10,000,000|약 40MB|

### <채점 환경 - 시간>
- 코테에서 시간 제한 1초 및 메모리 제한 128MB 같은 조건있음
- **2020기준 파이썬3.7으로 1초에 2000만번**
    - 2000만 번 연산안에 풀어랏!
    - EX) 시간제한 1초 + 데이터 개수 100만개 => 2000만 번 연산을 위해서는 시간 복잡도(O(NlogN))
        - so 코테에서 시간제한과 데이터 개수를 통해 어느 정도의 시간 복잡도의 알고리즘으로 작성해야 풀 수 있는지 예측해야한다.
- **Pypy3은 1초에 2000만 번 ~ 1억 번 연산 가능**
    - c/c++만큼 빠르다
    - Pypy3가 코테에 있다면 이거 써라!

---

## 구현문제 유형
### 시뮬레이션
- 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행
- 일련의 명령에 따라서 그냥 하면 됨
### 완전 탐색(브루스포스)
- 모든 경우의 수를 주저 없이 다 계산하는 방법
- 완탐은 **비효율적 시간 복잡도**를 가지고 있으므로 데이터 가 큰 경우에 못 쓴다. 
    - **So 확인(탐색)할 전체 데이터 개수(N)가 100만 개 이하일 때 적절**
- **DFS 혹은 BFS로 해결**
    - **파이썬의 itertools 사용!!!!!!**
---
## 기출
### 프로그래머스
#### 완전 탐색(브루스포스)
[외벽점검](https://school.programmers.co.kr/learn/courses/30/lessons/60062)
<br>
[자물쇠와 열쇠](https://school.programmers.co.kr/learn/courses/30/lessons/60059)
<br>
[뱀](https://www.acmicpc.net/problem/3190)
<br>
[기둥과 보 설치](https://school.programmers.co.kr/learn/courses/30/lessons/60061)
<br>
[치킨 배달](https://www.acmicpc.net/problem/15686)