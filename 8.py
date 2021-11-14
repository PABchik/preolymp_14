a = 3196
b = 1128

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
print(a + b)