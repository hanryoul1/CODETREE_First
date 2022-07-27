n = int(input())

if n == 2:
    print(28)

elif (n <= 7 and n % 2 != 0) or (n >8 and n % 2 == 0):
    print(31)

else:
    print(30)

# 2 => 28
# 1, 3, 5, 7, 8, 10, 12 => 31
# 4, 6, 9, 11 => 30