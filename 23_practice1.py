numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_even = sum(list(filter(lambda x: x % 2 == 0, numbers)))
print(sum_even)

quote = "Hola, ¿cómo estás hoy?, Podemos hablar?"
count_words = len(quote.split())
print('words: ',count_words)

lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

list1 = set(lista1)
list2 = set(lista2)

list3 = list(list1.intersection(list2))
print(list3)

def tup_squares(numbers):
  result = []
  for n in numbers:
    t = (n, n**2)
    result.append(t)

  return result

n = [1, 2, 3, 4, 5]
result = tup_squares(n)
print(result)

def get_max_and_min(list_numbers):
  list_numbers.sort()
  return (list_numbers.pop(), list_numbers.pop(0))

l = [10, 3, 5, 6, 2, 8, 1]
nl = get_max_and_min(l)
print(nl)