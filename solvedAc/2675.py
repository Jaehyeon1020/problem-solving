T = int(input())
test = []
printStr = ""

for i in range(T):
    test.append(list(input().split()))

for case in test:
    for char in case[1]:
        printStr += char * int(case[0])
    
    print(printStr)
    printStr = ""