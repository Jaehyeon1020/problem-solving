n, m = map(int, input().split())
col, row, direction = map(int, input().split())
location = [col, row] # 행 열로 입력 받음

game_map = []
visited = [[False for i in range(m)] for j in range (n)]

for _ in range(n):
    game_map.append(list(map(int, input().split())))

def can_go_left():
    global location
    global visited
    global direction
    global game_map

    dir_copy = direction
    col_copy = location[0]
    row_copy = location[1]

    turn_left()
    move_forward()

    # 움직였을 때 바다인 곳이거나 방문한 곳이면 False
    if game_map[location[0]][location[1]] == 1 or visited[location[0]][location[1]] is True:
        direction = dir_copy
        location[0] = col_copy
        location[1] = row_copy
        return False
    else:
        direction = dir_copy
        location[0] = col_copy
        location[1] = row_copy
        return True

def can_go_back():
    global location
    global direction
    global game_map

    dir_copy = direction
    col_copy = location[0]
    row_copy = location[1]

    move_backward()

    # 움직였을 때 바다이면 false
    if game_map[location[0]][location[1]] == 1:
        direction = dir_copy
        location[0] = col_copy
        location[1] = row_copy
        return False
    else:
        direction = dir_copy
        location[0] = col_copy
        location[1] = row_copy
        return True

def set_visited():
    global location
    global visited

    visited[location[0]][location[1]] = True

def move_forward():
    global location
    global direction
    
    # 북쪽을 보고있을 때
    if direction == 0:
        location[0] += -1 # 위 행으로 이동

    # 동쪽을 보고있을 때
    elif direction == 1:
        location[1] += 1 # 오른쪽 열로 이동

    # 남쪽을 보고있을 때
    elif direction == 2:
        location[0] += 1 # 아래 행으로 이동

    # 서쪽을 보고있을 때
    elif direction == 3:
        location[1] += -1 # 왼쪽 열로 이동

def move_backward():
    global location
    global visited
    global direction
    
    # 북쪽을 보고있을 때 => 남쪽으로 이동해야됨
    if direction == 0:
        location[0] += 1 # 아래 행으로 이동

    # 동쪽을 보고있을 때
    elif direction == 1:
        location[1] += -1 # 왼쪽 열로 이동

    # 남쪽을 보고있을 때
    elif direction == 2:
        location[0] += -1 # 위 행으로 이동

    # 서쪽을 보고있을 때
    elif direction == 3:
        location[1] += 1 # 오른쪽 열로 이동

def turn_left():
    global direction

    direction = (direction + 3) % 4

set_visited()
dir_change = 0
while True:
    if can_go_left() is True:
        turn_left()
        move_forward()
        set_visited()
        dir_change = 0
    else:
        turn_left()
        dir_change += 1

    # 네 방향 모두 갈 수 없다면
    if dir_change == 4:
        # 뒤로 갈 수 있는지 체크
        if can_go_back() is True:
            move_backward()
            set_visited()
            dir_change = 0
        else:
            break

count = 0
for col in visited:
    for item in col:
        if item is True:
            count += 1

print(count)