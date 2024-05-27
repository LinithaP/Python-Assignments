'''
11. Write a Python program to create a list of given strings individually of the list using the Python map function.
Eg. Input: ['Red', 'Blue', 'Black', 'White', 'Pink']
 Output: [['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i', 'n', 'k']]
'''

def map_func(list1):
    return list(map(list,list1))

print(map_func(['Red', 'Blue', 'Black', 'White', 'Pink']))