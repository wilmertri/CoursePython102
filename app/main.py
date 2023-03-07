import utils

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

def run():
  keys, values = utils.get_population()
  
  country = input('Ingrese el país: ')
  result = utils.population_by_country(populations, country)
  print(result)

if __name__ == '__main__':
  run()