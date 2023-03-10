import time as _time

###### 입력 ######
n, m = map(int, input().split())
ice = []

for _ in range(n):
  ice.append(list(map(int, input())))
#################

_start_time = _time.time()  # 실행시간측정

###### 실행 ######


def dfs(col, row):
  if col < 0 or col > n - 1 or row < 0 or row > m - 1:
    print("out")
    return

  ice[col][row] = 1

  dfs(col - 1, row)  # 상
  dfs(col + 1, row)  # 하
  dfs(col, row - 1)  # 좌
  dfs(col, row + 1)  # 우


count = 0

# for col in range(n):
#   for row in range(m):
#     if ice[col][row] == 0:
#       count += 1
#       dfs(col, row)

print(count)
#################

_end_time = _time.time()  # 실행시간측정
print("실행시간:", _end_time - _start_time, "초")  # 실행시간측정
