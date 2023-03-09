# for item in range(1, 100, 5):
#     print(item)


value = False

print(value)

# if value === true => false else => true
value2 = False if value else True
print(value2, end='/__\n')


# If the number of arguments is unknown, add a * before the parameter name:
def myFunc(*rest):
    for item in rest:
        # print(f'rest is {rest} and item is {item}', end='\n')
        print(f'Rest__{item} and length of array is {len(rest)}')
    # print('Meooow__', rest[1])


# myFunc('Bark', 'Pew', 'Duc', 'King', 'Lion')

"""_summary_
    while/else => chạy xong while thì tự động chạy else
    for/else => chạy xong for thì tự động chạy else
    """

# If the number of keyword arguments is unknown, add a double ** before the parameter name:


def myFuncArgumentsIsUnKnow(**rest):
    fname, mname, lname = rest.get('fname', ''), rest.get(
        'mname', ''), rest.get('lname', '')
    fullName = f'{fname} {mname} {lname}'
    print(
        f'\nMy first name is {fname} and my last name is {lname} \n=> My full name is: {fullName}')

    print(rest['meow'])
    print(rest)


myFuncArgumentsIsUnKnow(fname='Ha', mname='Minh', lname='Duc', meow='Meow')
