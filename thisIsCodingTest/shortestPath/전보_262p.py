import time
import sys
import heapq

###### 입력 ######
n, m, c = map(int, input().split())
roads = []

for _ in range(m):
  roads.append(list(map(int, sys.stdin.readline().rstrip().split())))
#################

start_time = time.time()  # 실행시간측정

###### 실행 ######
INF = 987654321
distance = [INF for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

for r in roads:
  x, y, z = r
  graph[x].append((y, z))


def dijkstra(start):
  q = []

  distance[start] = 0
  heapq.heappush(q, (0, start))

  while q:
    dist, cur = heapq.heappop(q)

    if distance[cur] < dist:
      continue

    for n in graph[cur]:
      cost = dist + n[1]

      if cost < distance[n[0]]:
        distance[n[0]] = cost
        heapq.heappush(q, (cost, n[0]))


dijkstra(c)

count = 0
times = []
for i in range(1, len(distance)):
  if distance[i] != INF and distance[i] != 0:
    count += 1
    times.append(distance[i])

print(count, max(times))
#################

end_time = time.time()  # 실행시간측정
print("실행시간:", end_time - start_time, "초")  # 실행시간측정
