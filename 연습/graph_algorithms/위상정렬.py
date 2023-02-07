from collections import deque

# 노드 개수, 간선 개수 입력
v, e = map(int, input().split())

# 모든 노드에 대해 진입차수 0으로 초기화
indegree = [0 for _ in range(v + 1)]

# 각 노드에 연결된 간선 정보를 담는 연결 리스트 초기화
graph = [[] for _ in range(v + 1)]

# 방향 그래프의 모든 간선 정보 입력
for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)  # 정점 A -> B 연결
  indegree[b] += 1  # b의 진입차수 1 증가

# 위상정렬


def topology_sort():
  result = []  # 수행 결과 리스트
  q = deque()

  # 처음 시작할 때 진입차수 0인 노드 큐에 삽입
  for i in range(1, v + 1):
    if indegree[i] == 0:
      q.append(i)

  # 큐 빌때까지 반복
  while q:
    now = q.popleft()
    result.append(now)

    # 지금 꺼낸 원소와 연결되어있던 노드에서 진입차수 1 빼기
    for i in graph[now]:
      indegree[i] -= 1

      # 새롭게 진입차수가 0이 된 노드를 큐에 삽입
      if indegree[i] == 0:
        q.append(i)

  # 결과 출력
  for r in result:
    print(r, end=' ')


topology_sort()
