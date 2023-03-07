with open('./text.txt', 'w
+') as file:
  for line in file:
    print(line)
  file.write('\nNueva linea en el archivo')
  file.write('\nOtra linea')
  file.write('\nMas lineas')