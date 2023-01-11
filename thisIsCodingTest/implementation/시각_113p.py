n = int(input())

result = 0

def include3(num):
    if 30 <= num < 40 or num % 10 == 3:
        return True
    else:
        return False

for time in range(n + 1):
    for min in range(60):
        for sec in range(60):
            if include3(time) or include3(min) or include3(sec):
                result += 1

print(result)