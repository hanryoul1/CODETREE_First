q = 0; s = 1; t = 1

for i in range(4):
    q = s + t
    t = s
    s = q

print(q)