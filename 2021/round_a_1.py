t = int(input())

for i in range(t):
    N, K = [int(k) for k in input().split()]
    s = input()
    score = 0

    for k in range(N//2):
        if s[k] != s[N-k-1]:
            score += 1
    ans = abs(score - K)
    
    print("Case #{}: {}".format(i+1, ans))