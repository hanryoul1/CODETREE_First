a, b, c = 5, 6, 7

#1번
temp = a
a = c
c = b
b = temp
print(a)
print(b)
print(c)

#2번
a, b, c = c, a, b
print(a)
print(b)
print(c)