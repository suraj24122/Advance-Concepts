numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]


nums = [10, 15, 20, 25]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [10, 20]


from functools import reduce

nums = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, nums)
print(total)  # Output: 10
