set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 3, 4, 1}
print(set_numbers)

set_diferent_types = {6, 'Hi', True, 2.5}
print(set_diferent_types)

set_from_string = set("Andreita")
print(set_from_string)

set_from_tuples = set(('abc', 123, False, 'abc'))
print(set_from_tuples)

numbers = [1, 2, 3, 2, 1, 4, 5, 3]
set_from_list = set(numbers)
print(set_from_list)
unique_numbers = list(set_from_list)
print(unique_numbers)