#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
 
using namespace std;
 
int n, m, k, sqrtN;
long long arr[1000001];
long long bucket[4000001];
 
void init()
{
    sqrtN=sqrt(n);
    for(int i=1; i<=n; i++){
        bucket[i/sqrtN]+=arr[i];
    }
}
 
void update(int x, long long val)
{
    arr[x]=val;
    int idx=x/sqrtN;
    int s=idx*sqrtN, e=s+sqrtN;
    bucket[idx]=0;
    for(int i=s; i<e; i++){ bucket[idx]+=arr[i]; }
}
 
long long sum(int l, int r)
{
    long long ret=0;
    while(l%sqrtN!=0 && l<=r){ ret+=arr[l]; l++; }
    while((r+1)%sqrtN!=0 && l<=r){ ret+=arr[r]; r--; }
    while(l<=r){
        ret+=bucket[l/sqrtN];
        l+=sqrtN;
    }
    return ret;
}
 
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    cin >> n >> m >> k;
    for(int i=1; i<=n; i++){ cin >> arr[i]; }
    init();
    for(int i=1; i<=m+k; i++){
        int qry; cin >> qry;
        if(qry==1){
            int idx; long long val;
            cin >> idx >> val;
            update(idx, val);
        }
        else{
            int l, r;
            cin >> l >> r;
            cout << sum(l, r) << "\n";
        }
    }
    return 0;
}