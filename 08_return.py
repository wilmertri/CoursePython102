def find_volume(length=1, width=1, depth=1):
  return length * width * depth, width, 'hello'

volume = find_volume()
print(volume)
volume, width, string = find_volume(width=15, depth=3)
print(volume, width, string)