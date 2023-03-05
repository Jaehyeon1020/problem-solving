import time as _time

###### 입력 ######
s = input()
#################

_start_time = _time.time()  # 실행시간측정

###### 실행 ######
prev = s[0]

group_0 = 0
group_1 = 0

if prev == '0':
  group_0 += 1
else:
  group_1 += 1

for i in range(1, len(s)):
  if s[i] != prev:
    if s[i] == '0':
      group_0 += 1
    else:
      group_1 += 1

  prev = s[i]

print(min(group_0, group_1))
#################

_end_time = _time.time()  # 실행시간측정
print("실행시간:", _end_time - _start_time, "초")  # 실행시간측정
