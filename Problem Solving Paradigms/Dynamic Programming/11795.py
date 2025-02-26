from sys import stdin

INF = float('inf')

def universe(N): return (1<<N)-1

def is_elt(n,X): return (X|(1<<n))==X

def remove_elt(n,X): return X-(1<<n) if is_elt(n,X) else X

def singlenton(n,X): return X==(1<<n)

def phi_memo(N,w,u,X,weapons,mem):
    ans,key = None,(X,weapons)
    if key in mem: ans = mem[key]
    else:
        if weapons == 0: 
            ans = 0
        elif singlenton(u,X):
            ans = 1
        else:
            ans, Y = 0, remove_elt(u,X)
            for v in range(1,N):
                if is_elt(v,Y) and is_elt(v-1,weapons):
                    Z = weapons | w[v] 
                    ans += phi_memo(N,w,v,Y,Z,mem)
        mem[key] = ans 
    return ans

def tsp(N,w):
    X = universe(N)
    mem = dict()
    ans = phi_memo(N,w,0,X,w[0],mem)
    return ans

def main():
    T = int(stdin.readline().strip())
    for t in range(1,T+1):
        N = int(stdin.readline().strip())+1
        w = []
        for _ in range(N):
            string = stdin.readline().strip()
            w.append(int(string[::-1],2))
        ans = tsp(N,w)
        print(f"Case {t}: {ans}")

main()
