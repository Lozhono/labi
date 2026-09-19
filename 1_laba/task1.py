def v1(n: int) -> int:
    return n + 1
a = 5
b = v1(a)
print(f"a={a}, b={b}") 

# 2 variant
def v2(num: dict) -> None:
    num["n"] += 1
obj = {"n": 5}
v2(obj)
print(obj)