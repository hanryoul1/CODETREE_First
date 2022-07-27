n = 0
inp = input().split()
sym1, tem1 = inp[0], int(inp[1])

inp = input().split()
sym2, tem2 = inp[0], int(inp[1])

inp = input().split()
sym3, tem3 = inp[0], int(inp[1])

if (sym1 == 'Y' and tem1 >= 37):
    n += 1

if (sym2 == 'Y' and tem2 >= 37):
    n += 1

if (sym3 == 'Y' and tem3 >= 37):
    n += 1

if n >= 2:
    print('E')
else:
    print('N')
