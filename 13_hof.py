def increment(x):
  return x + 1

increment_v2 = lambda x : x + 1
result = increment_v2(50)
print(result)

def high_ord_func(x, func):
  return x + func(x)

result = high_ord_func(50, increment)
# 50 + (50 + 1)
print(result)

high_ord_func_v2 = lambda x, func: x + func(x)

result2 = high_ord_func_v2(50, increment_v2)
print(result2)
result3 = high_ord_func_v2(50, lambda x : x * 2)
# 50 + (50 * 2) 
print(result3)