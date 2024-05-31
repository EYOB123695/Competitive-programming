# Problem: A - Large Number - https://codeforces.com/gym/511242/problem/A

def sol():
    n , d = input().split()
    x = int(n)
    
    a = int(d)
    s =input()  
    arr = list(s)
     
    flag = True
    if a ==  0:
        arr.append(0)
        flag = False
    else:
        for i in range(len(s)):  
            if a > int(s[i]) : 
                idx = i
                arr.insert(idx,a) 
                flag = False

                break 
    if flag:
        arr.append(a)  

           
    return arr
                   

           
        
        
        
        
             








    
    
   

T= int(input())
for _ in range(T):
   answer =  sol() 
   for i in range(len(answer)):
        answer[i] = str(answer[i])
    
   x = "".join(answer)
   print(x)  
