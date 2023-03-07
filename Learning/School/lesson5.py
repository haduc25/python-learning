myList = ['a', 'b', 'c', 'd']
print('My list is: ', myList)
print('My list from index 2 is: ', myList[2])
print('My list from last index is: ', myList[-1])
print('My list from last index + 1 (-2) is: ', myList[-2])

print(type(myList))

####################################
print('#'*25, end='\n')

#         0  1  2  3  4  5  6  7  8  9
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = 3
b = 7

# from 3 to 6 (index) | start:end -1
print(f'From A({a}) to B({b}) is', myList[a:b])  # [4, 5, 6, 7]
print('From -4 to -1 is ', myList[-4:-1])  # [7, 8, 9]

############### Check Exists or not in List ###############
print('#'*25, end='\n')
myList = ['MaSV', 'Banana', 'Cherry', 'Orange']


def checkExistsInListOrNot(list, strNeedCheck):
    if (strNeedCheck in list):
        print('Have value', strNeedCheck)
        return

    print('Dont have value', strNeedCheck)


checkExistsInListOrNot(myList, 'Banana')

# thay đổi giá trị dựa vào khoảng index
print('\nList before replace is: ', myList)
myList[1:3] = ['Meow', 'Kiwi']
print('List after replaced is: ', myList)

# add value to list | append( )/ thêm vào cuối, insert() / chèn vào vị trí index

# append()
print('\nList before is: ', myList)
myList.append('Value')
print('List after is: ', myList)

# insert()
print('\nList before is: ', myList)
myList.insert(3, 'Value with index is 3')
print('List after is: ', myList)

# extend() / gộm list
myList1 = ['value1', 'value2', 'value3']
myList2 = ['value4', 'value5', 'value6']

# gộp vào list1
print('\nmyList1 efore extend is ', myList1)
myList1.extend(myList2)
print('myList1 hen extended is ', myList1)


# remove(), pop() / xoa pt theo index
# remove
myList = ['MaSV', 'Banana', 'Cherry', 'Orange', 'Banana']
print('\nmyList before is ', myList)
myList.remove('Banana')  # remove first element found
print('myList after is ', myList)

# pop
myList = ['MaSV', 'Banana', 'Cherry', 'Orange', 'Banana']
print('\nmyList before is ', myList)
myList.pop(1)  # remove by index
print('myList after is ', myList)

# pop remove all
while len(myList) != 0:
    myList.pop(0)  # xoa pt dau
    # myList.pop()  # xoa pt cuoi

print('myList when pop all: ', myList)


# clear()
myList = ['MaSV', 'Banana', 'Cherry', 'Orange', 'Banana']
print('\nmyList before is ', myList)
myList.clear()
print('myList after is ', myList)


# pop last index
myList = ['MaSV', 'Banana', 'Cherry', 'Orange', 'Banana']
print('\nmyList before is ', myList)
myList.pop()  # remove last index
print('myList after remove last index with pop is ', myList)


# duyệt danh sách
myList = ['MaSV', 'Banana', 'Cherry', 'Orange', 'Banana']

# for/in
for i in myList:
    # print('for/in: ', i)
    print(i, end=' - ')

print('\n')
# for/range
for i in range(len(myList)):
    # print('for/range: ', myList[i])
    print(myList[i], end=' - ')


# new list using Comprehension
myList = ['MaSV', 'Banana', 'Cherry', 'Orange', 'Banana', 'Beow']
newList = []

# for i in myList:
# if ''


#
# newList = [x for x in myList] # lấy toàn bộ
# newList = [x for x in myList if 'a' in x] # chi lay ten co ky tu a

# sort() / alpha, arr.sort(reverse = True), arr.sort(key = myFunc), abs()
# lower(), reverse(), copy()

myList = ['MaSV', 'Banana', 'Cherry', 'Orange', 'Banana', 'Beow']
newList = myList.copy()  # sử dụng hàm copy
newList2 = list(myList)  # sử dụng hàm tạo list

print('\nnewList is ', newList)
print('\nnewList2 is ', newList2)


# nối ds
list1 = [1, 2, 3]
list2 = [4, 2, 3]

list3 = list1 + list2

print('List3 is ', list3)
