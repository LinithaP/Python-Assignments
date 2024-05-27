'''
1. Write a Python program to find the common elements between two lists.
 Sample Input: l1 = [1, 2, 3, 4, 5] and l2 = [4, 5, 6, 7, 8] Sample output: [4, 5]
'''

def common_elements(l1, l2):
    s1, s2 = set(l1), set(l2)
    result = (s1 & s2)
    print(list(result))

common_elements([1, 2, 3, 4, 5],[4, 5, 6, 7, 8])
