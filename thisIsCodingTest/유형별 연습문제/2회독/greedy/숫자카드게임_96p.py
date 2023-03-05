import time as _time

###### 입력 ######
n, m = map(int, input().split())
cards = []

for _ in range(n):
  cards.append(list(map(int, input().split())))
#################

_start_time = _time.time()  # 실행시간측정

###### 실행 ######
nums = []

for col in cards:
  nums.append(min(col))

print(max(nums))
#################

_end_time = _time.time()  # 실행시간측정
print("실행시간:", _end_time - _start_time, "초")  # 실행시간측정
