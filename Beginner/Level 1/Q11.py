'''
11. Write a Python program to calculate the sum of digits of a given number until the sum becomes a single-digit number.
Sample Input: num = 987
Sample Output: Sum_of_digits = 24,
Again compute the sum of digits so that it can be reduced to on single digit. Final Output: 6
'''

def single_sum(n):
    while n >= 10:
        st = str(n)
        digit_list = [int(i) for i in st]
        n = sum(digit_list)
    return n
print(single_sum(987))


