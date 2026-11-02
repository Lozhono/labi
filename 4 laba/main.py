from functools import reduce


# Итерирование циклами
def sum_for(*args):
    total = 0
    for i in range(len(args)):
        total += args[i]
    return total


def sum_for_of(*args):
    total = 0
    for x in args:
        total += x
    return total


def sum_while(*args):
    total = 0
    i = 0
    while i < len(args):
        total += args[i]
        i += 1
    return total


def sum_do_while(*args):
    total = 0
    if not args:
        return total
    i = 0
    while True:
        total += args[i]
        i += 1
        if i >= len(args):
            break
    return total


def sum_reduce(*args):
    return reduce(lambda acc, x: acc + x, args, 0)


# Итерирование по двумерному массиву
def max_2d(matrix):
    result = matrix[0][0]
    for row in matrix:
        for x in row:
            if x > result:
                result = x
    return result


# Итерирование объектов-справочников
def ages(persons):
    result = {}
    for name in persons:
        result[name] = persons[name]["died"] - persons[name]["born"]
    return result


print(sum_for(1, 2, 3))
print(sum_for_of(0))
print(sum_while())
print(sum_do_while(1, -1, 1))
print(sum_reduce(10, -1, -1, -1))

m = max_2d([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m)

persons = {
    "lenin": {"born": 1870, "died": 1924},
    "mao": {"born": 1893, "died": 1976},
    "gandhi": {"born": 1869, "died": 1948},
    "hirohito": {"born": 1901, "died": 1989},
}
print(ages(persons))