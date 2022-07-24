n = input()
arr = n.split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])
min = 0

if (a <= b) and (a <= c):
    min = a

elif (b <= a) and (b <= c):
    min = b

else:
    min = c

print(min)