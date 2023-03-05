location = input()
result = 0

# ord()로 아스키코드 뽑을 수 있음
def move_horizonal(location):
    num = 0

    # 왼쪽으로 이동 가능한지 여부
    if ord(location[0]) >= ord('c'): 
        # 수직으로 이동 가능 여부
        if 2 <= int(location[1]) <= 7:
            num += 2
        else:
            num += 1
    
    # 오른쪽으로 이동 가능한지 여부
    if ord(location[0]) <= ord('f'):
        # 수직으로 이동 가능 여부
        if 2 <= int(location[1]) <= 7:
            num += 2
        else:
            num += 1

    return num

def move_vertical(location):
    num = 0

    # 위로 이동 가능 여부
    if int(location[1]) >= 3:
        if ord('b') <= ord(location[0]) <= ord('g'):
            num += 2
        else:
            num += 1

    # 아래로 이동 가능 여부
    if int(location[1]) <= 6:
        if ord('b') <= ord(location[0]) <= ord('g'):
            num += 2
        else:
            num += 1

    return num

result += move_horizonal(location) + move_vertical(location)

print(result)
