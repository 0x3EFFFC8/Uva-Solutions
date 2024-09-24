#include<cstdio>
#include<vector>

using namespace std;

int tabulate(int n, int m, vector<int> moves){
  vector<int> tab(n+1, 0);
  tab[1] = 1;
  int ans;
  int i = 2;
  int j;
  while (i <= n){
    ans = 0;
    j = 0;
    while (j < m && ans != 1){
      if ((moves[j] <= i) && (tab[i-moves[j]] != 1))
          ans = 1;
      j++;
    }
    tab[i] = ans;
    i++;
  }
  
  return tab[n];

}

int main() {
  int n, m, v, ans;
  vector<int> moves;

  while(scanf("%d%d", &n, &m) != EOF){
    moves.clear();
    for(int i = 0; i < m; ++i){
      scanf("%d", &v);
      moves.push_back(v);
    }

    ans = tabulate(n, m, moves);

    if (ans)
      printf("Stan wins\n");
    else
      printf("Ollie wins\n");

  }

  return 0;
  
}
