from sys import stdin,setrecursionlimit
setrecursionlimit(1<<20)

visited = None
band = None
Montesco = None
Capuleto = None
ans = None

def montescoAux(G,u,family):
    global band, Montesco, Capuleto, visited
    visited[u] = family
    if family == 1:
        Montesco += 1
    else: 
        Capuleto += 1
    for v in G[u]:
        if visited[v] == visited[u]:
            band = False
        elif visited[v] == -1:
            montescoAux(G,v,1-family)

def montesco(G):
    global band, Montesco, Capuleto, ans
    Montesco = Capuleto = ans = 0
    for v in range(len(G)):
        if len(G[v]) == 0: 
            ans += 1
        elif visited[v] == -1:
            band = True
            Montesco = Capuleto = 0
            montescoAux(G,v,1)
            if band == True:
                ans += max(Montesco,Capuleto)
     
def main():
    global visited
    n = int(stdin.readline())
    while n > 0:
        stdin.readline().strip()
        m = int(stdin.readline())
        G = [set() for _ in range(m)]
        visited = [ -1 for _ in range(m)]
        for i in range(m):
            line = list(map(int,stdin.readline().split()))
            for j in range(1,len(line)):
                if line[j] <= m:
                    G[i].add(line[j]-1)
                    G[line[j]-1].add(i)
        montesco(G)
        print(ans)
        n -= 1
main()
