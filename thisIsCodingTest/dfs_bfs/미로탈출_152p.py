from collections import deque

n, m = map(int, input().split())
road = []
visited = [[False for _ in range(m)] for _ in range(n)]

for _ in range(n):
    road.append(list(map(int, input())))

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([(x, y)])
    visited[x][y] = True

    while len(q) != 0:
        current = q.popleft()

        for i in range(4):
            new_x = current[0] + dx[i]
            new_y = current[1] + dy[i]

            if (0 <= new_x < n 
            and 0 <= new_y < m 
            and road[new_x][new_y] != 0 
            and visited[new_x][new_y] == False):
                q.append((new_x, new_y))
                visited[new_x][new_y] = True
                road[new_x][new_y] = road[current[0]][current[1]] + 1

bfs(0,0)

print(road[n-1][m-1])
                
