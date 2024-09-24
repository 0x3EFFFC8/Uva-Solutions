from sys import stdin

"""
def phi(n, fred, res):
    if n == len(fred)-1: ans = 0
    else:
        if (res == 1 and fred[n] > fred[n+1]) or (res == -1 and fred[n] < fred[n+1]):
            ans = 1 + phi(n + 1, fred, res*-1)
        else: ans = phi(n + 1, fred, res)
    return ans

#ans = phi(1,fred,1) + 1
"""

def phiIter(fred):
    ans = n = res = 1
    while n != len(fred)-1:
        if (res == 1 and fred[n] > fred[n+1]) or (res == -1 and fred[n] < fred[n+1]):
            ans, res = ans + 1, res*-1
        n += 1
    return ans

def main():
    t = int(stdin.readline())
    while t > 0:
        fred = list(map(int,stdin.readline().split()))
        ans = phiIter(fred)
        print(ans)
        t-=1

main()    

