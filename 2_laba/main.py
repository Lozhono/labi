"""Ідентифікатори"""
name = "Іван"
BIRTH_YEAR = 2006


def greet(name):
    print(f"Привіт, {name}!")


"""Цикли"""
def range_numbers(start, end):
    result = []
    for i in range(start, end + 1):
        result.append(i)
    return result


def range_odd(start, end):
    result = []
    for i in range(start, end + 1):
        if i % 2 != 0:
            result.append(i)
    return result


"""Функції"""
def average(a, b):
    return (a + b) / 2


def square(x):
    return x ** 2


def cube(x):
    return x ** 3


def calculate():
    result = []
    for i in range(10):
        result.append(average(square(i), cube(i)))
    return result


"""Об'єкти"""
def fn():
    CONST_OBJ = {"name": "Alpha"}
    var_obj = {"name": "Beta"}

    CONST_OBJ["name"] = "Alpha changed"
    var_obj["name"] = "Beta changed"

    CONST_OBJ = {"name": "Gamma"}
    var_obj = {"name": "Delta"}

    return CONST_OBJ, var_obj


def create_user(name, city):
    return {"name": name, "city": city}


"""Колекції: масив об'єктів"""
phone_book = [
    {"name": "Marcus Aurelius", "phone": "+380445554433"},
    {"name": "Julius Caesar", "phone": "+380441112233"},
    {"name": "Augustus", "phone": "+380443334455"},
    {"name": "Nero", "phone": "+380446667788"},
]


def find_phone_by_name(name):
    for record in phone_book:
        if record["name"] == name:
            return record["phone"]
    return None


"""Колекції: хеш-таблиця"""
hash_table = {}
for record in phone_book:
    hash_table[record["name"]] = record["phone"]


def find_phone_by_name_hash(name):
    return hash_table.get(name)


greet(name)
print(BIRTH_YEAR)

print(range_numbers(15, 30))
print(range_odd(15, 30))

print(calculate())

print(fn())
print(create_user("Marcus Aurelius", "Roma"))

print(find_phone_by_name("Marcus Aurelius"))
print(find_phone_by_name_hash("Marcus Aurelius"))