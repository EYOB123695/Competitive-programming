# Problem: E - Min Divisible Outside Segment - https://codeforces.com/gym/545013/problem/E

q=  int(input())
for i in range(q):
    l,r,d = map(int,input().split())
    if d < l :
        print(d)
    else:
        if r % d == 0:
            print(r + d)
        else :
           print( r + (d - r%d))
    

