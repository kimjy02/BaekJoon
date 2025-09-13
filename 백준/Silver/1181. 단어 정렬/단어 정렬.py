N = int(input())
words = {input().strip() for _ in range(N)}

for w in sorted(words, key = lambda x : (len(x), x)):
    print(w)