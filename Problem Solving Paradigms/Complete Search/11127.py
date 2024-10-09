from sys import stdin

def check(n,string):
    ans,beta,t = True,(n+1)//3,1
    while t <= beta and t+t+t <= n+1 and ans:         
        i = n
        while i-t-t-t >= -1 and ans: 
            if string[i] == string[i-t] and string[i-t] == string[i-t-t]:
                teta,j = True, 0
                while j < t and teta:
                    if string[i-j] != string[i-t-j] or string[i-t-j] != string[i-t-t-j]:
                         teta = False
                    j += 1
                if teta: ans = False
            i -= 1
        t += 1
    return ans

def triplefree(n,string,ans):
    if n == len(string):
        if check(n-1,string): 
            ans += 1 
    else:
        if string[n] == '*':
            if check(n-1,string):
                string[n] = '0'
                ans = triplefree(n+1,string,ans)
                string[n] = '1'
                ans = triplefree(n+1,string,ans)
                string[n] = '*'
        else:
            ans = triplefree(n+1,string,ans)
    return ans 

def main():
    line = stdin.readline().strip()
    case = 1
    while line != "0":
        x, string = line.split()
        string = list(string)
        ans = triplefree(0,string,0)
        print(f"Case {case}: {ans}") 
        line = stdin.readline().strip()
        case += 1 

main()  
