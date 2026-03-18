def fibonacci(n):
    if n == 0:
        return (0, 1)

    a, b = fibonacci(n // 2)

    c = a * ((2 * b - a)) % 1000000007
    d = (a * a + b * b) % 1000000007

    if n % 2 == 0:
        return (c, d)
    else:
            return (d, (d + c) % 1000000007)
        
n = int(input())
if n % 2 == 0:
    print(fibonacci(n)[0])
else:
    print(fibonacci(n + 1)[0])