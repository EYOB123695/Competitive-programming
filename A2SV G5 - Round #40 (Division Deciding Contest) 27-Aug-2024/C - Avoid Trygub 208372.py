# Problem: C - Avoid Trygub - https://codeforces.com/gym/543431/problem/C

from collections import *
T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    x = list(s)
   
   
    stack = ["b","u","g","y","r","t"] 
   
    for idx,i in enumerate(x):
        
        if stack and i == stack[-1]:
           
           
            val = stack.pop()
          
      
 
    
   
    if len(stack) != 0:
        print(s)
        
    else:
        for i in range(len(x)):
            for j in range(i,len(x)):
                if x[i] == "t" and x[j] == "b":
                    x[i] , x[j] = x[j] , x[i] 
                
     
        print("".join(x)) 