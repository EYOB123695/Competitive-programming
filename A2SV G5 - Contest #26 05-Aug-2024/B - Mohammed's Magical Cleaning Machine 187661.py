# Problem: B - Mohammed's Magical Cleaning Machine - https://codeforces.com/gym/537362/problem/B

for _ in range(int(input())):
    n = int(input())
    arr= list(map(int, input().split()))

    ans = 0 
    for a in arr[:-1]:
        if a or ans > a:
            ans += a + int(a == 0)

    print(ans)