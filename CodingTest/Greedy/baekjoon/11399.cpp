#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
int n, t;
vector<int> arr;

int main(void){
    int answer = 0;

    cin >> n;
    for(int i=0; i<n; i++) {
        cin >> t;
        arr.push_back(t);
    }

    sort(arr.begin(), arr.end());

    int preSum=0;
    for(int i=0; i<n; i++){
        preSum+=arr[i];
        answer += preSum;
    }

    cout << answer << endl;
    return 0;
}

/*
g++ -o testest testest.cpp
*/
/*
g++ -o testest testest.cpp
*/