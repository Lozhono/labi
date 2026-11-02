# 1
def pipe(*fns):
    for fn in fns:
        if not callable(fn):
            raise TypeError('arguments must be func')

    def composed(x):
        result = x
        for fn in fns:
            result = fn(result)
        return result
    return composed

# 2
def compose(*fns):
    handlers = []
    def composed(x):
        result = x
        for fn in reversed(fns):
            try:
                result = fn(result)
            except Exception as e:
                for handler in handlers:
                    handler(e)
                return None
        return result

    def on(event, handler):
        if event == 'error':
            handlers.append(handler)
    composed.on = on
    return composed

inc = lambda x: x + 1
twice = lambda x: x * 2
cube = lambda x: x ** 3

def fail(x):
    raise ValueError('error')

f = pipe(inc, twice, cube)
print(f(5))
f = pipe(inc, inc)
print(f(7))

try:
    f = pipe(inc, 7, cube)
except TypeError as e:
    print('Error:', e)

g = compose(inc, twice, cube)
print(g(5))
h = compose(inc, fail, cube)
h.on('error', lambda e: print('Error:', e))
print(h(5))