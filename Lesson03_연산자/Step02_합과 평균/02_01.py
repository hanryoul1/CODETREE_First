#Side note
a, b, c, d = 9, 4, 5, 7
arr = [9, 4, 5, 7]
print(sum(arr), sum(arr) / len(arr))

#Solution
num = input()
arr2 = num.split()
e = int(arr2[0])
f = int(arr2[1])
print(f"{e + f} {(e + f) / 2:.1f}")