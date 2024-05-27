'''.Write a program in Python to perform the following operation:
If a number is divisible by 3 it should print “Consultadd” as a string
If a number is divisible by 5 it should print “Python Training” as a string
If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a string'''

def choices(n):
    if n % 3 == 0 and n % 5 ==0:
        return ("Consultadd - Python Training")
    elif n % 3 == 0:
        return ("Consultadd")
    elif n % 5 == 0:
        return ("Python Training")
    else:
        return ""
print(choices(3))