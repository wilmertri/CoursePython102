numbers = [1, 2, 3, 4, 5, 6]
numbers_v2 = []
for number in numbers:
  numbers_v2.append(number * 2)

numbers_v3 = list(map(lambda i: i * 3, numbers))

print(numbers)
print(numbers_v2)
print(numbers_v3)

numbers1 = [2, 3, 4, 5, 6]
numbers2 = [3, 6, 9]

numbers3 = list(map(lambda x, y: x + y, numbers1, numbers2))
print(numbers3)