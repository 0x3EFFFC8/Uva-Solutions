#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int phi(int n, int m, int N, int M, vector<int>& P, vector<int>& W, vector<vector<int>>& memo){
  int ans;
  if (memo[n][m] != -1) ans = memo[n][m];
  else {
    if ((n == N) || (m == M)) ans = 0;
    else {
      ans = phi(n+1,m,N,M,P,W,memo);
      if (M-m >= W[n]) ans = max(ans,phi(n+1,m+W[n],N,M,P,W,memo)+P[n]);
    }
    memo[n][m] = ans;
  }
  return ans;
}

int main(){
  int cases, N, M, p, w, G, ans;
  vector<int> P, W;
  scanf("%d", &cases);
  while (cases--){
    P.clear();
    W.clear();
    scanf("%d", &N);
    for (int i = 0; i < N; ++i){
      scanf("%d%d", &p, &w);
      P.push_back(p);
      W.push_back(w);
    }
    scanf("%d", &G);
    ans = 0;
    for (int i = 0; i < G; ++i){
      scanf("%d", &M);
      vector<vector<int>> memo(N+1, vector<int>(M+1, -1));
      ans += phi(0,0,N,M,P,W,memo);
    }
    printf("%d\n",ans);
  }
  return 0;
}
