# https://www.acmicpc.net/problem/11404

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b :
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    