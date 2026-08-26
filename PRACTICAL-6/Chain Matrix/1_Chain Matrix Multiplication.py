def M_C_M(arr):
    n = len(arr)
    m = [[0] * n for _ in range(n)]

    for T in range(2, n):
        for i in range(n - T):
            j = i + T

            m[i][j] = float('inf')

            for k in range(i + 1, j):
                cost = (
                    m[i][k]
                    + m[k][j]
                    + arr[i] * arr[k] * arr[j]
                )

                m[i][j] = min(m[i][j], cost)

    return m[0][n - 1]

arr = list(map(int, input("Enter matrix dimensions: ").split()))
result = M_C_M(arr)
print("Minimum number of scalar multiplications:", result)