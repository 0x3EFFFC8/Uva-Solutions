from heapq import heappush, heappop
from collections import deque
from sys import stdin
import math

INF = float('inf')

def prim(G):
  visited = [False for i in range(len(G))]
  c = [ INF ]*len(G) ; c[0] = 0
  p = [-1] * len(G)
  pqueue = list()
  heappush(pqueue, (c[0], 0))
  while len(pqueue)!=0:
    du,u = heappop(pqueue)
    visited[u] = True
    if c[u] == du:
        for v,duv in G[u]:
            if not visited[v] and duv < c[v]:
                c[v] = duv
                p[v] = u                     
                heappush(pqueue, (c[v], v))
  return c, p    

def BFS(n,c,p):
    distances = [0 for _ in range(n)]
    q = deque()
    q.append(0)
    while len(q) != 0:
        u = q.popleft()   
        if distances[p[u]] > c[u] and u != 0:
            distances[u] = distances[p[u]]
        else:
            distances[u] = c[u]
        for i in range(len(p)):
            if p[i] == u: 
                q.append(i)   
    return distances

def PIN(distances,M):
    sM, Ti = 0, 0
    for i in range(len(distances)):
        Ti += (distances[i])*M[i]
        sM += M[i]
    ans = Ti/sM
    return ans

def main():
    n = int(stdin.readline())
    Nisland = 0
    while n != 0:
        Nisland += 1
        X = [0 for _ in range(n)]
        Y = [0 for _ in range(n)]
        M = [0 for _ in range(n)]
        edge = [[] for _ in range(n)]
        for i in range(n):
            island = list(map(int,stdin.readline().split()))
            X[i],Y[i],M[i] = island[0],island[1],island[2]
        for i in range(n-1):
            for j in range(i+1,n):
                v = math.hypot(X[i]-X[j],Y[i]-Y[j])
                edge[i].append((j,v))
                edge[j].append((i,v))
        c, p = prim(edge)
        distances = BFS(n,c,p)
        ans = PIN(distances,M)
        print(f"Island Group: {Nisland} Average {ans:.2f}\n")
        n = int(stdin.readline())

main()
