'''
9. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
'''
#
def iterate_list(list1,k):
    sum = 0
    try:
        for i in range(k):
            sum += (list1[i])
        print(sum)
    except IndexError:
        print("Index is out of range")

iterate_list([1,2,3,4], 5)