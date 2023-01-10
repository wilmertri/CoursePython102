import random
countries = ['col', 'mex', 'bol', 'per', 'ecu']
populations = { country: random.randint(0, 100) for country in countries }
print(populations)

result = { country:population for (country,population) in populations.items() if population > 50}
print(result)

text = 'Hi, my name is Fabian and I love Python'
unique = { c:c.upper() for c in text if c in 'aeiou' }
print(unique)

frequency_vowels = { c:text.count(c) for c in text if c in 'aeiou'}
print(frequency_vowels)
