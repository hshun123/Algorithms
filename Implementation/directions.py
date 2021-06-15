n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx <= 0 or nx > n or ny <= 0 or ny > n:
        continue
    x = nx
    y = ny

print(x, y)