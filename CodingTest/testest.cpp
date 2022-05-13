#include <iostream>
#include <queue>

#define MAX_N 20
#define MAX_M 20
#define BA 0
#define UP 1
#define FR 2
#define BO 3
#define RI 4
#define LE 5

using namespace std;

int G[MAX_N+1][MAX_M+1];
int N, M, K;
int dice[6] = {2, 1, 5, 6, 3, 4}; // BA, UP, FR, BO, RI, LE
int dir[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
int direction = 0;
struct pos{
    int r, c;
};
pos dicePos = {1, 1};
int score;

void getInputs(){
    cin >> N >> M >> K;
    for(int r=1; r<=N; ++r){
        for(int c=1; c<=M; ++c){
            cin >> G[r][c];
        }
    }
}

void moveEast(){
    int temp[6];
    for(int i=0; i<6; ++i){
        temp[i] = dice[i];
    }
    dice[RI] = temp[UP]; dice[UP] = temp[LE]; dice[LE] = temp[BO];
    dice[BO] = temp[RI]; dice[FR] = temp[FR]; dice[BA] = temp[BA];
}

void moveWest(){
    int temp[6];
    for(int i=0; i<6; ++i){
        temp[i] = dice[i];
    }
    dice[RI] = temp[BO]; dice[UP] = temp[RI]; dice[LE] = temp[UP];
    dice[BO] = temp[LE]; dice[FR] = temp[FR]; dice[BA] = temp[BA];
}

void moveNorth(){
    int temp[6];
    for(int i=0; i<6; ++i){
        temp[i] = dice[i];
    }
    dice[RI] = temp[RI]; dice[UP] = temp[FR]; dice[LE] = temp[LE];
    dice[BO] = temp[BA]; dice[FR] = temp[BO]; dice[BA] = temp[UP];
}

void moveSouth(){
    int temp[6];
    for(int i=0; i<6; ++i){
        temp[i] = dice[i];
    }
    dice[RI] = temp[RI]; dice[UP] = temp[BA]; dice[LE] = temp[LE];
    dice[BO] = temp[FR]; dice[FR] = temp[UP]; dice[BA] = temp[BO];
}

bool outOfBound(int r, int c){
    return r < 1 || c < 1 || r > N || c > M;
}

void moveDice(){
    pos next = {dicePos.r + dir[direction][0], dicePos.c + dir[direction][1]};
    if(outOfBound(next.r, next.c)){
        direction += 2;
        direction %= 4;
    }
    // cout << "next r, c " << next.r << ", " << next.c << "\n";
    next = {dicePos.r + dir[direction][0], dicePos.c + dir[direction][1]};
    // cout << "next r, c 2 " << next.r << ", " << next.c << "\n";
    if(direction == 0){
        moveEast();
    }
    if(direction == 1){
        moveSouth();
    }
    if(direction == 2){
        moveWest();
    }
    if(direction == 3){
        moveNorth();
    }

    dicePos = next;
    // cout << "dice pos " << dicePos.r << ", " << dicePos.c << "\n";
    if(dice[BO] > G[dicePos.r][dicePos.c]){
        direction += 1;
        direction %= 4;
        return;
    }
    if(dice[BO] < G[dicePos.r][dicePos.c]){
        direction += 3;
        direction %= 4;
        return;
    }
}

void countScore(){
    queue<pos> q;
    int visited[N+1][M+1];
    for(int r=1; r<=N; ++r){
        for(int c=1; c<=M; ++c){
            visited[r][c] = false;
        }
    }
    q.push(dicePos);
    int B = G[dicePos.r][dicePos.c];
    // cout << "B " << B << "\n";
    int C = 0;

    while(!q.empty()){
        pos curr = q.front(); q.pop();
        if(outOfBound(curr.r, curr.c)) continue;
        if(visited[curr.r][curr.c]) continue;
        visited[curr.r][curr.c] = true;
        ++C;
        // cout << "C " << C << "\n";

        for(int i=0; i<4; ++i){
            pos next = {curr.r + dir[i][0], curr.c + dir[i][1]};
            if(outOfBound(next.r, next.c)) continue;
            if(G[next.r][next.c] != B) continue;
            if(visited[next.r][next.c]) continue;
            q.push(next);
        }
    }

    score += B*C;
}

void printG(){
    cout << "\n======\n";
    for(int r=1; r<=N; ++r){
        for(int c=1; c<=M; ++c){
            cout << G[r][c] << ' ';
        }cout << "\n";
    }
}

void solve(){
    getInputs();
    while(K--){
        moveDice();
        countScore();
    }
    cout << score;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    solve();

    return 0;
}