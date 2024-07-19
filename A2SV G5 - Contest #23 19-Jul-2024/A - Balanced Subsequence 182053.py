# Problem: A - Balanced Subsequence - https://codeforces.com/gym/532814/problem/A

from collections import *
n,k = map(int,input().split())
s =  input()

x = []
flag = True
dic = defaultdict(int)
s = s.lower()
for i in range(len(s)):
     dic[s[i]] += 1




for i in range(n): 
    c =  ord(s[i]) - ord("a")
    if c > k:
         print(0)
         flag = False
    
    x.append(c)


for i in range(k) :
    
    if i not in x:
        flag = False 
        print(0)
        break

if flag:
    e = float("inf")
    for key , val in dic.items():
        
           b = ord(key)   - ord("a")
         
           if b in x:
                e = min(e,val)
  
    ans = 0
    for key, val in dic.items(): 
        b = ord(key)   - ord("a")
        if  b in x:  
             ans += e 
    
  
    print(ans) 
       



