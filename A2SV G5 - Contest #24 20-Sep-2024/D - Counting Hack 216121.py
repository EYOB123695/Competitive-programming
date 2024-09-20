# Problem: D - Counting Hack - https://codeforces.com/gym/534160/problem/D

for _ in range(int(input())):
    length = int(input())
    numbers = list(map(int, input().split()))

    seen = set()
    suffix_count = [0] * (length + 1)
    for idx in range(length - 1, -1, -1):
        if numbers[idx] not in seen:
            seen.add(numbers[idx])
            suffix_count[idx + 1] = 1
            seen.add(numbers[idx])
    
    for idx in range(1, len(suffix_count)):
        suffix_count[idx] += suffix_count[idx - 1]

    seen.clear()
    result = 0
    for idx in range(length):
        if numbers[idx] not in seen:
            result += suffix_count[-1] - suffix_count[idx]
            seen.add(numbers[idx])

    print(result)
