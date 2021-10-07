cubes = []
for number in range(1, 1001, 2):
    cubes.append(number ** 3)

# пункт a)
result = 0
for cube in cubes:
    digits_sum = 0
    for digit in str(cube):
        digits_sum += int(digit)
    if digits_sum % 7 == 0:
        result += cube
print('Пункт a:', result)

# пункт b)
cubes_with_17 = []
for cube in cubes:
    cubes_with_17.append(cube + 17)

result = 0
for cube in cubes_with_17:
    digits_sum = 0
    for digit in str(cube):
        digits_sum += int(digit)
    if digits_sum % 7 == 0:
        result += cube
print('Пункт b:', result)

# пункт c), вариант 1:
result = 0
for cube in cubes:
    cube += 17
    digits_sum = 0
    for digit in str(cube):
        digits_sum += int(digit)
    if digits_sum % 7 == 0:
        result += cube
print('Пункт c (1):', result)

# пункт c), вариант 2:
for index in range(len(cubes)):
    cubes[index] = cubes[index] + 17

result = 0
for cube in cubes:
    digits_sum = 0
    for digit in str(cube):
        digits_sum += int(digit)
    if digits_sum % 7 == 0:
        result += cube
print('Пункт c (2):', result)
