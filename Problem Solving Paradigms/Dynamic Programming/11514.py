from sys import stdin

nameSuperpower, attackFactor, energyConsumption, defenseFactor, weakness = None, None, None, None, None

def ks_mem(n,m,P,V,mem):
    ans = None
    if (n,m) in mem: ans = mem[(n,m)]
    else:
        if n <= P and m == V:
            ans = 0
        elif n == P and m != V:
            ans = float('inf')
        else:
            if nameSuperpower[n] in weakness[m] and attackFactor[n] >= defenseFactor[m]:
                ans = min(ks_mem(n+1,m,P,V,mem),ks_mem(n+1,m+1,P,V,mem)+energyConsumption[n])
            else:
                ans = ks_mem(n+1,m,P,V,mem)
        mem[(n,m)] = ans 
    return ans
    
def main():
    global nameSuperpower, attackFactor, energyConsumption, defenseFactor, weakness
    P, V, E = list(map(int,stdin.readline().split()))
    while P != 0 and V != 0 and E != 0:
        nameSuperpower, attackFactor, energyConsumption = [],[],[]
        for _ in range(P):
            line = stdin.readline().split()
            nameSuperpower.append(line[0])
            attackFactor.append(int(line[1]))
            energyConsumption.append(int(line[2]))
        defenseFactor, weakness = [], []
        for _ in range(V):
            line = stdin.readline().split()
            defenseFactor.append(int(line[1]))
            weakness.append(set(line[2].split(',')))
        mem = {}
        ans = ks_mem(0,0,P,V,mem)
        if ans <= E: print('Yes')
        else: print('No')
        P, V, E = list(map(int,stdin.readline().split()))

main()

