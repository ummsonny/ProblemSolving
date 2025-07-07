#include <algorithm>
#include <iostream>
#include <vector>
#include <string>

using namespace std;
string str;
vector<int> arr;

int main(void){
    cin >> str;

    int sum=0;
    string temp="";
    int mul = 1;
    for(int i=0; i<str.size(); i++){
        if('0'<=str[i] && str[i]<='9') {
            temp+=str[i];
        } else {
            // cout << temp << "--" << endl;
            sum += mul * stoi(temp);
            if (str[i]=='-') {
                mul = -1;
            }
            temp = "";
        }
    }
    sum += mul * stoi(temp);
    cout << sum << endl;
}

/*
g++ -o testest testest.cpp
*/
/*
g++ -o testest testest.cpp
*/