# Priority Queue
## 1. 디폴트

```c++
#include <iostream>
#include <queue>
#include <functional>

using namespace std;

int main(){
    priority_queue<int> pq; // 기본이 최대힙
    //priority_queue<int, vector<int>, greater<int>> pq; // 최소힙

    pq.push(4);
    pq.push(7);
    pq.push(3);
    pq.push(1);
    pq.push(10);

    cout << "?��???? ? ?????? : " << pq.size() << "\n";
    
    while(!pq.empty()){
        cout << pq.top() << '\n';
        pq.pop();
    }

    return 0;

}
```

## 2. 구조체 및 정렬 메서드 선언
```c++
#include <iostream>
#include <queue>
#include <functional>

using namespace std;

struct Student
{

    int id;
    int math, eng;

    Student(int num, int m, int e) : id(num), math(m), eng(e) {}

    bool operator<(const Student s) const {
        return this->id > s.id;
    }

};


int main(){
    priority_queue<Student> pq;

    pq.push(Student(3,100,50));
    pq.push(Student(1,60,50));
    pq.push(Student(2,80,50));
    pq.push(Student(4,90,50));
    pq.push(Student(5,70,50));

    cout << "?��???? ? ?????? : " << pq.size() << "\n";
    
    while(!pq.empty()){

        Student ts = pq.top();
        pq.pop();
        cout << "(?��?, ????, ????) : " << ts.id << ' ' << ts.math << ' ' << ts.eng << "\n";
    }

    return 0;

}
```

## 3. cmp 구조체 사용

```c++
#include <iostream>
#include <queue>
#include <functional>

using namespace std;

struct Student
{

    int id;
    int math, eng;

    Student(int num, int m, int e) : id(num), math(m), eng(e) {}

};

struct cmp
{
    bool operator()(Student a, Student b){
        return a.id < b.id;
        //return a.id > b.id; 
    }
};




int main(){
    priority_queue<Student, vector<Student>, cmp> pq;

    pq.push(Student(3,100,50));
    pq.push(Student(1,60,50));
    pq.push(Student(2,80,50));
    pq.push(Student(4,90,50));
    pq.push(Student(5,70,50));

    cout << "?��???? ? ?????? : " << pq.size() << "\n";
    
    while(!pq.empty()){

        Student ts = pq.top();
        pq.pop();
        cout << "(?��?, ????, ????) : " << ts.id << ' ' << ts.math << ' ' << ts.eng << "\n";
    }

    return 0;

}
```

## 기출
### 프로그래머스
[이중우선순위큐](https://school.programmers.co.kr/learn/courses/30/lessons/42628)
<br>
[야근 지수](https://school.programmers.co.kr/learn/courses/30/lessons/12927)
<br>
[숫자 게임](https://school.programmers.co.kr/learn/courses/30/lessons/12987)
<br>
[디스크 컨트롤러](https://school.programmers.co.kr/learn/courses/30/lessons/42627)