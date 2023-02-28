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

def add_taxes(item):
  new_item = item.copy()
  new_item['tax'] = new_item['price'] * 0.19
  return new_item

new_items = list(map(add_taxes, items))
print(new_items)
print(items)