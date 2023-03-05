import time as _time

###### 입력 ######
s = list(map(int, input()))
#################

_start_time = _time.time()  # 실행시간측정

###### 실행 ######
result = s[0]

for i in range(1, len(s)):
  cur = s[i]

  if result + cur >= result * cur:
    result += cur
  else:
    result *= cur

print(result)
#################

_end_time = _time.time()  # 실행시간측정
print("실행시간:", _end_time - _start_time, "초")  # 실행시간측정
