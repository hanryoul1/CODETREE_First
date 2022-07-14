rec = input()
arr = rec.split()
w, h = int(arr[0]), int(arr[1])

w += 8
h *= 3

print(w)
print(h)
print(w * h)