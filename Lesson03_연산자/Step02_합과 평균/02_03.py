num = input()
arr = num.split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

sum = a + b + c
ave = (a + b + c) // 3
result = sum - ave

print(sum)
print(ave)
print(result)