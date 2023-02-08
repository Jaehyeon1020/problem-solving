import time

###### 입력 ######
n, m = map(int, input().split())
roads = []

for _ in range(m):
  roads.append(list(map(int, input().split())))
#################

start_time = time.time()  # 실행시간측정

###### 실행 ######
parents = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
  parents[i] = i


def find_parent(parent_list, a):
  if parent_list[a] != a:
    parent_list[a] = find_parent(parent_list, parent_list[a])

  return parent_list[a]


def union_parent(parent_list, a, b):
  a = find_parent(parent_list, a)
  b = find_parent(parent_list, b)
  if a < b:
    parent_list[b] = a
  else:
    parent_list[a] = b


roads.sort(key=(lambda r: r[2]))
total_cost = 0
costs = []

for road in roads:
  a, b, cost = road

  if find_parent(parents, a) != find_parent(parents, b):
    union_parent(parents, a, b)
    total_cost += cost
    costs.append(cost)

total_cost -= max(costs)
print(total_cost)
#################

end_time = time.time()  # 실행시간측정
print("실행시간:", end_time - start_time, "초")  # 실행시간측정
