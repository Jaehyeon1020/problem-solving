import time as _time

###### 입력 ######
n = int(input())
frusts = list(map(int, input().split()))
#################

_start_time = _time.time()  # 실행시간측정

###### 실행 ######
frusts.sort()
result = 0

required_member = 0
cur_members = 0

for f in frusts:
  required_member = f
  cur_members += 1

  if cur_members >= required_member:
    cur_members = 0
    required_member = 0
    result += 1

print(result)
#################

_end_time = _time.time()  # 실행시간측정
print("실행시간:", _end_time - _start_time, "초")  # 실행시간측정
