#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
int n, k;
vector<int> arr;

int main(void){
    cin >> n >> k;
    for(int i=0; i<n; i++){
        int t;
        cin >> t;
        arr.push_back(t);
    }

    int ans=0;
    for(int i=n-1; i>=0; i--){
        if(k<arr[i]) continue;

        ans += k/arr[i];
        k%=arr[i];

        if(k<=0) break;
    }
    cout << ans << endl;
}