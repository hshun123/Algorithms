n, m = map(int, input().split())

# map represents the visited routes
d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1 # current position is visited

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

#
dx = [-1, 0, 1, 0] 
dy = [0, 1, 0, -1]

def turn_left():
    global direction 
    direction -= 1
    if direction == -1:
        direction = 3

# simulation
count = 1
turn_time = 0
while True:

    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # if there is an unvisited positon
    if d[nx][ny] == 0 and array[nx][ny]:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    # no possible route
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # move backward if possible
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
