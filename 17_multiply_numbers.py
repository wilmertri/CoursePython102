def multiply_numbers(numbers):
    return list(map(lambda x: x * 2, numbers))

numbers = [10, 25, 32, 41]
response = multiply_numbers(numbers)
print(response)