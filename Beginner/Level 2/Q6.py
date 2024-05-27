'''
6. Write a Python program to check if a number is a power of two using recursion.
'''

def power_2(n):

    if n == 1:
        return True
    elif n %2 != 0 or n == 0:
        return False
    else:
        return power_2(n//2)

print(power_2(16))