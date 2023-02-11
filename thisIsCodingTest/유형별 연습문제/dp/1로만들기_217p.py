import time

###### 입력 ######
x = int(input())
d = [0] * 30001
#################

start_time = time.time() # 실행시간측정

###### 실행 ######
d[1] = 0

for i in range(2, x + 1):
    d[i] = d[i - 1] + 1

    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
    
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

print(d[x])
#################

end_time = time.time() # 실행시간측정
print("실행시간:", end_time - start_time, "초") # 실행시간측정