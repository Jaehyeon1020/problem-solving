'''
그래프 구성

1 -> 2, 3, 8
2 -> 1, 7
3 -> 1, 4, 5
4 -> 3, 5
5 -> 3, 4
6 -> 7
7 -> 2, 6, 8
8 -> 1, 7
'''

from collections import deque

## 큐로 bfs 구현
def bfs(graph, v, visited):
    q = deque([v]) # 큐에 첫 노드 삽입
    visited[v] = True # 삽입 후 방문처리

    while len(q) != 0:
        # 삽입했던 노드 큐에서 빼내고 출력
        current_searching = q.popleft() # popleft : 왼쪽에서 빼냄
        print(current_searching, end=' ')

        # 큐에서 빼낸 노드와 인접한 방문되지 않은 노드들 큐에 삽입
        for n in graph[current_searching]:
            if visited[n] is False:
                q.append(n)
                visited[n] = True # 삽입 후 방문처리 (삽입 이후 방문처리 바로 안하면 큐에서 빠지기 전에 똑같은게 다시 들어올 수 있음)


# 노드가 1-8까지 존재한다면(0번 없이) visited[0]은 무시되어야 하므로 0-8까지 9개 요소 생성
visited = [False for _ in range(9)]

# 노드 개수 : 8
# adjacency list로 구현
graph = [
    [], # 0번 노드가 없으므로 비워놓고 graph[1]부터 시작할 수 있도록 처리
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 1번 노드부터 시작
v = 1

bfs(graph, v, visited)