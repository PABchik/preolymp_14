def func1(a, b, c):
    return b and not (a and b and c)

def func2(a, b, c):
    return c and not (a and b and c)

def func3(a, b, c):
    return c and not (not a or not c)

def func4(a, b, c):
    return a or b and c

def func5(a, b, c):
    return c and not a or c and not b

def forEachFunc(f):
    print("A B C : F")
    for a in range(2):
        for b in range(2):
            for c in range(2):
                print("%d %d %d : %d" % (a, b, c, f(a, b, c)))

def normal():
    correctFuncResult = "01010100"
    result1 = ""
    result2 = ""
    result3 = ""
    result4 = ""
    result5 = ""

    for a in range(2):
        for b in range(2):
            for c in range(2):
                result1 += str(int(func1(a, b, c)))
                result2 += str(int(func2(a, b, c)))
                result3 += str(int(func3(a, b, c)))
                result4 += str(int(func4(a, b, c)))
                result5 += str(int(func5(a, b, c)))

    if result1 == correctFuncResult:
        print("1")
    if result2 == correctFuncResult:
        print("2")
    if result3 == correctFuncResult:
        print("3")
    if result4 == correctFuncResult:
        print("4")
    if result5 == correctFuncResult:
        print("5")

normal()

forEachFunc(func2)