#include <algorithm>
#include <iostream>
#include <vector>
#include <queue>
#include <deque>
using namespace std;

int graph[50][50];
vector<pair<int, int>> chicken;
vector<pair<int, int>> home;
int answer=100000;
int n,m;
int chickDist(vector<pair<int, int>> &temp) {
    int ret=0;
    for(int i=0; i<home.size(); i++) {
        int loclRet=100;
        for(int j=0; j<temp.size(); j++) {
            int c = (abs(home[i].first-temp[j].first)+abs(home[i].second-temp[j].second));
            loclRet = min(loclRet, c);
        }
        ret+=loclRet;
    }
    // cout << ret << endl;
    return ret;
}

void combination(int cnt, int start, vector<pair<int, int>> &temp) {
    if(cnt==m) {    
        answer = min(answer,chickDist(temp));
        for(auto ele : temp) {
            // cout << ele.first << "," << ele.second << " ";
        }
        // cout << "" << endl;
        return;
    }

    for(int i=start; i<chicken.size(); i++) {
        temp.push_back(chicken[i]);
        combination(cnt+1, i+1, temp);
        temp.pop_back();
    }
}
int main(void){

    cin >> n >> m;


    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            cin >> graph[i][j];
            if(graph[i][j]==2) chicken.push_back({i,j});
            else if(graph[i][j]==1) home.push_back({i,j});
        }
    }

    vector<pair<int, int>> temp;
    combination(0,0,temp);

    cout << answer << endl;

    return 0;

}
  
/*
g++ -o test test.cpp
*/
/*
g++ -o testest testest.cpp
*/


