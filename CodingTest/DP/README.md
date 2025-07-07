# DP
## 왜 DP를 사용?
- 컴퓨터를 활용해도 많은 시간 또는 공간을 필요로 하여 해결하기 어려운 문제의 존재로 인해
- **메모리 공간을 약간 더 활용하면 연산 속도를 비약적으로 증가시킬 수 있는 방법이 DP이다.**
    - DP문제에서 N이 작은 이유이다.

## DP의 전제조건
- 큰 문제를 작은 문제로 나눌 수 있다.
- 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다. 즉, 같은 문제라면 **한 번씩만** 푼다.

## DP 구현 방법
1. 탑다운 - 메모이제이션
    - 재귀 함수
2. 보텀업
    - 반복문
    - DP 테이블

## DP 해결 Tip!
1. DP유형임을 파악하자
    - 완전 탐색으로 접근했을 때 **부분 문제들의 중복 여부로 인해** 시간이 매우 오래 걸리면 DP를 의심해보자
    - N이 생각보다 작다.
    - "결과값에 특정 정수를 나눈 나머지를 출력하라"라는 말이 나오면 DP의심. 완탐으로는 시간초과가 나기 때문이다.
2. 풀이 방법
    1. 재귀 함수를 통한 비효율적 코드 작성
    2. 탑다운(메모이제이션)으로 업그레이드
        - 하지만 재귀 함수의 스택이 한정되어 있을 수 있다.
        - sys라이브러리 - setrecursionlimit()함수 호출
    3. 보텀업
        - **권장**
---
## 기출
### 프로그래머스
[정수 삼각형](https://school.programmers.co.kr/learn/courses/30/lessons/43105)
<br>
[등굣길](https://school.programmers.co.kr/learn/courses/30/lessons/42898#)
<br>
[스티커 모으기(2)](https://school.programmers.co.kr/learn/courses/30/lessons/12971)
<br>
[연속 펄스 부분 수열의 합](https://school.programmers.co.kr/learn/courses/30/lessons/161988)
<br>
[가장 긴 팰린드롬](https://school.programmers.co.kr/learn/courses/30/lessons/12904)
<br>
[거스름돈](https://school.programmers.co.kr/learn/courses/30/lessons/12907)
<br>
[보행자 천국](https://school.programmers.co.kr/learn/courses/30/lessons/1832)