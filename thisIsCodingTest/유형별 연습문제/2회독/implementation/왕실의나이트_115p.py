import time as _time

###### 입력 ######
loc = input()
#################

_start_time = _time.time()  # 실행시간측정

###### 실행 ######
count = 0

row = int(ord(loc[0]) - ord('a') + 1)
col = int(loc[1])

moves = [(2, 1), (-2, 1), (2, -1), (-2, -1),
         (1, 2), (-1, 2), (1, -2), (-1, -2)]

for m in moves:
  cur_row = row
  cur_col = col

  cur_row += m[0]
  cur_col += m[1]

  if cur_row < 1 or cur_row > 8:
    continue
  elif cur_col < 1 or cur_col > 8:
    continue
  else:
    count += 1

print(count)
#################

_end_time = _time.time()  # 실행시간측정
print("실행시간:", _end_time - _start_time, "초")  # 실행시간측정
