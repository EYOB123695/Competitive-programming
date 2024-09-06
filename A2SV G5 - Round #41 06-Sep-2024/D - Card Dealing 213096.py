# Problem: D - Card Dealing - https://codeforces.com/gym/545013/problem/D

from collections import *
T = int(input())
for _ in range(T):
    n = int(input())
    alice = 1
    bob = 0
    flag = False
    countbob = 0
    countalice = 0
    res = []
    ava = n-1
    for i in range(2,n+1):
        if flag :
            if  ava <= i: 
                alice += ava
                break 

            ava-=i
            alice +=  i
            countalice +=1 
            if countalice == 2 :
                flag = False
                countalice = 0
        elif not flag :
            if  ava <= i: 
                bob += ava
                break 
            ava-=i  
            bob += i
            countbob += 1
            if countbob == 2 :
                flag = True
                countbob = 0
           
 
    print(alice , bob , sep = " ")


        
