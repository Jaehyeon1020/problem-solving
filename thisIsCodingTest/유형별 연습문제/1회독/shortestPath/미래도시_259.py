import time
import sys

###### 입력 ######
n, m = map(int, input().split())
connections = []

for _ in range(m):
  connections.append(list(map(int, sys.stdin.readline().rstrip().split())))

x, k = map(int, input().split())
#################

start_time = time.time()  # 실행시간측정

###### 실행 ######
INF = 987654321
graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
  graph[i][i] = 0

for c in connections:
  graph[c[0]][c[1]] = 1
  graph[c[1]][c[0]] = 1  # 양방향 연결 구현

for d in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][d] + graph[d][b])

dist_to_K = graph[1][k]

if dist_to_K == INF:
  print(-1)
else:
  K_to_X = graph[k][x]

  if K_to_X == INF:
    print(-1)
  else:
    print(dist_to_K + K_to_X)
#################

end_time = time.time()  # 실행시간측정
print("실행시간:", end_time - start_time, "초")  # 실행시간측정
