price = 100 # global scope

def increment():
  price = 200 # local
  result = price + 10
  print(result)
  return result

print(price)
price = increment()
print(price)