# 진법 
## 진법 변환 함수
```c++
//숫자 n, k진법 변환
string jinbub(int n, int k){
    string ret="";
    while(n){
        int m = n%k;
        string t = "";
        t += ('0'+m);
        ret = t+ret;
        
        n /= k;
    }
    return ret;
}
```
## Note!
진법 변환, 특히 숫자가 작은 진법변환을 하면 자릿수가 많아짐
- 자료형 조심. int대신 long으로 받기
- https://school.programmers.co.kr/learn/courses/30/lessons/92335
    




