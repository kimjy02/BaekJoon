import sys
input = sys.stdin.readline

def check(road, L):
    N = len(road)
    used = [False] * N

    for i in range(N - 1):
        diff = road[i+1] - road[i]

        if diff == 0:
            continue

        elif diff == 1:
            for j in range(i, i - L, -1):
                if j < 0 or road[j] != road[i] or used[j]:
                    return False
                used[j] = True

        elif diff == -1:
            for j in range(i + 1, i + L + 1):
                if j >= N or road[j] != road[i+1] or used[j]:
                    return False
                used[j] = True

        else:
            return False

    return True


N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for i in range(N):
    if check(board[i], L):
        ans += 1


for j in range(N):
    col = [board[i][j] for i in range(N)]
    if check(col, L):
        ans += 1

print(ans)
