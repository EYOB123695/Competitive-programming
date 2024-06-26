# Problem: D - The Equalizer XOR - https://codeforces.com/gym/528792/problem/D

T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int,input().split()))
    xor = [0] * n
    Flag = True
    xor[0] = arr[0]
    for i  in range(1,len(arr)):
        xor[i] = xor[i-1] ^ arr[i]
    if xor[n-1] == 0:
        print("YES")
        Flag = False
    else:
        for i in range(n):
            one = xor[i]
            if not Flag:
                break
            for j in range(i+1,n-1):
                two = xor[j] ^ xor[n-1]
                three = xor[i] ^ xor[j] 
                if one == two == three :
                    print("YES")
                    Flag = False 
                    break
    if Flag :

        print("NO") 

    




