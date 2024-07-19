# Problem: B - Tzuyu and Sana - https://codeforces.com/gym/532814/problem/B

T= int(input())
for _ in range(T):
    x,y = map(int,input().split())
    print(x^y)