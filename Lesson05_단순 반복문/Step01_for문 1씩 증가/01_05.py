N = 128
result = 0

for i in range(1, N):
    if N % i == 0:
        result += i

print(result)