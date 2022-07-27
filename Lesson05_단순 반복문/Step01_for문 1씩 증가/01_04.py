a = 60
b = 0

for i in range(1, a + 1):
    if a % i == 0:
        b += 1
    
print(b)