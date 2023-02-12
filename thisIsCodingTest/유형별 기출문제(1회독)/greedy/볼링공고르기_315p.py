import time as _time

###### 입력 ######
n, m = map(int, input().split())
data = list(map(int, input().split()))
#################

_start_time = _time.time()  # 실행시간측정

###### 실행 ######
result = 0

for i in range(len(data) - 1):
  for j in range(i + 1, len(data)):
    if data[i] != data[j]:
      result += 1

print(result)
#################

_end_time = _time.time()  # 실행시간측정
print("실행시간:", _end_time - _start_time, "초")  # 실행시간측정
