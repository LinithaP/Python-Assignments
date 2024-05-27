'''
. Write a Python program to count the frequency of each element in a list.
 Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5] Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}
'''

def freq(l):
    result = {}
    for i in l:
        result[i] = result.get(i,0) +1
    return result
print(freq([1, 2, 3, 2, 4, 1, 2, 4, 5]))