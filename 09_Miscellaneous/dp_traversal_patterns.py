n = 5
num = 1

dp = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n-i):
        dp[j][i+j] = num
        num += 1

# The matrix is now updated with the pattern
# You can print it to verify
for row in dp:
    print(' '.join(str(num).rjust(2) for num in row))

# Output:
#  1  6 10 13 15
#  0  2  7 11 14
#  0  0  3  8 12
#  0  0  0  4  9
#  0  0  0  0  5