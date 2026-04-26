import math
N,M,K = map(int,input().split())

def f(k):
    t = math.factorial(N+M) // (math.factorial(N) * math.factorial(M))
    if t < k:
        return -1
    dp = [[1 for _ in range(0, M + 1)] for _ in range(0, N + 1)]
    dp[0][0] = 0

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    answer = ""
    n, m = N, M
    while (n > 0 or m > 0):
        if (n == 0 or m == 0):
            answer += 'a' * n
            answer += 'z' * m
            break
        else:
            if k <= dp[n - 1][m]:
                answer += "a"
                n -= 1
            else:
                k -= dp[n - 1][m]
                answer += "z"
                m -= 1
    return answer

print(f(K))