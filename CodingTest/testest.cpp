#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
int n, m;
vector<int> arr;
int weight[11]={0,};

int main(void){
    cin >> n >> m;
    for(int i=0; i<n; i++){
        int k;
        cin >> k;
        arr.push_back(k);
    }

    for(int i=0; i<n; i++) weight[arr[i]]++;

    int ans = 0;
    for(int i=1; i<=n; i++){
        n-=weight[i];
        ans += n*weight[i];
    }

    cout << ans << endl;
    return 0;
}

/*
g++ -o testest testest.cpp
*/
/*
g++ -o testest testest.cpp
*/