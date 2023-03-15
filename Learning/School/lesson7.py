import GlobalFunction as gf

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

# Set
# gán giá trị cho 1 set()
mySet = {1, 2, 3, 'Một', 'Hai', 'Ba'}


# dùng hàm khởi tạo set
set1 = {1, 2, 3, 4}
set2 = {'Một', 'Hai', 'Ba'}
set3 = {7, 8, 9, 10}
set1.intersection_update(set3)
print('set1: {0}'.format(set1))
print(set2)  # rỗng => chỉ lấy phẩn có tồn tại trong cả 2 set

# exam
set1 = {1, 2, 3, 4}
set2 = {4, 8, 9, 10}
set1.intersection_update(set2)
print('set1: {0}'.format(set1))  # {4}

gf.print_colored('union', 'red')

# union
set1 = {1, 2, 3, 4}
set2 = {'Một', 'Hai', 'Ba'}
set3 = {7, 8, 9, 10}

# Using union() method
set4 = set1.union(set3)
print(set4)

# Using | operator
set5 = set2 | set3
print(set5)
