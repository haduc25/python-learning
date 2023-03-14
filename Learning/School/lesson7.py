# Tuple
tuple1 = (1, 2, 3)

# tuple => list, array
tuple2 = list(tuple1)
tuple2.append(123)

# list, array => tuple
tuple1 = tuple(tuple2)

print('sum: ', sum(tuple1))
print('min: ', min(tuple1))
print('max: ', max(tuple1))
print('len: ', len(tuple1))
