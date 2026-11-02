#1
def seq(*funcs):
    def inner(arg):
        if isinstance(arg, (int, float)):
            result = arg
            for f in reversed(funcs):
                result = f(result)
            return result
        return seq(*funcs, arg)
    return inner

#2
def array():
    items = []
    def get(i):
        if 0 <= i < len(items):
            return items[i]
        return None

    def push(value):
        items.append(value)

    def pop():
        if items:
            return items.pop()
        return None
    get.push = push
    get.pop = pop
    return get


print(seq(lambda x: x + 7)(lambda x: x * 2)(5))
print(seq(lambda x: x * 2)(lambda x: x + 7)(5))
print(seq(lambda x: x + 1)(lambda x: x * 2)(lambda x: x / 3)(lambda x: x - 4)(7))
arr = array()
arr.push('first')
arr.push('second')
arr.push('third')
print(arr(0))
print(arr(1))
print(arr(2))
print(arr.pop())
print(arr.pop())
print(arr.pop())
print(arr.pop())