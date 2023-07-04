# Sqrt Decomposition
## Sqrt Decomposition
- what
    - 특정 구간 쿼리를 O(N^(1/2))에 처리하는 알고리즘
    - 구간의 최댓값, 최솟값, 구간합 등을 구할때 사용
    - 밑에는 구간합을 예제로 알고리즘 설명

---
## 초기화 작업
    1. N^(1/2) 구하기
    2. N^(1/2)개의 원소들로 이뤄진 그룹 만들기
```c++
int n,m,k,sqrtN;
long long arr[1000001];
long long bucket[4000001]; //구간합 저장해 놓을 곳

void init(){
    sqrtN = sqrt(n);
    for(int i=1; i<=n; i++){
        bucket[i/sqrtN]+=arr[i];
    }
}
```

---
## 값 업데이트
- 시간복잡도 O(N^(1/2))
```c++
void update(int x, long long val){ //x번째 원소를 val로 바꾼다.
    arr[x]=val;
    int idx = x/sqrtN;
    int s=idx*sqrtN, e=s+sqrtN;
    bucket[idx]=0;
    for(int i=s;i<e;i++){
        bucket[idx]+=arr[i];
    }
}
```
- 시간복잡도 O(1)
- 원소 1개만 수정
```c++
void update(int x, long long val){ //x번째 원소를 val로 바꾼다.
    int idx = x/sqrtN;
    bucket[idx]-=arr[x];
    bucket[idx]+=val;
    arr[x]=val;
}
```
---
## 구간합 구하기
```c++
long long sum(int l, int r)
{
    long long ret=0;
    
    //1. 왼쪽과 오른쪽에 남은 원소들 먼저 더해준다.
    while(l%sqrtN!=0 && l<=r){ ret+=arr[l]; l++; }
    while((r+1)%sqrtN!=0 && l<=r){ ret+=arr[r]; r--; }
    
    //2. 구간 내에 있는 그룹들의 합을 구한다.
    while(l<=r){
        ret+=bucket[l/sqrtN];
        l+=sqrtN;
    }
    return ret;
}
```


