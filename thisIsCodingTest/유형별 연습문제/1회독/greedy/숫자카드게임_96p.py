n, m = map(int, input().split())
cards = []

for i in range(n):
    cards.append(list(map(int, input().split())))

maxVal = 0

for col in cards:
    comp = min(col)

    if maxVal < comp:
        maxVal = comp

print(maxVal)