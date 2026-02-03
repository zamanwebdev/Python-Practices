a = 30 # Global Scope / Variables
b = 20
def hablu():
    global a
    a = 100
    x = 10 # Local Scope / Variables
    print(x)
    print(a)
hablu()
print(a)
