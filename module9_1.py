
def pov_by_2(x):
    return x**2

numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
print('in  = ',numbers)

result = map(pov_by_2, filter(lambda x: x % 2 in numbers, numbers) )

print(result)
print('out = ',list(result))