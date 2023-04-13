def sum1(N):
    # Time Complexity: O(N)
    s = 0
    for i in range(1, N + 1):
        s = s + i
    return s
    # print(s)


def sum2(N):
    # Time Complexity: O(1)
    return N * (N + 1) // 2
    # print(N*(N+1)//2)


t = int(input())
while t:
    n = int(input())
    r1 = sum1(n)
    r2 = sum2(n)
    print('sum1 executed output:', r1)
    print('sum1 executed output:', r2)
    t = t - 1
