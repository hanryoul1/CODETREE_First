inp = input()
arr = inp.split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

if (b >= a and a >= c) or (c >= a and a >= b):
    print(a)

elif (a >= b and b >= c) or (c >= b and b>= a):
    print(b)

else:
    print(c)