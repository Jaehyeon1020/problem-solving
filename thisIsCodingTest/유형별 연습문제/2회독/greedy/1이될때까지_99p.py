import time as _time

###### 입력 ######
n, k = map(int, input().split())
#################

_start_time = _time.time()  # 실행시간측정

###### 실행 ######
count = 0

while n != 1:
  if n % k == 0:
    n = n // k
    count += 1
  else:
    n -= 1
    count += 1

print(count)

#################

_end_time = _time.time()  # 실행시간측정
print("실행시간:", _end_time - _start_time, "초")  # 실행시간측정
