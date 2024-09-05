def print_params(a = 1, b = 'строка', c = True):
    print('a =', a, 'b =', b, 'c =', c)

#1:
print_params()
print_params(20)
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(False, 'хорошо', [1, 2, 3])
print_params(*[1, 2, 3])

#2:
values_list = [3, False, 'привет']
values_dict = {'a': 10, 'b': 'ok', 'c': [5, 10, 20]}

print_params(*values_list)
print_params(**values_dict)

#3:
values_list_2 = [100.45, 'проверка']

print_params(*values_list_2, 42)

