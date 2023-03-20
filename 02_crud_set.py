set_countries = {'col', 'mex', 'bol'}
size = len(set_countries)
print(size)

print('col' in set_countries)
print('per' in set_countries)

#add
set_countries.add('per')
print(set_countries)

#update
set_countries.update({'arg', 'ecu', 'per'})
print(set_countries)

#remove
set_countries.remove('fra')
print(set_countries)

#discard
set_countries.discard('col')
print(set_countries)

#clear
set_countries.clear()
print(set_countries)