#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int graph[501][501]={0,};
int main(void){

    int t;
    cin >> t;
    for(int i=0; i<t; i++) {
        int n;
        cin >> n;

        vector<int> indegree(n+1, 0);
        for(int i=1; i<=n; i++)
            for(int j=1; j<=n; j++)
                graph[i][j] = 0;


        vector<int> arr(n);
        for(int i=0; i<n; i++) cin >> arr[i];
        for(int i=0; i<n-1; i++) {
            for(int j=i+1; j<n; j++) {
                graph[arr[i]][arr[j]]=1;
                indegree[arr[j]]++;
            }
        }

        int m;
        cin >> m;
        for(int i=0; i<m; i++) {
            int a, b;
            cin >> a >> b;

            if(graph[a][b]){
                graph[a][b]=0;
                indegree[b]--;
                graph[b][a]=1;
                indegree[a]++;
            }else {
                graph[a][b]=1;
                indegree[b]++;
                graph[b][a]=0;
                indegree[a]--;
            }

        }

        queue<int> q;
        for(int i=1; i<=n; i++) {
            if(!indegree[i]) q.push(i);
            // cout << indegree[i] << ",,";
        }
        // cout << "" << endl;

        int cnt = n;
        bool confused = false;
        vector<int> answer;
        while(!q.empty()) {

            if(q.size()>1) confused = true;

            int cur = q.front();
            q.pop();
            answer.push_back(cur);

            cnt--;
            for(int i=1; i<=n; i++) {
                if(graph[cur][i]){
                    indegree[i]--;
                    if(!indegree[i]) q.push(i);
                }
            }
        }

        // cout << cnt << endl;
        if(cnt) cout << "IMPOSSIBLE" << endl;
        else {
            if(confused) cout << "?" << endl;
            else {
                for(int i=0; i<n; i++) cout << answer[i] << " ";
                cout << "" << endl;
            }
        }

    }
    return 0;
}
  
/*
g++ -o test test.cpp
*/
/*
g++ -o testest testest.cpp
*/


