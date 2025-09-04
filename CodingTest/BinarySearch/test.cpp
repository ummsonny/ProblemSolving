#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int check(vector<int> &arr, int b) {
    int cnt=1;
    int idx=0;
    for(int i=1; i<arr.size(); i++) {
        if(arr[i]-arr[idx] >= b) {
            cnt++;
            idx = i;
        }
    }
    return cnt;

}
int main(void){
    int n, c;
    cin >> n >> c;
    vector<int> arr(n);
    for(int i=0; i<n; i++) cin >> arr[i];

    sort(arr.begin(), arr.end());

    int l = 1, r = arr[n-1]-arr[0];
    int answer;
    while(l<=r) {
        int m = (l+r)/2;
        // cout << l << ", " << r << ", " << m << endl;

        if(check(arr, m)<c) {
            r = m - 1;
        } else {
            answer = m;
            l = m + 1;
        }
    }

    cout << answer << endl;
}
  
/*
g++ -o test test.cpp
*/
/*
g++ -o testest testest.cpp
*/


