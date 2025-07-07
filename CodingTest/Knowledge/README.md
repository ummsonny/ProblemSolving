# 기타 지식

## 설명
- 알고리즘이 아닌 내용을 다루는 곳으로, 변수 메모리 할당 등 PS진행시 풀이자로서 신경써야 할 부분을 다뤘다.
---

### 메모리 할당
- 지역변수
    - 함수, 반복문 등에서 선언되는 변수
    - 이때, 같은 메모리에 반복적으로 변수가 할당된다.
        - ```c++
            // 연결리스트에서 특정 2개 노드 사이에 새로운 노드를 추가하는 코드.
            for(int i=1; i<=n; i++){
                Node newNode = {cur, cur->next, i};
                cur->next->prev = &newNode;
                cur->next = &newNode;

                cout << cur.next->num << endl;

                cur = &newNode;
            }
            ```
        - newNode가 할당되는 메모리는 항상 같은 공간. 따라서 cur은 항상 같은 공간을 가리킨다. 그래서 위 코드는 2개 노드사이에 여러개의 노드를 생성하는 것이 아닌
        1개 노드만 생성되고 노드의 3번째 값(i)만 반복문을 돌며 바뀌고 반복문이 끝나고 나면 cur이 가리키는 노드의 3번째 값은 n이 된다. 결국 3개의 노드만 존재하게됨.
        - ```c++
            //수정된 코드
                for(int i=1; i<=n; i++){
                    Node* newNode = new Node{cur, cur->next, i};
                    cur->next->prev = newNode;
                    cur->next = newNode;

                    cur = newNode;
                }
            ```
        - new를 통해 동적할당을 해주게되면, 매번 새로운 메모리 공간에 할당되어 본래 목적에 맞게 2개노드사이에 n개의 노드를 추가할 수 있다.
---
### call by value & call by reference
- call by value
    - 값을 복사해서 함수에 넘겨주는 과정
    - 그렇다면 아래의 경우는?
        - ```c++
                //프로그래머스 표편집 참고
                void moveUp(Node* kcur, int n){
                    for(int i=0; i<n; i++){
                        kcur = kcur->prev;
                    }
                }
            ```
        - 포인터를 인자로 넘겨준다. 그래서 함수가 종료되면 kcur이 변화한다고 오해하기 쉽다. 하지만 포인터도 주소를 담은 하나의 변수! 인자로 넘겨준 kcur은 call by value에 의해 값이 복사되어 넘어간다. 따라서 함수가 종료되어도 kcur은 변화하지 않는다. 
        - 위와 같이 포인터를 인자로 넘겨주는 경우는 포인터가 가리키는 변수의 값을 변경하기위에 사용하는 것이지 포인터 자체를 변경하지 않는다. 
            - ```c++
                void moveUp(Node* kcur, int n){
                    for(int i=0; i<n; i++){
                        kcur->num += i;
                    }
                }                
                ```
            - 포인터가 가리키는 num에 1~n까지 더해주는 코드. 포인터가 가리키는 변수는 변경된다.
