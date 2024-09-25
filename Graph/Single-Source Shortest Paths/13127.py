from heapq import heappush,heappop
from sys import stdin

INF = float('inf')

def dijkstra(G, policeStations):
    dist = [ INF ]*len(G)
    for s in policeStations: dist[s] = 0
    pred = [-1] * len(G)
    pqueue = list()
    for s in policeStations: heappush(pqueue, (dist[s], s))
    while len(pqueue)!=0:
        du,u = heappop(pqueue)
        if dist[u] == du:
            for v,duv in G[u]:
                if du+duv<dist[v]:
                    dist[v] = du+duv
                    pred[v] = u
                    heappush(pqueue, (dist[v], v))
    return dist

def solve(G, banks, policeStations):
    dist = dijkstra(G, policeStations)
    q = []
    for s in banks: q.append((dist[s],s))
    q.sort(key=lambda x: x[0])
    min = len(q)-2
    while min >= 0 and q[min][0] == q[-1][0]: min -= 1
    s, e = len(banks)-(min+1), q[-1][0]
    if q[min+1][0] == INF: e = '*'
    return s, e, q, min+1

def main():
    line = stdin.readline()
    while line != "":
        n, m, b, p = list(map(int,line.split()))
        G = [[] for _ in range(n)]
        for _ in range(m):
            u, v, t = list(map(int,stdin.readline().split()))
            G[u].append((v,t))
            G[v].append((u,t))
        banks = list(map(int,stdin.readline().split()))
        if p > 0:
            policeStations = list(map(int,stdin.readline().split()))
            s, e, q, min = solve(G, banks, policeStations)
            banksT = sorted(q[min:],key=lambda x: x[1])
            print(s,e)
            print(' '.join(map(str,(b[1] for b in banksT))))
        else:
            banks.sort()
            print(b,'*')
            print(' '.join(map(str,banks)))                        
        line = stdin.readline()
main()

