'''
12. Write a Python program to reverse a number using a while loop.
Sample Input: num = 12345 Sample Output: revnum = 54321
'''

def rev(n):
    result = 0

    while n != 0:
        num = n % 10
        result = result * 10 + num

        n //= 10
    return result
print(rev(12345))

