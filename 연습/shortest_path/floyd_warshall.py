INF = 987654321

# 노드, 간선 개수 입력
n = int(input())
m = int(input())

# 2차원 리스트(그래프)를 만들고 모든 값 무한으로 초기화
graph = [[INF for _ in range(n + 1)] for __ in range(n + 1)]

# 자신 -> 자신으로 움직이는 비용은 0으로 초기화
for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아 그 값으로 초기화(간선 개수만큼 입력 받아야됨)
for _ in range(m):
  a, b, c = map(int, input().split())  # a -> b로 가는 비용 = c
  graph[a][b] = c

##### 플로이드 워셜 알고리즘 수행 #####
# 노드 k를 거쳐가는 모든 a -> b 거리 계산
# 하나의 k값에 대해 모든 a -> b 경우의 수를 계산 하고 다음 k값으로 넘어감
for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      # 지금까지 계산된 a->b 거리와 k를 거쳐서 a->b로 이동하는 거리를 비교해 더 짧은 쪽을 선택
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
  for b in range(1, n + 1):
    # 도달할 수 없는 경우 INF 출력
    if graph[a][b] == INF:
      print("INF", end=' ')
    # 도달 가능한 경우 거리 출력
    else:
      print(graph[a][b], end=' ')
  print()
