n, m = map(int, input().split())
ice = []
visited = [[False for _ in range(m)] for _ in range(n)]
result = 0

for _ in range(n):
    ice.append(list(map(int,input())))

def dfs(x, y, visited, ice):
    # 범위 밖으로 탐색하는 경우 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 이미 완료된 곳 또는 칸막이에서 탐색 시작하면 종료
    if visited[x][y] == True or ice[x][y] == 1:
        return False

    visited[x][y] = True

    # 상하좌우로 dfs 탐색
    dfs(x - 1, y, visited, ice) # 상
    dfs(x + 1, y, visited, ice) # 하
    dfs(x, y - 1, visited, ice) # 좌
    dfs(x, y + 1, visited, ice) # 우
    return True

for i in range(n):
    for j in range(m):
        if dfs(i, j, visited, ice) == True:
            result += 1

print(result)