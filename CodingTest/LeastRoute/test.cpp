#include<iostream>
#include <queue>
#define INF 1e9
using namespace std;

vector<int> graph[20001];
int dist[20001];
int main(void){
    int n, m;
    cin >> n >> m;

    for(int i=0; i<m; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    for(int i=0; i<=n; i++) dist[i]=INF;

    priority_queue<pair<int, int>> pq;
    pq.push({0,1});

    while(!pq.empty()) {
        auto cur = pq.top();
        pq.pop();

        if(-cur.first > dist[cur.second]) continue;

        for(int nx : graph[cur.second]) {
            if(-cur.first+1 < dist[nx]){
                dist[nx] = -cur.first+1;
                pq.push({-dist[nx], nx});
            }
        }
    }

    int maxV = -1;
    int minNode = 1;
    int cnt = 0;
    for(int i=2; i<=n; i++) {
        if(maxV < dist[i]){
            maxV = dist[i];
            minNode = i;
            cnt = 1;
        } else if(maxV == dist[i]) cnt++;
    }

    cout << minNode << " " << maxV << " " << cnt << endl;


    
}
  
/*
g++ -o test test.cpp
*/
/*
g++ -o testest testest.cpp
*/


