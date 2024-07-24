# Problem: A - Se7en - https://codeforces.com/gym/537362/problem/A

import math
T = int(input())
for _ in range(T):
    x = int(input())
    if x % 7 == 0:
        print(x)
    else:
        x-= x %10
        while x %7:
            x += 1 
        print(x)        
            
            
      