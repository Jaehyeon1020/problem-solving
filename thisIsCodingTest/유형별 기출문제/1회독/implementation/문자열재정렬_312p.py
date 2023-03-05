import time as _time

###### 입력 ######
s = input()
#################

_start_time = _time.time()  # 실행시간측정

###### 실행 ######
strs = []
nums = []

for ss in s:
  try:
    nums.append(int(ss))
  except:
    strs.append(ss)

strs.sort()

print(''.join(strs) + str(sum(nums)))

#################

_end_time = _time.time()  # 실행시간측정
print("실행시간:", _end_time - _start_time, "초")  # 실행시간측정
