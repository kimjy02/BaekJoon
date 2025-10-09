import sys

input = sys.stdin.readline

M, N = map(int, input().split())

signatures = []

for _ in range(M):
    universe = list(map(int, input().split()))

    sorted_unique = sorted(set(universe))
    rank = {v: i for i, v in enumerate(sorted_unique)}

    compressed = tuple(rank[v] for v in universe)

    # print(compressed)
    signatures.append(compressed)
# print(signatures)

from collections import Counter

count = Counter(signatures)

answer = sum(c * (c - 1) // 2 for c in count.values())
print(answer)
