import time

###### 입력 ######
n = int(input())
#################

start_time = time.time()  # 실행시간측정

###### 실행 ######
d = [0] * 1001
d[1] = 1
d[2] = 3

for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

print(d[n])
#################

end_time = time.time()  # 실행시간측정
print("실행시간:", end_time - start_time, "초")  # 실행시간측정
