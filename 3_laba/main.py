
import math
import random as _random
from functools import reduce
from inspect import signature


def rand(min_value, max_value=None):
    if max_value is None:
        max_value = min_value
        min_value = 0
    return math.floor(_random.random() * (max_value - min_value + 1)) + min_value


"""generateKey"""
def generate_key(length, characters):
    key = ""
    for _ in range(length):
        key += characters[rand(len(characters) - 1)]
    return key


"""IP в число"""
def to_int32(n):
    n &= 0xFFFFFFFF
    return n - 0x100000000 if n & 0x80000000 else n
def ip_to_int(ip="127.0.0.1"):
    parts = [int(part) for part in ip.split(".")]
    shifts = [3, 2, 1, 0]
    return reduce(
        lambda acc, pair: acc + to_int32(pair[0] << (8 * pair[1])),
        zip(parts, shifts),
        0,
    )


"""Интроспекция объекта"""
def introspect(iface):
    result = []
    for key, value in iface.items():
        if callable(value):
            result.append([key, len(signature(value).parameters)])
    return result
def m2(x, y):
    return [x, y]
def m3(x, y, z):
    return [x, y, z]
iface = {
    "m1": lambda x: [x],
    "m2": m2,
    "m3": m3,
}


characters = "abcdefghijklmnopqrstuvwxyz0123456789"

print(rand(10))
print(rand(5, 10))

print(generate_key(16, characters))

print(ip_to_int())
print(ip_to_int("10.0.0.1"))
print(ip_to_int("192.168.1.10"))
print(ip_to_int("165.225.133.150"))
print(ip_to_int("0.0.0.0"))
print(hex(ip_to_int("8.8.8.8")))

print(introspect(iface))