import sys
input = sys.stdin.readline

N = int(input())
solution = list(map(int, input().split()))

lo, hi = 0, N-1
best_sum = 10**18
best_pair = (solution[lo], solution[hi])

while lo < hi :
    ans = solution[lo] + solution[hi]

    if abs(ans) < abs(best_sum):
        best_sum = ans
        best_pair = (solution[lo], solution[hi])

    if ans == 0:
        # print(solution[lo], solution[hi])
        break
    elif ans > 0:
        hi -= 1
    else :
        lo += 1

print(best_pair[0], best_pair[1])
