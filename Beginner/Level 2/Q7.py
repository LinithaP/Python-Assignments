'''
7. Write a Python function that finds the median of a list of numbers.
Sample Input: number_list = [7, 2, 5, 1, 9, 3] Sample Output: Median: 4.0
'''

def median(number_list):
    number_list.sort()
    k = len(number_list)

    if len(number_list) % 2 == 0:
        med = (number_list[k//2 - 1] + number_list[k//2]) /2
    else:
        med = number_list[k//2]
    return ("Median: ", med)

print(median([7, 2, 5, 1, 9, 3]))