import time as _time

###### 입력 ######
n, m = map(int, input().split())
a, b, d = map(int, input().split())
game_map = []

for _ in range(n):
  game_map.append(list(map(int, input().split())))
#################

_start_time = _time.time()  # 실행시간측정

###### 실행 ######


def leftof(cur_dir):  # 왼쪽방향이 어딘지 얻기
  if cur_dir == 0:
    return 3
  else:
    return cur_dir - 1


def get_moving_pos(cur_pos, cur_dir):  # 앞으로 전진하면 가게 될 위치 얻기
  moving_pos = [cur_pos[0], cur_pos[1]]

  # 북쪽을 보고있는 경우
  if cur_dir == 0:
    moving_pos[0] -= 1
  # 동쪽을 보고있는 경우
  elif cur_dir == 1:
    moving_pos[1] += 1
  # 남쪽을 보고있는 경우
  elif cur_dir == 2:
    moving_pos[0] += 1
  # 서쪽을 보고있는 경우
  elif cur_dir == 3:
    moving_pos[1] -= 1

  return moving_pos


def get_back_pos(cur_pos, cur_dir):  # 뒤로 가면 가게 될 위치 얻기
  moving_pos = [cur_pos[0], cur_pos[1]]

  # 북쪽을 보고있는 경우
  if cur_dir == 0:
    moving_pos[0] += 1
  # 동쪽을 보고있는 경우
  elif cur_dir == 1:
    moving_pos[1] -= 1
  # 남쪽을 보고있는 경우
  elif cur_dir == 2:
    moving_pos[0] -= 1
  # 서쪽을 보고있는 경우
  elif cur_dir == 3:
    moving_pos[1] += 1

  return moving_pos


cur_position = [a, b]
cur_direction = d
visited = [[0 for _ in range(m)] for _ in range(n)]
rotation = 0

while True:
  # 네 방향 모두 갈 수 없는 경우
  if rotation == 4:
    back = get_back_pos(cur_position, cur_direction)

    if game_map[back[0]][back[1]] == 1:
      break
    else:
      cur_position = back  # 뒤로 이동
      rotation = 0  # 회전수 초기화
      visited[cur_position[0]][cur_position[1]] = 1  # 방문 처리
      continue

  next = get_moving_pos(cur_position, leftof(cur_direction))

  # 다음 갈 곳이 육지이면서 아직 방문한적이 없는지 체크
  if game_map[next[0]][next[1]] == 0 and visited[next[0]][next[1]] == 0:
    cur_direction = leftof(cur_direction)  # 왼쪽으로 회전
    cur_position = get_moving_pos(cur_position, cur_direction)  # 이동
    visited[cur_position[0]][cur_position[1]] = 1  # 방문 체크
    rotation = 0  # 회전수 초기화
    continue
  else:
    cur_direction = leftof(cur_direction)  # 회전만 수행
    rotation += 1  # 회전수 증가

count = 0

for v in visited:
  for vv in v:
    if vv == 1:
      count += 1

print(count)
#################

_end_time = _time.time()  # 실행시간측정
print("실행시간:", _end_time - _start_time, "초")  # 실행시간측정
