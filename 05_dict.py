dict = {}
for i in range(1, 5):
  dict[i] = i * 2

print(dict)

dict_v2 = {}
dict_v2 = { i * 2: i * 3 for i in range(1, 5) }
print(dict_v2)

import random
countries = ['col', 'mex', 'bol', 'per', 'ecu']
population = {}
for country in countries:
  population[country] = random.randint(0, 100)

print(population)

population_v2 = { country: random.randint(0, 100) for country in countries }
print(population_v2)

names = ['Fabi', 'Anto', 'Caro']
ages = [30, 18, 25]
print(list(zip(names, ages)))

new_dict = { name: age for (name, age) in zip(names, ages) }
print(new_dict)

new_dict_v2 = { names[i]:ages[i] for i in range(len(names)) }
print(new_dict_v2)
