# Problem: F - Messi versus Ronaldo - https://codeforces.com/gym/522079/problem/F

T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    MOD = 1000_000_007
    bit_counts = [0]*60
    for j in arr:
        for i in range(60):
            if j&(1<<i):
                bit_counts[i] += 1
    final = 0
    for j in arr:
        totalone = 0
        totaltwo = 0
        for i in range(60):
            if j&(1<<i):
                totalone += (1<<i)%MOD*n
                totalone %= MOD
                totaltwo += (1<<i)%MOD*bit_counts[i]
                totaltwo %= MOD
            else:
                totalone += (1<<i)%MOD*bit_counts[i]
                totalone %= MOD
        final += totalone*totaltwo
        final %= MOD

    print(final)