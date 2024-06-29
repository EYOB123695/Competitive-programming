# Problem: D - Binyam and Kalkidan - https://codeforces.com/gym/531455/problem/D

n=  int(input())
arr= input()
check = "2357"
ans = []
for i in arr:
    if i == "4":
        ans.extend(['3','2','2'])
    elif i =='6':
        ans.extend(['5','3'])
    elif i =='8':
        ans.extend(['7','2','2','2'])
    elif i =='9':
        ans.extend(['7','3','3','2'])
    elif i in check:
        ans.append(i)

ans.sort()
ans = ans[::-1]


print("".join(ans)) 