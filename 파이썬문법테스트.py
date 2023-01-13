a = 1

def globA():
    global a
    a = 3

def noglob(a):
    print("noglob", a)

globA()
noglob(6)
print(a)