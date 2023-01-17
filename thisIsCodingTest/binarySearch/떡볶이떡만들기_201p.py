import time

###### 입력 ######
n, m = map(int, input().split())
cakes = list(map(int, input().split()))
#################

start_time = time.time() # 실행시간측정

###### 실행 ######
def get_customer_cake(cakes, cutter):
    customer = 0

    for cake in cakes:
        if cake > cutter:
            customer += cake - cutter

    return customer

cakes.sort()

bottom = 0
top = 0
cutter = 0

def find():
    global cakes
    global n, m
    global bottom, top, cutter

    bottom = 0
    top = cakes[n - 1]

    while bottom <= top:
        cutter = (bottom + top) // 2

        # 고객이 받을 떡 길이 합 계산
        customer = get_customer_cake(cakes, cutter)
        
        if customer == m:
            return True
        elif customer > m:
            bottom = cutter + 1
        elif customer < m:
            top = cutter - 1
    
    return False

if find() == True:
    print(cutter)
else:
    if get_customer_cake(cakes, cutter) > m:
        while get_customer_cake(cakes, cutter) > m:
            cutter -= 1
        
        print(cutter + 1)
    else:
        while get_customer_cake(cakes, cutter) < m:
            cutter += 1

        print(cutter)
#################

end_time = time.time() # 실행시간측정

print("실행시간:", end_time - start_time, "초")