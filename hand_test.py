from name_yourself import salary, hello_who

print(hello_who('Max'))

print(salary(2, 10))

if salary(2, 10) != 20:
    print('Failed!')

if hello_who('Max') != 'Hello, Max':
    print('Failed!')