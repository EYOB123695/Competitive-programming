# Problem: C - Ras Alula and The Decrypted Messages - https://codeforces.com/gym/513152/problem/C

def sol():
    n, m = map(int,input().split())
    s = [ord(x) for x in list(input())]
   
    w = [ord(x) for x in list(input())]
 
    l = 0
    
    
    counttwo = sum(w)  
    
    arr = s[:m] 
    countone = sum(arr)  
    if countone == counttwo:
        return "YES"
   
    for r in range(m,n):
       
        
        countone+=s[r] 
        countone-=s[l]  
        l+=1  
        if counttwo == countone:
            return "YES"
            
    return "NO" 
        








T = int(input())
for _ in range(T):
    x=sol()
    print(x) 