from sys import stdin

"""
def phi(n, l, L, gas):
    if l >= L: ans = 0
    else:
        k, best = n + 1, n
        while k < len(gas) and gas[k][0]-gas[k][1] <= l:
            if gas[k][0]+gas[k][1] > gas[best][0]+gas[best][1]:
                best = k
            k += 1
        ans = 1 + phi(k, gas[best][0]+gas[best][1], L, gas)
    return ans 

#ans = G-phi(0, 0, L, gas)
"""

def minGasStations(L, G, gas):
    gas.sort(key=lambda x: x[0] - x[1])
    k, l, ans, ok = 0, 0, 0, True
    while k < G and l < L and ok:
        if gas[k][0]-gas[k][1] > l: ok = False
        best, k = k, k + 1
        while ok and k < G and gas[k][0]-gas[k][1] <= l:
            if gas[k][0]+gas[k][1] > gas[best][0]+gas[best][1]:
                best = k
            k += 1
        l = gas[best][0]+gas[best][1]
        ans += 1
    if not ok or l < L: ans = -1
    return ans

def main():
    L, G = list(map(int,stdin.readline().split()))
    while L != 0 and G != 0:
        gas = []
        for _ in range(G):
            x, r = list(map(int,stdin.readline().split()))
            gas.append((x, r))
        ans = minGasStations(L, G, gas)
        if ans != -1: print(G-ans)
        else: print(ans)
        L, G = list(map(int,stdin.readline().split()))

main()

