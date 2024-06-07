# Problem: A - Double it and give it to the next person. - https://codeforces.com/gym/527294/problem/A

T= int(input())
for _ in range(T):
    s = input()
    l = ""
    ans = []
    final = []
    for i in range(len(s)):
        for j in range(2): 
            l += s[i]
    r = 0
    while r < len(l):
        ans.append(str(l[r]))
        r+=2
    ans.append("".join(ans[::-1]))
    
    print("".join(ans))
   





   