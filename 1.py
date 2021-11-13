def func(a, b, c, d, e):
    return a and b and not e or (a and b or c or d) and not e


counter = 0
print("A B C D E : F")
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    if func(a, b, c, d, e):
                        print("%d %d %d %d %d : %d" % (a, b, c, d, e, func(a, b, c, d, e)))
                        counter += 1
print(counter)