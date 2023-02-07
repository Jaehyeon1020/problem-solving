import time

###### 입력 ######
n, m = map(int, input().split())
calculations = []

for _ in range(m):
  calculations.append(list(map(int, input().split())))
#################

start_time = time.time()  # 실행시간측정

###### 실행 ######


def find_parent(parent_list, node):
  if parent_list[node] != node:
    parent_list[node] = find_parent(parent_list, parent_list[node])

  return parent_list[node]


def union_team(parent_list, a, b):
  a = find_parent(parent_list, a)
  b = find_parent(parent_list, b)

  if a < b:
    parent_list[b] = a
  else:
    parent_list[a] = b


parents = [0 for _ in range(n + 1)]

for i in range(n + 1):
  parents[i] = i

for cal in calculations:
  # 팀 합치기
  if cal[0] == 0:
    union_team(parents, cal[1], cal[2])
  # 판별
  else:
    if parents[cal[1]] == parents[cal[2]]:
      print("YES")
    else:
      print("NO")
#################

end_time = time.time()  # 실행시간측정
print("실행시간:", end_time - start_time, "초")  # 실행시간측정
