'''
13. Write a Python program to find if a given string starts with a given character using Lambda.
Sample input: input_string = "Hello, World!", given_char = "H" Sample Output: True
'''

starts_with_func = lambda s, c: s.startswith(c)

def check_startswith(string1, char):
    return starts_with_func(string1, char)

print(check_startswith("Hello world", "H"))