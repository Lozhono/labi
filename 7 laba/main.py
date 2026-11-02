# 1
def remove_element(array, item):
    if item in array:
        array.remove(item)

# 2
def remove_elements(array, *items):
    for i in items:
        remove_element(array, i)

# 3
def unique(array):
    result = []
    for x in array:
        if x not in result:
            result.append(x)
    return result

# 4
def difference(array1, array2):
    return [x for x in array1 if x not in array2]

array = [1, 2, 3, 4, 5, 6, 7]
remove_element(array, 5)
print(array)
array = ['Kiev', 'Beijing', 'Lima', 'Saratov']
remove_element(array, 'Lima')
remove_element(array, 'Berlin')
print(array)
array = [1, 2, 3, 4, 5, 6, 7]
remove_elements(array, 5, 1, 6)
print(array)
array = ['Kiev', 'Beijing', 'Lima', 'Saratov']
remove_elements(array, 'Lima', 'Berlin', 'Kiev')
print(array)
print(unique([2, 1, 1, 3, 2]))
print(unique(['top', 'bottom', 'top', 'left']))
print(difference([7, -2, 10, 5, 0], [0, 10]))
print(difference(['Beijing', 'Kiev'], ['Kiev', 'London', 'Baghdad']))