arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(512, 1024):
    i = bin(i)[2:].replace("0", "")
    arr[len(i) - 1] += 1

print(arr)
