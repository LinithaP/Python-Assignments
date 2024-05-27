'''. Write a Python program to calculate the LCM (Least Common Multiple) of two numbers.
number1 = 12, number2 = 18 LCM of 12 and 18 are: 36'''

def gdc(a,b):
    while b:
        a,b = b,a%b
    return a

def lcm(a,b):
    result = (a*b) // gdc(a,b)
    print(f"LCM of {a} and {b} are: {result}")

lcm(12,18)