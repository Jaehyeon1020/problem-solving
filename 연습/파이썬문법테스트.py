arr = [1, 2, 3, 4, 5]

count = 0
newArr = []
for item in arr[::-1]:
    if count == 7:
        break

    newArr.append(item)
    count += 1

print(newArr)
