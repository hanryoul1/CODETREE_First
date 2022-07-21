from unittest import result


me = input()
arr = me.split()
cm, kg = int(arr[0]), int(arr[1])
result = kg * 100 * 100 // (cm * cm) 

print(result)
if (result >= 25):
    print("Obesity")