
def sum_with_range(min, max):
  print(min, max)
  sum = 0
  for x in range(min,max):
    sum += x
  return sum

sum = sum_with_range(20,35)
print(sum)
sum2 = sum_with_range(sum, sum + 15)
print(sum2)