def increment(x):
  return x + 1

number = increment(10)
print(number)

increment_v2 = lambda x : x + 1
result = increment_v2(50)
print(result)

full_name = lambda name, last_name: f'Fullname is {name.title()} {last_name.title()}'
fullname =  full_name("fabian", "triana")
print(fullname)