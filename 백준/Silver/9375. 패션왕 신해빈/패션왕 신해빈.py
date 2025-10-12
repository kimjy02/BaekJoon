import sys
import math
input = sys.stdin.readline

T = int(input())  # 테스트케이스 수


for _ in range(T):
    n = int(input())
    dict = {}
    for _ in range(n):
        clothes, kind = map(str, input().split())
        if kind not in dict:
            dict[kind] = 0
        dict[kind] += 1

    kind_cnt = list(dict.values())
    kind_cnt = list(map(lambda x: x + 1, kind_cnt))
    cnt = math.prod(kind_cnt) - 1

    print(cnt)
    # print(type(dict.values()))
    # print(dict)
