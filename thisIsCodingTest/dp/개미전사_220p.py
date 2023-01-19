import time

###### 입력 ######
n = int(input()) # 3- 100
nums = list(map(int, input().split())) # 0 - 1000
#################

start_time = time.time() # 실행시간측정

###### 실행 ######
d = [0] * 101
max_food = 0

d[1] = nums[0]
d[2] = max(nums[0], nums[1])

for i in range(3, n + 1):
    d[i] = max(d[i - 1], d[i - 2] + nums[i - 1]) # 전항까지의 최대 or 전전항까지의 최대 + 현재 값 중 선택

print(d[n])
#################

end_time = time.time() # 실행시간측정
print("실행시간:", end_time - start_time, "초") # 실행시간측정