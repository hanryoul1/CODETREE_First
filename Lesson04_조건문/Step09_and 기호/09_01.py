a = input()
arr1 = a.split()
a1, a2 = int(arr1[0]), int(arr1[1])

b = input()
arr2 = b.split()
b1, b2 = int(arr2[0]), int(arr2[1])

if (a1 > b1) and (a2 > b2):
    print(1)

else:
    print(0)