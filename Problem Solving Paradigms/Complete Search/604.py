from sys import stdin

def check(word,letter,vowels):
    ans,omega,w = True,0,0
    if letter in vowels: omega += 1
    while w < len(word):
        if word[w] in vowels: omega += 1
        w += 1 
    if omega > 2 or len(word)+1 > 4: 
        ans = False
    elif omega > 2 and len(word)+1 < 4: 
        ans = False
    elif omega != 2 and len(word)+1 == 4:
        ans = False
    return ans

def boggle(x,y,A,B,word1,word2,move,vowels,setA,setB,bef):
    if len(word1) == 4: setA.add(word1)
    if len(word2) == 4: setB.add(word2)
    else:
        for x1,y1 in move:
            if x+x1 >= 0 and y+y1 >= 0 and x+x1 < 4 and y+y1 < 4 and (x+x1,y+y1) not in bef:
                tmp1, tmp2  = '', ''
                if word1 != '' and check(word1,A[x+x1][y+y1],vowels):       
                    tmp1 = ''.join([word1,A[x+x1][y+y1]])
                if word2 != '' and check(word2,B[x+x1][y+y1],vowels): 
                    tmp2 = ''.join([word2,B[x+x1][y+y1]])
                if tmp1 != '' or tmp2 != '':
                    bef.append((x+x1,y+y1))
                    boggle(x+x1,y+y1,A,B,tmp1,tmp2,move,vowels,setA,setB,bef)
                    bef.remove((x+x1,y+y1))
        
def main():
    move = [(0,1),(0,-1),(-1,0),(1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
    vowels = ('A','E','I','O','U','Y')
    line = stdin.readline().strip()
    alfa = False
    while line != '#':
        line = line.split()
        A, B, setA, setB = [], [], set(), set()
        A.append(line[0:4])
        B.append(line[4:8])
        for _ in range(3):
            line = stdin.readline().split()
            A.append(line[0:4])
            B.append(line[4:8])
        word1,word2 = "",""
        for i in range(4):
            for j in range(4):
                boggle(i,j,A,B,A[i][j],B[i][j],move,vowels,setA,setB,[(i,j)])
        ans = sorted(setA&setB)
        if alfa: print()
        if len(ans) != 0: 
            for w in ans: print(w)
        else:
            print("There are no common words for this pair of boggle boards.")
        stdin.readline()
        line = stdin.readline().strip()
        alfa = True

main()
