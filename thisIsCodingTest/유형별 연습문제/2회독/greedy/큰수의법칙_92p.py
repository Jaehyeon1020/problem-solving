import time as _time

###### 입력 ######
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
#################

_start_time = _time.time()  # 실행시간측정

###### 실행 ######
result = 0

data.sort(reverse=True)
max_num = data[0]
sec_num = data[1]

count = 0
max_count = 0

while count < m:
  if max_count == k:
    max_count = 0
    count += 1
    result += sec_num
  else:
    max_count += 1
    count += 1
    result += max_num

print(result)
#################

_end_time = _time.time()  # 실행시간측정
print("실행시간:", _end_time - _start_time, "초")  # 실행시간측정
