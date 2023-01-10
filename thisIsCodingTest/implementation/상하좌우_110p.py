def moving(dir, x, y, n):
    if dir == 'R':
        if y < n:
            return (0, 1)
    
    elif dir == 'L':
        if y > 1:
            return (0, -1)
    
    elif dir == 'U':
        if x > 1:
            return (-1, 0)
    
    elif dir == 'D':
        if x < n:
            x += 1
            return (1, 0)

    return (0, 0)

n = int(input())
moves = list(input().split())

x = 1
y = 1

for move in moves:
    current_move = moving(move, x, y, n)
    x += current_move[0]
    y += current_move[1]

print(x, y)

        