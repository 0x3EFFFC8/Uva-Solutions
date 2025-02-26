from sys import stdin 

def phiMemo(n,s,l,memo):
    ans, k = 0, (l,s,n)
    if k in memo: ans = memo[k]
    else:
        if l == 0 and s == 0:
            ans = 1
        elif n <= 26 and l > 0 and s > 0 and s <= ((26-n+1) * (n+26))//2:
            ans = phiMemo(n+1,s-n,l-1,memo) + phiMemo(n+1,s,l,memo)
        memo[k] = ans
    return ans

def main():
    memo, i = {}, 1
    l, s = list(map(int,stdin.readline().split()))
    while l != 0 and s != 0:
        ans = phiMemo(1,s,l,memo)
        print(f"Case {i}: {ans}")
        l, s = list(map(int,stdin.readline().split()))
        i += 1

main()
