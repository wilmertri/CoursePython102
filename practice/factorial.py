from functools import reduce

num = int(input("Ingrese un número entero positivo: "))

r = list(range(1, num + 1))
print(r)
fact = reduce(lambda x, y: x * y, r)

print(fact)