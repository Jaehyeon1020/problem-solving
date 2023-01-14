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

## 재귀함수로 dfs 구현
def dfs(graph, v, visited):
    visited[v] = True # 방문 처리
    print(v, end=' ') # 방문 노드 출력

    # 현재 노드에서 연결된 방문하지 않은 다른 노드 방문(재귀 호출)
    for i in graph[v]:
        if visited[i] is False:
            dfs(graph, i, visited)


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

dfs(graph, v, visited)