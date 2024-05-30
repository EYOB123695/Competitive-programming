# Problem: D - Medina & Merbebt - https://codeforces.com/gym/522079/problem/D

def sol():
    n = int(input())
    arr = list(map(int, input().split()))  
    q = int(input())

    val = [0] * 32
    prefix = [[0] * 32] 

   
    for a in arr:
        new_val = prefix[-1].copy()
        for i in range(32):
            if a & (1 << i) != 0:
                new_val[i] += 1
        prefix.append(new_val)

    def calc(l, r):
        ans = 0
        for i in range(32):
            bit_count = prefix[r][i] - (prefix[l - 1][i] if l > 0 else 0)
            if bit_count == (r - l + 1):
                ans |= (1 << i)
        return ans

    def search(l, k):
        left = l
        right = n
        while left <= right:
            mid = (right + left) // 2
            if calc(l, mid) >= k:
                left = mid + 1
            else:
                right = mid - 1

        if right < l:
            return -1
        return right

    final = []
  
    for _ in range(q):
        l, k = map(int, input().split())
        final.append(search(l, k))

    return final

T = int(input())
for i in range(T):
    v = sol()
    print(*v)