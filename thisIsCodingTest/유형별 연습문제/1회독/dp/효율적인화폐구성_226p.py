import time

###### 입력 ######
n, m = map(int, input().split())
moneys = []

for _ in range(n):
    moneys.append(int(input()))
#################

start_time = time.time()  # 실행시간측정

###### 실행 ######
d = [-1] * (m + 1)

for money in moneys:
    if money <= m:
        d[money] = 1

for i in range(max(moneys) + 1, m + 1):
    able = []  # 가능한 경우의 수 저장

    for money in moneys:
        if d[i - money] != -1:
            able.append(d[i - money] + 1)

    if able:
        d[i] = min(able)

print(d[m])
#################

end_time = time.time()  # 실행시간측정
print("실행시간:", end_time - start_time, "초")  # 실행시간측정
