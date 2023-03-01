import sys
print(sys.path)

import re
text = 'Mi numero de telefono es 3124145321, el código del pais es 57 y mi número de la suerte es el 7'
result = re.findall('[0-9]+', text)
print(result)

import time
timestamp = time.time()
print(timestamp)

local = time.localtime()
result = time.asctime(local)
print(result)

import collections

numbers = [10, 25, 31, 45, 17, 25, 142]
counter = collections.Counter(numbers)
print(counter)