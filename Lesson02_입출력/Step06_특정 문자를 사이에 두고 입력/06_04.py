date = input()
arr = date.split(".")
year, month, day = int(arr[0]), int(arr[1]), int(arr[2])

print(f"{month}-{day}-{year}")