# Problem: A - abbccc - https://codeforces.com/gym/530187/problem/A

n = int(input())
s = input()
ans = []
ans.append(s[0])
count = 2
i = 1
while i < n:
    ans.append(s[i])
    i+=count
    count+=1
print("".join(ans))


