# Problem: B - BANless - https://codeforces.com/gym/528792/problem/B

T= int(input())
for _ in range(T): 
    flag = True
    n = int(input())
   
    ans = []
    i = 1
    j = 3*n
    while j > i:

            ans.append([i,j])
            i+=3
            j-=3
           
    print(len(ans))
    for i,j in ans:
        print(i,j)




    

