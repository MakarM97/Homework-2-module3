def print_params(a=1, b='string', c=True):
    print(a, b, c)


print_params()
print_params(1, 'string')
print_params
print_params(b=25)
print_params(c=[1, 2, 3])


values_list = [1, 'apple', False]
values_dict = {'a': 1, 'b': 'string', 'c': True}


print_params(*values_list)
print_params(**values_dict)


values_list2 = [5, 2.4]

print_params(*values_list2,42)