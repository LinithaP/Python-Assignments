'''
10. Write a Python program to reverse the order of words in a given sentence.
Input_sentence = “Hello, World! Welcome to Python programming.”
Output after reverse = “programming. Python to Welcome World! Hello,”
'''

def rev(s):
    l = s.split() #gives list l

    reversed = l[::-1]

    return (" ".join(reversed))

print(rev("Hello, World! Welcome to Python programming."))