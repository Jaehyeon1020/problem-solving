import time
import sys

###### 입력 ######
n = int(input())
lectures = [[] for _ in range(n + 1)]

input2 = sys.stdin.readline

for i in range(1, n + 1):
  lectures[i] = list(map(int, input2().rstrip().split()))
#################

start_time = time.time()  # 실행시간측정

###### 실행 ######
lecture_times = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
  time_ = lectures[i][0]

  if len(lectures[i]) > 2:
    prev_lectures = lectures[i][1: len(lectures[i]) - 1]
    prev_times = []

    for p in prev_lectures:
      prev_times.append(lecture_times[p])

    lecture_times[i] = time_ + max(prev_times)

  else:
    lecture_times[i] = time_

for i in range(1, len(lecture_times)):
  print(lecture_times[i])
#################

end_time = time.time()  # 실행시간측정
print("실행시간:", end_time - start_time, "초")  # 실행시간측정
