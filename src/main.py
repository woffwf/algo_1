def max_experience(levels, experience):
    dp = [[0] * (i + 1) for i in range(levels)]


    for i in range(levels - 1, -1, -1):
        for j in range(i + 1):
            dp[i][j] = experience[i][j]
            if i < levels - 1:
                dp[i][j] += max(dp[i + 1][j], dp[i + 1][j + 1])

    return dp[0][0]



with open("career.in", "r") as file:
    levels = int(file.readline().strip())
    experience = [list(map(int, file.readline().split())) for _ in range(levels)]


result = max_experience(levels, experience)


with open("career.out", "w") as file:
    file.write(str(result))
