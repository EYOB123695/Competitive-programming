# Problem: E - Word Transformation - https://codeforces.com/gym/543431/problem/E

from collections import *
n = int(input())
dictionary = defaultdict(list)
for _ in range(n):
    flag  = True
    s,t  = input().split()
    dictionary = Counter(s)
    dictionarytwo = Counter(t)
    removecount = {}
    ans = []
    for i in s:
        removecount[i] = dictionary[i] -  dictionarytwo[i]
        if removecount[i] < 0:
            flag =False 
    if not flag:
        print("NO")
        continue 
    for i in s:
        if removecount[i] > 0 :
            removecount[i] -= 1
        else:
            ans.append(i)
    if "".join(ans) != t:
        print("NO")
    else:
        print("YES") 
    
     

    

     
    

    





      



