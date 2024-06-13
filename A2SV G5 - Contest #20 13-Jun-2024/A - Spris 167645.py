# Problem: A - Spris - https://codeforces.com/gym/528792/problem/A

a = int(input())
b = int(input())
c = int(input())
arr = [a,b,c]
flag = True
while a > 0:
    count = 0
    if a * 2 <= b and a * 4 <= c:
        count = a+a*2+a*4 
        flag = False
        print(count)
        break
    else:
        a-=1
if flag:
    print(0)
