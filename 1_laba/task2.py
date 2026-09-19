data = [True, "hello", 5, 12.5, -200, False, False, "word", None, [1, 2], {"a": 1}]
counts = {"bool": 0, "str": 0, "int": 0, "float": 0, "NoneType": 0, "list": 0, "dict": 0}
for i in data:
    type_name = type(i).__name__
    counts[type_name] += 1
print(counts)

