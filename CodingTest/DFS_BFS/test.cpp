#include <iostream>
#include <vector>
#include <string.h>
using namespace std;
int n, l, r;
int graph[50][50];
int visit[50][50]={0,};
int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};
bool mv = false;


void dfs(int x, int y, vector<pair<int, int>> &candi, int &cnt, int &sum) {
    visit[x][y]=1;
    candi.push_back({x,y});
    cnt++;
    sum+=graph[x][y];

    for(int i=0; i<4; i++) {
        int nx = x+dx[i], ny = y+dy[i];
        if(nx<0 || nx>=n || ny<0 || ny>=n) continue;
        if(visit[nx][ny]) continue;

        int sub = abs(graph[nx][ny]-graph[x][y]);
        if(l<= sub && sub <=r){
            dfs(nx, ny,candi,cnt,sum);
        }
    }
}
int main(void){
    cin >> n >> l >> r;
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            cin >> graph[i][j];
        }
    }

    int ans = 0;
    int temp[50][50];
    while(true) {
        mv = false;
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                if(!visit[i][j]) {
                    vector<pair<int, int>> candi;
                    int cnt=0, sum=0;
                    dfs(i,j,candi,cnt,sum);
                    if(candi.size()>1) mv = true;
                    for(auto ele : candi) {
                        temp[ele.first][ele.second] = sum/cnt;
                    }
                }
            }
        }

        memset(visit, 0, sizeof(visit));
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) graph[i][j] = temp[i][j];
        }

        // for(int i=0; i<n; i++) {
        //     for(int j=0; j<n; j++){
        //         cout << graph[i][j];
        //     }
        //     cout << "" << endl;
        // }
        if(!mv) break; 
        ans++;
    }

    cout << ans << endl;
}
  
/*
g++ -o test test.cpp
*/
/*
g++ -o testest testest.cpp
*/


