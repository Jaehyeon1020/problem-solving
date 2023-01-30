import heapq
import sys

input = sys.stdin.readline
INF = 987654321

# 노드의 개수, 간선의 개수 입력
n, m = map(int, input().split())

# 시작 노드 번호 입력
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n + 1)]

# 최단거리 테이블 모두 INF로 초기화
distance = [INF for i in range(n + 1)]

# 모든 간선 정보 입력
for _ in range(m):
  a, b, c = map(int, input().split())  # a -> b로 가는 비용이 c
  graph[a].append((b, c))  # (노드, 비용)


def dijkstra(start):
  q = []  # 우선순위 큐

  # 시작 노드로 가는 비용은 0이며, 큐에 먼저 삽입함
  heapq.heappush(q, (0, start))  # (비용, 가려고 하는 노드)의 튜플로 삽입
  distance[start] = 0

  # 큐가 비어있지 않으면 계속해서 반복
  while q:
    # 가장 최단거리가 짧은 노드를 꺼내기
    dist, now = heapq.heappop(q)

    # 이미 처리된 노드(이미 최단거리)라면 무시
    if distance[now] < dist:
      continue

    # 현재 노드와 연결된 다른 노드들을 확인
    for n in graph[now]:
      cost = dist + n[1]  # idx 0: 노드, idx 1: 비용

      # 현재 노드를 거쳐서 가는 거리가 원래 계산되어있던 거리보다 짧은 경우 갱신
      # 새롭게 갱신했다면 힙에 삽입
      if cost < distance[n[0]]:
        distance[n[0]] = cost
        heapq.heappush(q, (cost, n[0]))


# 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 1):
  # 도달할 수 없는 경우 무한(INF) 출력
  if distance[i] == INF:
    print("INF")
  # 도달할 수 있는 경우 거리를 출력
  else:
    print(distance[i])
