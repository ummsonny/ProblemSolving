#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int dp[10001]={0,};
vector<int> arr;
int main(void){
    int answer = 0;
    int n, m;
    cin >> n >> m;

    for(int i=0; i<n; i++) {
        int t;
        cin >> t;
        arr.push_back(t);
    }

    fill_n(dp, m+1, 20000);
    dp[0]=0;
    sort(arr.begin(), arr.end());

    for(int i=0; i<arr.size(); i++) {
        for(int j=arr[i]; j<=m; j++) {
            dp[j] = min(dp[j], dp[j-arr[i]]+1);
        }
    }

    if(dp[m]>10000) cout << -1 << endl;
    else cout << dp[m] << endl;
    return 0;
}

/*
g++ -o testest testest.cpp
*/
/*
g++ -o testest testest.cpp
*/

