from sys import stdin

def phiMem(n,t,lengths,memo):
    ans = songs = r1 = s1 = r2 = s2 = 0
    if (n,t) in memo: ans, songs = memo[(n,t)]
    elif n > 0:
        if lengths[n-1] < t:
            r2, s2 = phiMem(n-1,t-lengths[n-1],lengths,memo)
            r2, s2 = r2+lengths[n-1], s2+1    
        r1, s1 = phiMem(n-1,t,lengths,memo)
        if s2 > s1:  ans, songs = r2, s2
        elif s2 == s1 and r2 >= r1: ans, songs = r2, s2 
        else: ans, songs = r1, s1
        memo[(n,t)] = (ans,songs)
    return ans, songs

def main():
    cases = int(stdin.readline())
    k = 1
    while k <= cases:
        n, t = list(map(int,stdin.readline().split()))
        lengths = list(map(int,stdin.readline().split()))
        memo, songs, ans = {}, 0, 0
        ans, songs = phiMem(n,t,lengths,memo)
        print(f"Case {k}: {songs+1} {ans + 678}")
        k += 1

main()

