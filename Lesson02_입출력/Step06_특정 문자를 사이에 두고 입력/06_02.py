date = input()
arr = date.split("-")
month, day, year = int(arr[0]), int(arr[1]), int(arr[2])

print(f"{year}.{month}.{day}")