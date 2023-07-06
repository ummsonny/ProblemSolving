# Priority Queue
## 1. 기본 자료형

```c++
#include <iostream>
#include <queue>
#include <functional>

using namespace std;

int main(){
    priority_queue<int> pq; // 디폴트가 오름차순
    //priority_queue<int, vector<int>, greater<int>> pq; // 내림차순 혹은 파이썬처럼 음수로 넣는방법

    pq.push(4);
    pq.push(7);
    pq.push(3);
    pq.push(1);
    pq.push(10);

    cout << "우선순위 큐 사이즈 : " << pq.size() << "\n";
    
    while(!pq.empty()){
        cout << pq.top() << '\n';
        pq.pop();
    }

    return 0;

}
```

## 2. 구조체 및 내부 연산자 오버로딩
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

    //학번 작은게 우선순위 높다.
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

    cout << "우선순위 큐 사이즈 : " << pq.size() << "\n";
    
    while(!pq.empty()){

        Student ts = pq.top();
        pq.pop();
        cout << "(학번, 수학, 영어) : " << ts.id << ' ' << ts.math << ' ' << ts.eng << "\n";
    }

    return 0;

}
```

## 3. cmp 구조체

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
    //학번 큰게 우선순위 높다.
    bool operator()(Student a, Student b){
        return a.id < b.id;
        //return a.id > b.id; 오름차순
    }
};




int main(){
    priority_queue<Student, vector<Student>, cmp> pq;

    pq.push(Student(3,100,50));
    pq.push(Student(1,60,50));
    pq.push(Student(2,80,50));
    pq.push(Student(4,90,50));
    pq.push(Student(5,70,50));

    cout << "우선순위 큐 사이즈 : " << pq.size() << "\n";
    
    while(!pq.empty()){

        Student ts = pq.top();
        pq.pop();
        cout << "(학번, 수학, 영어) : " << ts.id << ' ' << ts.math << ' ' << ts.eng << "\n";
    }

    return 0;

}
```