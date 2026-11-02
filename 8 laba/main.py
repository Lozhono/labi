# 1
def iterate(obj, callback):
    for key in obj:
        callback(key, obj[key], obj)

# 2
def store(value):
    def read():
        return value
    return read

# 3
def contract(fn, *types):
    *arg_types, result_type = types
    def wrapped(*args):
        if len(args) != len(arg_types):
            raise TypeError(f'Expected {len(arg_types)} arguments, got {len(args)}')
        for arg, t in zip(args, arg_types):
            if not isinstance(arg, t):
                raise TypeError(f'Argument {arg!r} is not of type {t.__name__}')
        result = fn(*args)
        if not isinstance(result, result_type):
            raise TypeError(f'Result {result!r} is not of type {result_type.__name__}')
        return result
    return wrapped

obj = {'a': 1, 'b': 2, 'c': 3}
iterate(obj, lambda key, value, o: print({'key': key, 'value': value}))
read = store(5)
value = read()
print(value)
add = lambda a, b: a + b
add_numbers = contract(add, int, int, int)
res = add_numbers(2, 3)
print(res)
concat = lambda s1, s2: s1 + s2
concat_strings = contract(concat, str, str, str)
res = concat_strings('Hello ', 'world!')
print(res)

try:
    add_numbers(2, '3')
except TypeError as e:
    print('Error:', e)