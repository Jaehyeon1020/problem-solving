inputs = []

for i in range(9):
    inputs.append(int(input()))

maxVal = max(inputs)

print(maxVal)
print(inputs.index(maxVal) + 1)