'''
2. Create a function that takes a list and returns a new list with unique elements of the first list.
Sample Input: list1 = [1, 2, 2, 3, 4, 4, 5, 5] Sample Output: list2 = [1, 2, 3, 4, 5]
'''

def unique(list1):
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2

print(unique([1, 2, 2, 3, 4, 4, 5, 5] ))