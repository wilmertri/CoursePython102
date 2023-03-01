def get_population():
  keys = ['Col', 'Bol', 'Arg', 'Ecu']
  values = [100, 50, 150, 20]
  return keys, values

def population_by_country(data, country):
  result = list(filter(lambda item: item['country'] == country, data))
  return result