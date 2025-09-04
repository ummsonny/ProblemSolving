# 📘 누적합(Prefix Sum) 개념 정리

## 🧠 누적합이란?

**누적합(Prefix Sum)**은 배열의 인덱스 0부터 특정 인덱스까지의 합을 미리 계산해 놓는 방식입니다. 이를 통해 배열의 특정 구간 `[i, j]`의 합을 빠르게 구할 수 있습니다.



```cpp
//예를 들어 배열이 다음과 같다고 가정해 봅시다:
// 원본 배열
arr = [3, 2, 4, 1, 7]

//각 인덱스까지의 누적합은 다음과 같이 계산됩니다:
// 누적합 배열
prefix_sum = [3, 5, 9, 10, 17]

//이제 구간 [i, j]의 합은 다음과 같이 구할 수 있습니다:
// 구간 합 계산 공식
sum(i, j) = prefix_sum[j] - prefix_sum[i - 1]

//단, i == 0일 경우는 다음과 같이 처리합니다:
sum(0, j) = prefix_sum[j]
```
```cpp
#include <iostream>
#include <vector>

using namespace std;

// 누적합 벡터 생성 함수
vector<int> computePrefixSum(const vector<int>& arr) {
    vector<int> prefixSum(arr.size());
    prefixSum[0] = arr[0];

    for (size_t i = 1; i < arr.size(); ++i) {
        prefixSum[i] = prefixSum[i - 1] + arr[i];
    }

    return prefixSum;
}

// 구간 합 계산 함수: sum from arr[l] to arr[r]
int rangeSum(const vector<int>& prefixSum, int l, int r) {
    if (l == 0) return prefixSum[r];
    return prefixSum[r] - prefixSum[l - 1];
}

int main() {
    vector<int> arr = {3, 2, 4, 1, 7};

    vector<int> prefixSum = computePrefixSum(arr);

    // 구간 [1, 3]의 합: 2 + 4 + 1 = 7
    int l = 1, r = 3;
    cout << "Sum of arr[" << l << "] to arr[" << r << "] = " << rangeSum(prefixSum, l, r) << endl;

    return 0;
}
```

## ✅ 장점

- 반복적인 구간 합 계산 시 시간 복잡도를 **O(1)**로 줄일 수 있습니다.
- 초기 누적합 계산은 **O(n)**의 시간 복잡도로 수행됩니다.

---

## ⚠️ 주의할 점

- 배열이 큰 경우 **메모리**를 추가로 사용합니다.
- 인덱스가 **0부터 시작하는지**, **1부터 시작하는지**에 따라 코드 구현이 달라질 수 있습니다.
- 누적합 배열은 종종 원본보다 **한 칸 더 크게 선언**하여 `prefix[0] = 0`으로 시작하기도 합니다.

---

## 📚 관련 문제

- [백준 11659번: 구간 합 구하기 4](https://www.acmicpc.net/problem/11659)
- [LeetCode 303: Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)
- [Programmers: 누적합 기법을 활용한 문제들](https://school.programmers.co.kr/)
    - [파괴되지 않은 건물](https://school.programmers.co.kr/learn/courses/30/lessons/92344)
    - [광고 삽입](https://school.programmers.co.kr/learn/courses/30/lessons/72414)

---

## 💡 확장 개념

누적합은 다음과 같은 확장 버전으로도 활용됩니다:

### 🔹 2차원 누적합 (Prefix Sum in 2D)
- 예: 이미지 누적 영역 계산, 사각형 영역 합 등

### 🔹 구간 갱신이 필요한 경우
- **세그먼트 트리 (Segment Tree)**
- **펜윅 트리 (Fenwick Tree / Binary Indexed Tree)**

---
