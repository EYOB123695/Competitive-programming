# Problem: A - The Coordinate Challenge - https://codeforces.com/gym/531455/problem/A

from collections import *
import math 
t = int(input())
for _ in range(t):
    n = int(input())
    flag =True
    if n == 1 :
        print(2)
        flag =False
    elif n == 2 or n == 3:
        print(1)
        flag  = False 
    if flag:
        x = n / 2
        y = n/ 3
       
        x= math.ceil(x)
        y = math.ceil(y)
        if x < y :
            print(x)
        else:
            print(y) 