#include <iostream>
#include <vector>
#include <string.h>
#include <algorithm>
#include <queue>
using namespace std;

priority_queue<int> pq;

int main(void){
    int n;
    cin >> n;

    for(int i=0; i<n; i++) {
        int t;
        cin >> t;
        pq.push(-t);
    }

    int answer = 0;
    while(pq.size()!=1) {
        int a = -pq.top();
        pq.pop();
        int b = -pq.top();
        pq.pop();
        answer += (a+b);
        pq.push(-(a+b));
    }
    cout << answer << endl;
}
  
/*
g++ -o test test.cpp
*/
/*
g++ -o testest testest.cpp
*/


