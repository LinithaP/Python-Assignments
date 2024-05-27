'''
5. Write a Python program to find the factorial of a number using a for loop.
'''

def fact(n):
    result = 1
    if n < 0: return 0
    if n ==0 or n==1 : return 1

    for i in range(2,n+1):
        result *= i
    return result
print(fact(5))