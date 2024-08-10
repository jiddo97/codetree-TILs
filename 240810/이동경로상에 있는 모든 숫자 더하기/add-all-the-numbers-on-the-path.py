def direction_index(dir):
    directions = ['N', 'E', 'S', 'W']
    return directions.index(dir)

def move_position(x, y, direction):
    if direction == 'N':
        return x - 1, y
    elif direction == 'E':
        return x, y + 1
    elif direction == 'S':
        return x + 1, y
    elif direction == 'W':
        return x, y - 1

N, T = map(int, input().split())
commands = input().strip()
grid = [list(map(int, input().split())) for _ in range(N)]

x, y = N // 2, N // 2
direction = 'N'
total_sum = 0

for command in commands:
    if command == 'L':
        if direction == 'N':
            direction = 'W'
        elif direction == 'W':
            direction = 'S'
        elif direction == 'S':
            direction = 'E'
        elif direction == 'E':
            direction = 'N'
    elif command == 'R':
        if direction == 'N':
            direction = 'E'
        elif direction == 'E':
            direction = 'S'
        elif direction == 'S':
            direction = 'W'
        elif direction == 'W':
            direction = 'N'
    elif command == 'F':
        new_x, new_y = move_position(x, y, direction)
        if 0 <= new_x < N and 0 <= new_y < N:
            x, y = new_x, new_y
            total_sum += grid[x][y]

print(total_sum)