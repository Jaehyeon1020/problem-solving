import time as _time

###### 입력 ######
n = int(input())
moneys = list(map(int, input().split()))
#################

_start_time = _time.time()  # 실행시간측정

###### 실행 ######
moneys.sort()  # 1, 2, 3, 8

target = 1
for m in moneys:
  if target < m:
    break

  target += m

print(target)
#################

_end_time = _time.time()  # 실행시간측정
print("실행시간:", _end_time - _start_time, "초")  # 실행시간측정
