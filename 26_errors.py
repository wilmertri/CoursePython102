try:
  print(25 / 2)
  assert 1 != 1, 'Uno no es igual que uno'
  age = 10
  if age < 18:
    raise Exception('No se permite menores de edad')
except ZeroDivisionError as error:
  print(error)
except AssertionError as error:
  print(error)
except Exception as error:
  print(error)
  
print('Hola')