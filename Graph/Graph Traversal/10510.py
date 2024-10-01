from collections import deque
from sys import stdin, setrecursionlimit
setrecursionlimit(1<<20)

visited,disc,fin,time,res = None,None,None,None,None
low = []
apNodos = set()
t,n, = int(), int()

def reverse(G):
  ans = [ list() for _ in G ]
  for u in range(len(G)):
    for v in G[u]:
      ans[v].append(u)
  return ans

def dfs(G, order):
  global visited,disc,fin,time
  ans = list()
  visited,disc,fin,time = list(),list(),list(),0
  for _ in G:
    visited.append(0)
    disc.append(None)
    fin.append(None)
  for u in order:
    if visited[u]==0:
      ans.append(list())
      dfs_visit(G, u, ans[-1]) 
  return ans
    
def dfs_visit(G, u, comp):
  global visited,disc,fin,time,res
  visited[u],disc[u],time = 1,time,time+1
  comp.append(u)
  for v in G[u]:
    if visited[v]==0:
      dfs_visit(G, v, comp)
    elif visited[v] == 2:
      res = False
  visited[u],fin[u],time = 2,time,time+1 

def main():
    global res, visited
    cases = int(stdin.readline())
    while cases > 0:
        n = int(stdin.readline())
        m = int(stdin.readline())
        G = deque(deque() for i in range(n))
        res = True
        for i in range(m):
            u, v = map(int,stdin.readline().split())
            G[u].append(v)
        dfs(G, range(len(G)))
        solve = res
        tmp = list(zip( [ u for u in range(len(G)) ], fin))
        tmp.sort(key=lambda x: -x[1])   
        order = [ x[0] for x in tmp ]   
        GT = reverse(G)
        scc = dfs(GT, order)
        if len(scc) == 1 and solve == True:
          print("YES")
        else:
          print("NO")
        cases -= 1
main()
