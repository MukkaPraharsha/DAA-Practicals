def knapsack(w, val, wt):
    n = len(wt)

    dp = [[0 for _ in range(w + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(w + 1):

            if i == 0 or j == 0:
                dp[i][j] = 0

            else:
                pick = 0

                if wt[i - 1] <= j:
                    pick = val[i - 1] + dp[i - 1][j - wt[i - 1]]

                not_pick = dp[i - 1][j]

                dp[i][j] = max(pick, not_pick)

    return dp[n][w]

n = int(input("Enter number of items: "))
val = list(map(int, input("Enter values: ").replace(",", " ").split()))
wt = list(map(int, input("Enter weights: ").replace(",", " ").split()))
w = int(input("Enter capacity of knapsack: "))

result = knapsack(w, val, wt)

print("Maximum value =", result)