# 기타 
# C++
## 문자(열)
### 문자 변환
- 라이브러리
    - toupper(문자형)
        - 소문자를 대문자로 변환
        - 숫자, 공백, 대문자가 들어가면 변함 없음
    - tolower(문자형)
        - 대문자를 소문자로 변환
        - 마찬가지로 숫자, 공백, 대문자가 들어가면 변함 없음

### 문자열과 문자
- 문자열 + 문자는 문자열이다.
    - string + char는 string
    - string a = "hello" + '!'; -> 이 코드가 가능

### substr
```c++
#include <iostream>
#include <string>

using namespace std;

int main()
{
    string str = "ABCDEFG";

    //인수로 아무 것도 전달하지 않으면 원본 문자열 그대로 반환
    //ABCDEFG
    cout << str.substr() << endl; 

    //인수로 시작 인덱스만 전달한다면 해당 인덱스 ~ 문자열 마지막까지 반환
    //BCDEFG
    cout << str.substr(1) << endl;

    //일반적인 동작 방식
    //CDE
    cout << str.substr(2, 3) << endl;

    //지정된 범위가 원본 문자열 길이를 벗어나면 오류 없이 문자열 마지막까지만 반환
    //G
    cout << str.substr(6, 5) << endl;
}
```

---
---
## 내림, 올림, 반올림
### 헤더파일
- cmath
### 내림
- floor()
### 올림
- ceil()

### 반올림
- round()
    - C++11부터 지원
- floor(N+0.5)
### 대상 자료형
- float
- double
- long double
---
---
## 함수
### 매개변수
- Parameter
    - call by value
        - 값을 복사해서 넘겨줌
    - call by reference
        - 값의 주소 즉, 원본 값을 넘겨줌
    - Note
        - CBV 방식은 복사할 메모리를 확보한 후 값을 복사하여 사용하기에 parameter값이 매우 크다면 시간이 오래걸림
            - [프로그래머스 - 쿼드압축 후 개수 세기] 참고!

## 자료구조
### vector
- 초기화
    1. vector<int> answer(원하는크기, -1);
        - 모든 원소를 원하는 크기만큼 -1로 초기화
    2. 다른 자료구조 요소들을 이용해 vector 생성하기
        - ```c++
            unordered_map <string, int> m2;
            vector <pair<string, int>> v(m2.begin(),m2.end()); 
### unordered_map
- 순회
    - ```c++     
        # key값, value값
        for(auto k : cartime){
            cout << k.first << ", " << k.second << endl;
        }
    - 




