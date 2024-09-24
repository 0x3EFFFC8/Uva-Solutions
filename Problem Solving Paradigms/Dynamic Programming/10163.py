from sys import stdin

PINF = float('inf')

def phiMem(m,n,P,memo):
    ans, h = None, (m,n)
    if h in memo: ans = memo[h]
    else:
        if m == 0: ans = PINF if n==0 else 0
        else:
            ans = phiMem(m-1,n,P,memo)
            for k in range(1,min(n,P[m-1])+1):
                ans = max(ans,min(phiMem(m-1,n-k,P,memo),P[m-1]//k))        
        memo[h] = ans
    return ans

"""
def roMem(m,n,P,L,memo,memoR):
    ans, h = PINF, (m,n)
    if h in memoR: ans = memoR[h]
    else:
        if m == 0: ans = PINF if n!=0 else 0
        else:
            if memo[(m-1,n)] >= L:
                ans = roMem(m-1,n,P,L,memo,memoR)
            for k in range(1,min(n,P[m-1])+1):
                if P[m-1]//k >= L and memo[(m-1,n-k)] >= L:
                    ans = min(ans,roMem(m-1,n-k,P,L,memo,memoR)+P[m-1])
        memoR[h] = ans
    return ans
"""

def optTabulateRo(M,N,L,P,memo):
    prev, curr = 0, 1 
    tab = [[0 for _ in range(N + 1)] for _ in range(2)]
    for m in range(1, M + 1):
        for n in range(1, N + 1):
            if (m-1,n) in memo and memo[(m-1,n)] >= L:
                tab[curr][n] = tab[prev][n]
            else: tab[curr][n] = PINF
            for k in range(1, min(n, P[m-1]) + 1):
                if P[m-1]//k >= L and (m-1,n-k) in memo and memo[(m-1,n-k)] >= L:
                    tab[curr][n] = min(tab[curr][n],tab[prev][n-k]+P[m-1])
        prev, curr = curr, prev
    return tab[prev][N]

def main():
    n, m = list(map(int,stdin.readline().split()))
    while n != 0 and m != 0:
        P = list(map(int,stdin.readline().split()))
        memo = {}
        #memoR = {}
        L = phiMem(m,n,P,memo)
        if L != 0: Y = optTabulateRo(m,n,L,P,memo) #roMem(m,n,P,L,memo,memoR)  
        else: Y = 0
        print(L,Y)
        n, m = list(map(int,stdin.readline().split()))
main()

