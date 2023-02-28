items = [
  {
    'product': 'pants',
    'price': 100
  },
  {
    'product': 'shirt',
    'price': 50
  },
  {
    'product': 'hat',
    'price': 20
  },
  {
    'product': 'jacket',
    'price': 300
  }
]

prices = list(map(lambda item: item['price'], items))
print(prices)

def add_taxes(item):
  item['tax'] = item['price'] * 0.19
  return item

new_items = list(map(add_taxes, items))
print(new_items)
print(items)

