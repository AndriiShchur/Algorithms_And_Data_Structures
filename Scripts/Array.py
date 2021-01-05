print("Hello VS Code")

array = [10,7,3,5]
print(array)
print(array[2])
print(array[0:2])
print(array[:-1])

array = [10.0,7,'Adam',5]
print(array)

array[2] = ['Kevin']
print(array[2])

# Linear Search 0(N)

array = [10, 42, 55, 2, 1, 0]

max = array[0]

for num in array:
    if num > max:
        max = num

print(max)

min = array[0]

for num in array:
    if num < min:
        min = num

print(min)
