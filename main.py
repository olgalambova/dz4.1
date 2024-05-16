numbers = [9, 0, 4, 0, 2, 0, 4, 6, 9]
new_numbes = []

for i in range(len(numbers)):
    if numbers[i] > 0:
        new_numbes.append(numbers[i])

print(new_numbes)
count_zeros = numbers.count(0)

print(count_zeros)

for _ in range(count_zeros):
    new_numbes.append(0)

print(new_numbes)