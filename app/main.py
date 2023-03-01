import utils

keys, values = utils.get_population()
print(keys, values)

populations = [
  {
    'country': 'Colombia',
    'population': 50
  },
  {
    'country': 'Brazil',
    'population': 120
  },
  {
    'country': 'Mexico',
    'population': 90
  }
]

country = input('Ingrese el país: ')
result = utils.population_by_country(populations, country)
print(result)