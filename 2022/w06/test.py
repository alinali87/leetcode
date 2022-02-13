nums = [(3, 'b'), (2, 'a'), (1, 'c')]
a = sorted(nums, key=lambda x: x[1])
print(type(a))
print(a)