# 한번 계산되었던 결과는 저장
d = [0] * 100

def fibo(x):
    global d

    # 피보나치 수열의 첫 번째, 두 번째 숫자는 1
    if x == 1 or x == 2:
        return 1

    # 이미 계산한 적이 있는 숫자라면 저장되어있는 숫자 반환    
    if d[x] != 0:
        return d[x]
    
    # 계산한 적이 없는 숫자라면 계산해서 저장하고 반환(Memoization)
    else:
        d[x] = fibo(x - 1) + fibo(x - 2)
        return d[x]

def fibo_bottomUp(x):
    global d

    d[1] = 1
    d[2] = 1

    for i in range(3, x + 1):
        d[i] = d[i - 1] + d[i - 2]

    return d[x]

print(fibo_bottomUp(5))
    
